#!/usr/bin/env python3
"""Verify, compare and regenerate the locked Pinyin/Jieba dictionary assets."""

from __future__ import annotations

import argparse
import gzip
import hashlib
import io
import json
import math
import os
import re
import sqlite3
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any, Iterable, Sequence


REPO_ROOT = Path(__file__).resolve().parents[2]
LOCK_PATH = REPO_ROOT / "data" / "dictionaries.lock.json"
DEFAULT_OUTPUT = REPO_ROOT / "build" / "dictionaries" / "review-2026-09-01"

CHARACTER_PATTERN = re.compile(
    r'dict\[0x([0-9a-fA-F]+)\] = ("(?:\\.|[^"\\])*");'
)


class DictionaryError(RuntimeError):
    """Raised when an asset or upstream snapshot differs from its lock."""


def sha256_bytes(content: bytes) -> str:
    return hashlib.sha256(content).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise DictionaryError(message)


def load_lock(path: Path = LOCK_PATH) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as source:
        lock = json.load(source)
    require(lock.get("schemaVersion") == 1, "dictionary lock schemaVersion must be 1")
    require(isinstance(lock.get("assets"), dict), "dictionary lock has no assets object")
    require(isinstance(lock.get("upstreams"), dict), "dictionary lock has no upstreams object")
    return lock


def verify_bytes(content: bytes, expected_size: int, expected_sha256: str, label: str) -> None:
    require(len(content) == expected_size, f"{label} size differs: {len(content)} != {expected_size}")
    actual_sha256 = sha256_bytes(content)
    require(actual_sha256 == expected_sha256, f"{label} SHA-256 differs: {actual_sha256}")


def sqlite_query(raw_database: bytes, query: str, parameters: Sequence[Any] = ()) -> list[tuple[Any, ...]]:
    handle, temporary_name = tempfile.mkstemp(prefix="autojs6-pinyin-dict-", suffix=".db")
    os.close(handle)
    temporary_path = Path(temporary_name)
    try:
        temporary_path.write_bytes(raw_database)
        connection = sqlite3.connect(f"file:{temporary_path.as_posix()}?mode=ro", uri=True)
        try:
            return connection.execute(query, parameters).fetchall()
        finally:
            connection.close()
    finally:
        temporary_path.unlink(missing_ok=True)


def verify_database(asset_id: str, spec: dict[str, Any], raw_database: bytes) -> dict[str, Any]:
    database = spec["database"]
    integrity = sqlite_query(raw_database, "PRAGMA integrity_check")
    require(integrity == [("ok",)], f"{asset_id} SQLite integrity check failed: {integrity}")
    table = database["table"]
    schema_rows = sqlite_query(
        raw_database,
        "SELECT sql FROM sqlite_master WHERE type = 'table' AND name = ?",
        (table,),
    )
    require(schema_rows == [(database["schema"],)], f"{asset_id} SQLite schema differs")
    row_count = sqlite_query(raw_database, f'SELECT COUNT(*) FROM "{table}"')[0][0]
    require(row_count == database["rowCount"], f"{asset_id} row count differs: {row_count}")
    if asset_id == "words":
        metadata = sqlite_query(
            raw_database,
            "SELECT value FROM metadata WHERE key = 'min_freq'",
        )
        require(metadata == [(database["metadataMinFreq"],)], "words min_freq metadata differs")
    return {
        "asset": asset_id,
        "rows": row_count,
        "uncompressedSize": len(raw_database),
    }


