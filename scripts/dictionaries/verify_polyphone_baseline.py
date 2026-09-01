#!/usr/bin/env python3
"""Validate the polyphone regression corpus against the locked SQLite data."""

from __future__ import annotations

import gzip
import json
import os
import sqlite3
import sys
import tempfile
from collections import Counter
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[2]
CORPUS_PATH = REPO_ROOT / "app" / "src" / "androidTest" / "assets" / "polyphone-baseline.json"
CHARACTERS_PATH = REPO_ROOT / "app" / "src" / "main" / "assets" / "dict-chinese-chars.db.gzip"
PHRASES_PATH = REPO_ROOT / "app" / "src" / "main" / "assets" / "dict-chinese-phrases.db.gzip"
REQUIRED_CHARACTERS = set("重长行乐单")
EXPECTED_CATEGORIES = {
    "candidate-order": 5,
    "phrase-disambiguation": 7,
    "surname": 3,
}


class BaselineError(ValueError):
    """Raised when the regression corpus or locked data do not agree."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise BaselineError(message)


def load_corpus(path: Path = CORPUS_PATH) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as source:
        corpus = json.load(source)
    require(corpus.get("schemaVersion") == 1, "schemaVersion must be 1")
    cases = corpus.get("cases")
    require(isinstance(cases, list) and cases, "cases must be a non-empty array")
    identifiers: set[str] = set()
    categories: Counter[str] = Counter()
    for case in cases:
        require(isinstance(case, dict), "each case must be an object")
        identifier = case.get("id")
        require(isinstance(identifier, str) and identifier, "each case needs an id")
        require(identifier not in identifiers, f"duplicate case id: {identifier}")
        identifiers.add(identifier)
        category = case.get("category")
        require(category in EXPECTED_CATEGORIES, f"invalid category for {identifier}: {category}")
        categories[category] += 1
        text = case.get("input")
        expected = case.get("expected")
        require(isinstance(text, str) and text, f"invalid input for {identifier}")
        require(isinstance(expected, list) and expected, f"invalid expected result for {identifier}")
        require(all(isinstance(row, list) and row for row in expected), f"empty row in {identifier}")
        require(
            all(isinstance(item, str) and item for row in expected for item in row),
            f"invalid pronunciation in {identifier}",
        )
    require(categories == Counter(EXPECTED_CATEGORIES), f"category coverage differs: {dict(categories)}")
    covered = {case["input"] for case in cases if case["category"] == "candidate-order"}
    require(covered == REQUIRED_CHARACTERS, f"candidate-order coverage differs: {covered}")
    return corpus


def database_from_gzip(path: Path) -> tuple[sqlite3.Connection, Path]:
    raw = gzip.decompress(path.read_bytes())
    handle, temporary_name = tempfile.mkstemp(prefix="autojs6-polyphone-", suffix=".db")
    os.close(handle)
    temporary_path = Path(temporary_name)
    temporary_path.write_bytes(raw)
    return sqlite3.connect(f"file:{temporary_path.as_posix()}?mode=ro", uri=True), temporary_path


def verify_data_cases(corpus: dict[str, Any]) -> Counter[str]:
    characters, character_path = database_from_gzip(CHARACTERS_PATH)
    phrases, phrase_path = database_from_gzip(PHRASES_PATH)
    passed: Counter[str] = Counter()
    try:
        for case in corpus["cases"]:
            category = case["category"]
            if category == "candidate-order":
                row = characters.execute(
                    "SELECT Pinyin FROM Dict WHERE CodePoint = ?",
                    (ord(case["input"]),),
                ).fetchone()
                require(row is not None, f"character not found: {case['input']}")
                actual = [row[0].split(",")]
                require(actual == case["expected"], f"candidate order differs for {case['id']}: {actual}")
                passed[category] += 1
            elif category == "phrase-disambiguation":
                rows = phrases.execute(
                    "SELECT Pinyin, OrderIndex FROM PhrasesDict WHERE Word = ? ORDER BY OrderIndex, rowid",
                    (case["input"],),
                ).fetchall()
                require(rows, f"phrase not found: {case['input']}")
                actual: list[list[str]] = []
                for pronunciation, order_index in rows:
                    while len(actual) < order_index:
                        actual.append([])
                    actual[order_index - 1].append(pronunciation)
                require(actual == case["expected"], f"phrase reading differs for {case['id']}: {actual}")
                passed[category] += 1
        return passed
    finally:
        characters.close()
        phrases.close()
        character_path.unlink(missing_ok=True)
        phrase_path.unlink(missing_ok=True)


def main() -> int:
    try:
        corpus = load_corpus()
        passed = verify_data_cases(corpus)
    except (BaselineError, OSError, json.JSONDecodeError, sqlite3.DatabaseError) as error:
        print(f"POLYPHONE_BASELINE_ERROR {error}", file=sys.stderr)
        return 1
    total = len(corpus["cases"])
    print(
        "POLYPHONE_BASELINE_OK "
        f"total={total} "
        f"candidate-order={passed['candidate-order']}/{EXPECTED_CATEGORIES['candidate-order']} "
        f"phrase-disambiguation={passed['phrase-disambiguation']}/{EXPECTED_CATEGORIES['phrase-disambiguation']} "
        f"surname-binder-cases={EXPECTED_CATEGORIES['surname']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
