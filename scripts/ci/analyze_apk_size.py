#!/usr/bin/env python3
"""Measure the packaged dictionary footprint and optionally write the strategy report."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
import zipfile
from pathlib import Path
from typing import Any


DICTIONARY_ENTRIES = {
    "characters": "assets/dict-chinese-chars.db.gzip",
    "phrases": "assets/dict-chinese-phrases.db.gzip",
    "segmentation": "assets/dict-chinese-words.db.gzip",
    "hmm": "assets/prob_emit.txt",
}


class SizeAnalysisError(RuntimeError):
    """Raised when the APK cannot support a meaningful size analysis."""


def analyze(apk_path: Path) -> dict[str, Any]:
    if not apk_path.is_file():
        raise SizeAnalysisError(f"APK does not exist: {apk_path}")
    apk_bytes = apk_path.read_bytes()
    try:
        with zipfile.ZipFile(apk_path) as archive:
            if archive.testzip() is not None:
                raise SizeAnalysisError("APK ZIP integrity check failed")
            entries = {}
            for asset_id, entry_name in DICTIONARY_ENTRIES.items():
                try:
                    info = archive.getinfo(entry_name)
                except KeyError as error:
                    raise SizeAnalysisError(f"APK is missing {entry_name}") from error
                entries[asset_id] = {
                    "name": entry_name,
                    "sourceBytes": info.file_size,
                    "packagedBytes": info.compress_size,
                    "apkPercent": info.compress_size * 100.0 / len(apk_bytes),
                }
            native_entries = [name for name in archive.namelist() if name.startswith("lib/") and name.endswith(".so")]
    except zipfile.BadZipFile as error:
        raise SizeAnalysisError(f"invalid APK ZIP: {error}") from error

    dictionary_bytes = sum(entry["packagedBytes"] for entry in entries.values())
    segmentation_stack_bytes = entries["segmentation"]["packagedBytes"] + entries["hmm"]["packagedBytes"]
    return {
        "apk": str(apk_path.resolve()),
        "apkBytes": len(apk_bytes),
        "apkSha256": hashlib.sha256(apk_bytes).hexdigest(),
        "entries": entries,
        "dictionaryPackagedBytes": dictionary_bytes,
        "dictionaryApkPercent": dictionary_bytes * 100.0 / len(apk_bytes),
        "segmentationStackPackagedBytes": segmentation_stack_bytes,
        "segmentationStackApkPercent": segmentation_stack_bytes * 100.0 / len(apk_bytes),
        "theoreticalWithoutSegmentationStackBytes": len(apk_bytes) - segmentation_stack_bytes,
        "nativeEntryCount": len(native_entries),
    }


def mib(value: int) -> str:
    return f"{value / (1024 * 1024):.2f} MiB"


def render_report(result: dict[str, Any]) -> str:
    entries = result["entries"]
    lines = [
        "# APK 体积策略评估",
        "",
        "评估日期: `2026-09-01`  ",
        f"被测 release APK: `{Path(result['apk']).name}`  ",
        f"APK SHA-256: `{result['apkSha256']}`  ",
        f"APK 大小: `{result['apkBytes']:,}` bytes ({mib(result['apkBytes'])})  ",
        f"原生库条目: `{result['nativeEntryCount']}`",
        "",
        "## ZIP 条目测量",
        "",
        "| 数据 | 源资产大小 | APK 内压缩大小 | APK 占比 |",
        "|---|---:|---:|---:|",
    ]
    labels = {
        "characters": "单字拼音数据库",
        "phrases": "词组拼音数据库",
        "segmentation": "Jieba 分词词库",
        "hmm": "未登录词 HMM 参数",
    }
    for asset_id in DICTIONARY_ENTRIES:
        entry = entries[asset_id]
        lines.append(
            f"| {labels[asset_id]} | {entry['sourceBytes']:,} | {entry['packagedBytes']:,} | {entry['apkPercent']:.2f}% |"
        )
    lines.extend(
        [
            f"| 四份数据合计 | — | {result['dictionaryPackagedBytes']:,} | {result['dictionaryApkPercent']:.2f}% |",
            "",
            "这里按 APK ZIP 条目的 `compress_size` 计量。条目、中央目录、签名块和对齐会使真正拆分出的变体大小与简单减法略有差异，因此下面的精简数字只作为上限估算。",
            "",
            "## lite 可行性",
            "",
            f"分词词库本身占 APK `{entries['segmentation']['apkPercent']:.2f}%`；连同 HMM 参数，分词栈占 `{result['segmentationStackPackagedBytes']:,}` bytes (`{result['segmentationStackApkPercent']:.2f}%`)。直接删掉两者的理论剩余大小约为 `{result['theoreticalWithoutSegmentationStackBytes']:,}` bytes ({mib(result['theoreticalWithoutSegmentationStackBytes'])})。体积收益显著，但当前不可作为无感优化：",
            "",
            "- `segment` 是已发布选项；去掉分词词库会让该选项报错或静默退化，均改变现有契约。",
            "- AutoJs6 当前按 `pinyin` engine 选择服务，并在脚本 APK 打包时预期四份资产；宿主尚无 full/lite 变体选择语义。",
            "- 只删分词数据仍保留约 1.3 MB 的词组库，但普通长文本没有 Jieba 切词后无法稳定命中词组，准确性取舍不容易向用户解释。",
            "- 已有约 0.3 MB 的姊妹 Pinyin4j 插件承接轻量逐字转换需求，无需在本插件内立即复制一个能力重叠且容易误选的变体。",
            "",
            "## 决策",
            "",
            "当前保持单一 `default` universal APK，并完整保留单字、词组、分词与 HMM 四份离线数据；不发布 lite 变体。这个结论是“暂不拆分”，不是永久否决。满足以下任一条件时重新评估：宿主提供显式 variant 选择与能力协商；full APK 超过 8 MiB；分词栈超过 APK 的 75%；或出现有代表性的用户需求且 Pinyin4j 无法覆盖。",
            "",
            "若未来实施 lite，必须使用独立 variant/清晰名称，`segment` 在能力协商阶段即显示为不支持，full 仍为默认，并分别执行 Binder、文档、打包资产与升级兼容测试；不得让同一 `default` 包静默缩水。",
            "",
            "复测命令：",
            "",
            "```powershell",
            ".\\gradlew.bat :app:assembleRelease",
            "py scripts\\ci\\analyze_apk_size.py app\\build\\outputs\\apk\\release\\app-release.apk --report docs\\size\\packaging-strategy-2026-09-01.md",
            "```",
            "",
        ]
    )
    return "\n".join(lines)


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("apk", type=Path)
    parser.add_argument("--report", type=Path, help="write the Markdown strategy report")
    parser.add_argument("--json", action="store_true", help="print full JSON instead of one-line metrics")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        result = analyze(args.apk)
        if args.report is not None:
            args.report.parent.mkdir(parents=True, exist_ok=True)
            args.report.write_text(render_report(result), encoding="utf-8", newline="\n")
    except (OSError, SizeAnalysisError) as error:
        print(f"APK_SIZE_ERROR {error}", file=sys.stderr)
        return 1
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(
            "APK_SIZE_OK "
            f"apk_bytes={result['apkBytes']} "
            f"dictionary_percent={result['dictionaryApkPercent']:.2f} "
            f"segmentation_percent={result['entries']['segmentation']['apkPercent']:.2f} "
            f"segmentation_stack_percent={result['segmentationStackApkPercent']:.2f} "
            f"native_entries={result['nativeEntryCount']}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