def verify_locked_assets(lock: dict[str, Any], root: Path = REPO_ROOT) -> list[dict[str, Any]]:
    summaries: list[dict[str, Any]] = []
    for asset_id, spec in lock["assets"].items():
        path = root / spec["path"]
        require(path.is_file(), f"missing locked asset: {spec['path']}")
        content = path.read_bytes()
        verify_bytes(content, spec["size"], spec["sha256"], spec["path"])
        if "database" in spec:
            try:
                raw_database = gzip.decompress(content)
            except (EOFError, gzip.BadGzipFile) as error:
                raise DictionaryError(f"{spec['path']} is not a valid gzip stream: {error}") from error
            verify_bytes(
                raw_database,
                spec["uncompressedSize"],
                spec["uncompressedSha256"],
                f"uncompressed {spec['path']}",
            )
            summaries.append(verify_database(asset_id, spec, raw_database))
        else:
            require(content.count(b"\r\n") == spec["lineCount"], "HMM CRLF line count differs")
            require(content.count(b"\n") == spec["lineCount"], "HMM LF line count differs")
            summaries.append({"asset": asset_id, "rows": spec["lineCount"], "uncompressedSize": len(content)})
    return summaries


def git_output(repository: Path, *arguments: str) -> bytes:
    try:
        return subprocess.check_output(
            ["git", "-C", str(repository), *arguments],
            stderr=subprocess.STDOUT,
        )
    except (OSError, subprocess.CalledProcessError) as error:
        output = getattr(error, "output", b"").decode("utf-8", errors="replace").strip()
        raise DictionaryError(f"git {' '.join(arguments)} failed in {repository}: {output}") from error


def upstream_blob(
    lock: dict[str, Any],
    asset_id: str,
    repositories: dict[str, Path],
) -> bytes:
    spec = lock["assets"][asset_id]
    source = spec["source"]
    upstream_id = source["upstream"]
    require(upstream_id in repositories, f"no local clone supplied for {upstream_id}")
    repository = repositories[upstream_id]
    require((repository / ".git").exists(), f"not a Git clone: {repository}")
    upstream = lock["upstreams"][upstream_id]
    commit = source.get("commit", upstream["commit"])
    content = git_output(repository, "show", f"{commit}:{source['path']}")
    verify_bytes(content, len(content), source["blobSha256"], f"{upstream_id}:{source['path']}")
    return content


def parse_character_source(content: bytes) -> list[tuple[int, str]]:
    text = content.decode("utf-8")
    rows = [(int(code_point, 16), json.loads(value)) for code_point, value in CHARACTER_PATTERN.findall(text)]
    require(rows, "character source produced no rows")
    require(len(rows) == len({row[0] for row in rows}), "character source contains duplicate code points")
    return rows


def parse_phrase_source(content: bytes) -> list[tuple[str, str, int]]:
    text = content.decode("utf-8")
    start = text.index("{")
    end = text.rindex("};") + 1
    json_body = re.sub(r",\s*}", "\n}", text[start:end])
    phrase_map = json.loads(json_body)
    rows = [
        (word, pronunciation, slot_index)
        for word, slots in phrase_map.items()
        for slot_index, candidates in enumerate(slots, 1)
        for pronunciation in candidates
    ]
    require(rows, "phrase source produced no rows")
    return rows


def parse_word_source(content: bytes) -> tuple[list[tuple[int, str, float, float, str]], float]:
    parsed: list[tuple[str, float, str]] = []
    for line_number, line in enumerate(content.decode("utf-8").splitlines(), 1):
        if not line:
            continue
        parts = line.split()
        require(len(parts) == 3, f"invalid Jieba row at line {line_number}")
        word, frequency, part_of_speech = parts
        parsed.append((word.lower(), float(frequency), part_of_speech))
    total = sum(row[1] for row in parsed)
    require(total > 0, "Jieba total frequency is not positive")
    rows = [
        (index, word, frequency, math.log(frequency / total), part_of_speech)
        for index, (word, frequency, part_of_speech) in enumerate(parsed, 1)
    ]
    return rows, math.log(2.0 / total)


def locked_database_bytes(lock: dict[str, Any], asset_id: str) -> bytes:
    return gzip.decompress((REPO_ROOT / lock["assets"][asset_id]["path"]).read_bytes())


