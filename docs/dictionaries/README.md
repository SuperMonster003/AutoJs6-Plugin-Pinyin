# 词典来源、锁定与更新流程

本项目随 APK 分发的单字、词组、分词与 HMM 四份历史数据，现已由 `data/dictionaries.lock.json` 固定来源提交、源文件 SHA-256、成品/解压后 SHA-256、SQLite schema 与行数。锁定的当前数据不会随上游自动变化。

## 已确认来源

| 资产 | 上游固定点 | 语义转换 | 当前规模 |
|---|---|---|---|
| `dict-chinese-chars.db.gzip` | [hotoo/pinyin `865f101`](https://github.com/hotoo/pinyin/tree/865f10195a25533bb44cda62017d94c5fb9db42e/data) 的 `dict-zi.ts` | 按源文件顺序写入 code point 与有序候选 | 41,244 行 |
| `dict-chinese-phrases.db.gzip` | 同一 hotoo/pinyin 固定点的 `phrases-dict.ts` | 依次展开词组、字位与该字位候选 | 127,820 行 |
| `dict-chinese-words.db.gzip` | [huaban/jieba-analysis `9c6527f`](https://github.com/huaban/jieba-analysis/tree/9c6527fdd9602034ea6267a8a04255a8b0612814/src/main/resources) 的 `dict.txt` | 词项转小写；归一化频率为 `ln(frequency / total)`，未知词下限为 `ln(2 / total)` | 349,045 行 |
| `prob_emit.txt` | [huaban/jieba-analysis `3ec44e7`](https://github.com/huaban/jieba-analysis/blob/3ec44e7ec983b5a768f42f8b0b736b7f316a1cf7/src/main/resources/prob_emit.txt) | 内容不变，仅采用 CRLF 行尾 | 35,228 行 |

hotoo/pinyin 使用 MIT 许可证；huaban/jieba-analysis 使用 Apache-2.0 许可证。运行时代码对 hotoo/pinyin 的 API 语义保持兼容，分词实现来自 huaban/jieba-analysis 的 Kotlin/Android 适配。

上述结论不是通过文件名推测：`compare-upstream` 会从固定 Git 对象读取源文件，验证 blob 哈希，并将全部 41,244 / 127,820 / 349,045 行及 HMM 内容与当前资产逐项比较。

## 日常校验

以下命令完全离线，不获取上游网络内容；CI 每次构建都会执行：

```powershell
py scripts\dictionaries\manage_dictionaries.py verify
py scripts\dictionaries\generate_place_names.py --check
```

第一条同时校验压缩包与解压数据库哈希、gzip 可读性、SQLite 完整性、schema、行数及分词 `min_freq` 元数据。第二条校验精选地名 JSON 与运行时映射/来源表没有漂移。

## 上游比较与再生成

更新前先把两个上游仓库克隆到任意临时目录；脚本只读取锁文件指定的提交，即使克隆当前位于更新的分支也不会静默采用最新数据：

```powershell
git clone https://github.com/hotoo/pinyin.git build\dictionary-upstream\hotoo-pinyin
git clone https://github.com/huaban/jieba-analysis.git build\dictionary-upstream\jieba-analysis

py scripts\dictionaries\manage_dictionaries.py compare-upstream `
  --hotoo build\dictionary-upstream\hotoo-pinyin `
  --jieba build\dictionary-upstream\jieba-analysis

py scripts\dictionaries\manage_dictionaries.py regenerate `
  --hotoo build\dictionary-upstream\hotoo-pinyin `
  --jieba build\dictionary-upstream\jieba-analysis
```

`regenerate` 只在 `build/dictionaries/review-2026-09-01/` 生成候选数据库、gzip 文件和 `DICTIONARY_DIFF.md`，绝不覆盖 `app/src/main/assets/`。SQLite 页布局、SQLite 版本与 gzip 头可能导致候选包与历史二进制哈希不同，因此采用“源语义逐行一致 + 当前发布资产哈希锁定”两层校验。

## 更新门禁

词典升级必须由人工 PR 完成，不设置定时下载或自动合并：

1. 在独立分支把锁文件中的上游 commit 与 blob SHA-256 更新为已审阅固定点。
2. 运行 `compare-upstream` 和 `regenerate`，审阅来源变化、行级差异、候选顺序、APK 体积及 `DICTIONARY_DIFF.md`。
3. 运行多音字基线、JVM 测试与真实 Binder instrumentation 测试；变化必须在 PR 描述中解释。
4. 审核通过后才以候选资产替换发布资产，并同步更新锁文件中的成品/解压哈希、大小、schema 与行数。
5. `PLACE_NAME` 精选语料走独立的 `data/place-names.json` 复核流程，详见 [place-names.md](place-names.md)。
