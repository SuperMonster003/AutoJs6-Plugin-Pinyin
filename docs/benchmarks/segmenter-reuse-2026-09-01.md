# Jieba segmenter reuse benchmark

Date: 2026-09-01

## Question

Does keeping one lazily initialized `JiebaSegmenter` delegate for the service lifetime change cold/warm conversion cost compared with constructing a lightweight segmenter wrapper for every segmented conversion?

Code inspection established an important correction to the original Roadmap premise: `WordDictionary` and `FinalSeg` were already process singletons. The old path constructed a new `JiebaSegmenter` wrapper per call, but only the first segmented conversion loaded the word dictionary, Trie and HMM model.

## Method

- Device: Android API 36 x86_64 AVD (`AVD_API_36.1`), read-only cold app install for each variant.
- Artifact: signed Debug target APK plus instrumentation APK.
- Harness: `PinyinSegmenterBenchmarkTest`.
- Input: `音乐重要，重庆银行行长，长孙无忌。` repeated twice (34 UTF-16 code units).
- Sample: one cold Binder call, followed by nine warm Binder calls; warm latency reports min/median/max.
- Memory: process PSS and used Java heap sampled before the cold call, after the cold call and after all warm calls.
- Both variants used the same AVD, input, build type and sampling code. APKs were uninstalled between runs.

## Raw results

| Metric | Per-call wrapper baseline | Reused lazy delegate | Difference |
|---|---:|---:|---:|
| Cold call | 2762.671 ms | 3123.832 ms | +13.1% |
| Warm minimum | 562.623 ms | 590.356 ms | +4.9% |
| Warm median | 571.821 ms | 598.933 ms | +4.7% |
| Warm maximum | 670.342 ms | 625.009 ms | -6.8% |
| PSS before | 31,280 KB | 31,331 KB | +0.2% |
| PSS after cold | 135,051 KB | 129,039 KB | -4.5% |
| PSS after warm | 138,546 KB | 126,922 KB | -8.4% |
| Heap before | 2,967,136 B | 2,967,136 B | 0.0% |
| Heap after cold | 62,125,776 B | 58,422,992 B | -6.0% |
| Heap after warm | 63,510,272 B | 59,807,488 B | -5.8% |

## Interpretation

The one-run timing spread does not demonstrate a speed improvement. That result matches the corrected architecture finding: dictionary and model initialization were already singleton-backed, so removing a small wrapper allocation cannot materially change the dominant Trie construction, SQLite queries and conversion work. The lower post-run memory samples are encouraging but remain observational rather than a stable guarantee.

The implementation is still preferable because its ownership now matches the intended service lifetime and removes needless wrapper creation. `PinyinSegmenterReuseTest` separately proves that 64 concurrent calls initialize exactly one delegate and preserve all results. No latency or memory threshold is enforced in CI; the manual harness remains available for comparable future measurements.