def compare_upstreams(lock: dict[str, Any], repositories: dict[str, Path]) -> list[dict[str, Any]]:
    characters = parse_character_source(upstream_blob(lock, "characters", repositories))
    actual_characters = sqlite_query(
        locked_database_bytes(lock, "characters"),
        "SELECT CodePoint, Pinyin FROM Dict ORDER BY rowid",
    )
    require(actual_characters == characters, "character database differs semantically from pinned source")

    phrases = parse_phrase_source(upstream_blob(lock, "phrases", repositories))
    actual_phrases = sqlite_query(
        locked_database_bytes(lock, "phrases"),
        "SELECT Word, Pinyin, OrderIndex FROM PhrasesDict ORDER BY rowid",
    )
    require(actual_phrases == phrases, "phrase database differs semantically from pinned source")

    words, minimum = parse_word_source(upstream_blob(lock, "words", repositories))
    actual_words = sqlite_query(
        locked_database_bytes(lock, "words"),
        "SELECT id, word, frequency, normalized_freq, part_of_speech FROM dictionary ORDER BY id",
    )
    require(actual_words == words, "segmentation database differs semantically from pinned source")
    actual_minimum = sqlite_query(
        locked_database_bytes(lock, "words"),
        "SELECT value FROM metadata WHERE key = 'min_freq'",
    )
    require(actual_minimum == [(minimum,)], "segmentation min_freq differs from pinned source")

    hmm_source = upstream_blob(lock, "hmm", repositories)
    hmm_expected = hmm_source.replace(b"\r\n", b"\n").replace(b"\n", b"\r\n")
    hmm_actual = (REPO_ROOT / lock["assets"]["hmm"]["path"]).read_bytes()
    require(hmm_actual == hmm_expected, "HMM asset differs from pinned source after CRLF normalization")

    return [
        {"asset": "characters", "sourceRows": len(characters)},
        {"asset": "phrases", "sourceRows": len(phrases)},
        {"asset": "words", "sourceRows": len(words)},
        {"asset": "hmm", "sourceRows": hmm_expected.count(b"\n")},
    ]


def create_database(path: Path, schema: str, rows: Iterable[Sequence[Any]], insert_sql: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.unlink(missing_ok=True)
    connection = sqlite3.connect(path)
    try:
        connection.execute(schema)
        connection.executemany(insert_sql, rows)
        connection.commit()
    finally:
        connection.close()


def deterministic_gzip(content: bytes) -> bytes:
    output = io.BytesIO()
    with gzip.GzipFile(filename="", mode="wb", fileobj=output, compresslevel=9, mtime=0) as archive:
        archive.write(content)
    return output.getvalue()


def regenerate(lock: dict[str, Any], repositories: dict[str, Path], output: Path) -> list[dict[str, Any]]:
    output.mkdir(parents=True, exist_ok=True)
    generated: list[dict[str, Any]] = []

    characters = parse_character_source(upstream_blob(lock, "characters", repositories))
    phrases = parse_phrase_source(upstream_blob(lock, "phrases", repositories))
    words, minimum = parse_word_source(upstream_blob(lock, "words", repositories))

    raw_paths = {
        "characters": output / "dict-chinese-chars.db",
        "phrases": output / "dict-chinese-phrases.db",
        "words": output / "dict-chinese-words.db",
    }
    create_database(
        raw_paths["characters"],
        lock["assets"]["characters"]["database"]["schema"],
        characters,
        "INSERT INTO Dict (CodePoint, Pinyin) VALUES (?, ?)",
    )
    create_database(
        raw_paths["phrases"],
        lock["assets"]["phrases"]["database"]["schema"],
        phrases,
        "INSERT INTO PhrasesDict (Word, Pinyin, OrderIndex) VALUES (?, ?, ?)",
    )
    create_database(
        raw_paths["words"],
        lock["assets"]["words"]["database"]["schema"],
        words,
        "INSERT INTO dictionary (id, word, frequency, normalized_freq, part_of_speech) VALUES (?, ?, ?, ?, ?)",
    )
    connection = sqlite3.connect(raw_paths["words"])
    try:
        connection.execute("CREATE TABLE metadata (\n    key TEXT NOT NULL PRIMARY KEY,\n    value REAL NOT NULL\n)")
        connection.execute("INSERT INTO metadata (key, value) VALUES ('min_freq', ?)", (minimum,))
        connection.commit()
    finally:
        connection.close()

    for asset_id, raw_path in raw_paths.items():
        generated_path = output / Path(lock["assets"][asset_id]["path"]).name
        raw = raw_path.read_bytes()
        generated_path.write_bytes(deterministic_gzip(raw))
        raw_path.unlink()
        generated.append(
            {
                "asset": asset_id,
                "path": generated_path,
                "size": generated_path.stat().st_size,
                "sha256": sha256_bytes(generated_path.read_bytes()),
                "lockedSha256": lock["assets"][asset_id]["sha256"],
            }
        )

    hmm = upstream_blob(lock, "hmm", repositories).replace(b"\r\n", b"\n").replace(b"\n", b"\r\n")
    hmm_path = output / "prob_emit.txt"
    hmm_path.write_bytes(hmm)
    generated.append(
        {
            "asset": "hmm",
            "path": hmm_path,
            "size": len(hmm),
            "sha256": sha256_bytes(hmm),
            "lockedSha256": lock["assets"]["hmm"]["sha256"],
        }
    )

    report = output / "DICTIONARY_DIFF.md"
    lines = [
        "# Dictionary regeneration review",
        "",
        f"Lock version: `{lock['lockVersion']}`",
        "",
        "Regeneration writes review candidates only; it never replaces application assets.",
        "Semantic equivalence is checked separately with `compare-upstream`. SQLite and gzip bytes may differ across tool versions.",
        "",
        "| Asset | Candidate SHA-256 | Locked SHA-256 | Byte-identical |",
        "|---|---|---|---|",
    ]
    for item in generated:
        identical = "yes" if item["sha256"] == item["lockedSha256"] else "no"
        lines.append(
            f"| {item['asset']} | `{item['sha256']}` | `{item['lockedSha256']}` | {identical} |"
        )
    report.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    return generated


def repository_arguments(args: argparse.Namespace) -> dict[str, Path]:
    require(args.hotoo is not None, "--hotoo is required for this command")
    require(args.jieba is not None, "--jieba is required for this command")
    return {
        "hotoo-pinyin": args.hotoo.resolve(),
        "huaban-jieba-analysis": args.jieba.resolve(),
    }


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser("verify", help="verify committed hashes, SQLite schemas and row counts")
    for command in ("compare-upstream", "regenerate"):
        subparser = subparsers.add_parser(command)
        subparser.add_argument("--hotoo", type=Path, help="local clone of hotoo/pinyin")
        subparser.add_argument("--jieba", type=Path, help="local clone of huaban/jieba-analysis")
        if command == "regenerate":
            subparser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        lock = load_lock()
        if args.command == "verify":
            summaries = verify_locked_assets(lock)
        elif args.command == "compare-upstream":
            verify_locked_assets(lock)
            summaries = compare_upstreams(lock, repository_arguments(args))
        else:
            verify_locked_assets(lock)
            repositories = repository_arguments(args)
            compare_upstreams(lock, repositories)
            summaries = regenerate(lock, repositories, args.output.resolve())
    except (DictionaryError, OSError, UnicodeError, json.JSONDecodeError, sqlite3.DatabaseError) as error:
        print(f"DICTIONARY_ERROR {error}", file=sys.stderr)
        return 1
    for summary in summaries:
        printable = {key: str(value) if isinstance(value, Path) else value for key, value in summary.items()}
        print("DICTIONARY_OK " + " ".join(f"{key}={value}" for key, value in printable.items()))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
