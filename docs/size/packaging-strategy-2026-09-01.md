# APK 体积策略评估

- 评估日期: `2026-09-01`
- 被测 release APK: `app-release.apk`
- APK SHA-256: `9ae16c0320b9906b8ae35e089e6525c6857fb596096030ae03ba0295a3bf2828`
- APK 大小: `6,234,761` bytes (5.95 MiB)
- 原生库条目: `0`

## ZIP 条目测量

| 数据 | 源资产大小 | APK 内压缩大小 | APK 占比 |
|---|---:|---:|---:|
| 单字拼音数据库 | 299,008 | 299,071 | 4.80% |
| 词组拼音数据库 | 1,286,826 | 1,283,215 | 20.58% |
| Jieba 分词词库 | 4,225,844 | 4,227,125 | 67.80% |
| 未登录词 HMM 参数 | 700,668 | 260,290 | 4.17% |
| 四份数据合计 | — | 6,069,701 | 97.35% |

这里按 APK ZIP 条目的 `compress_size` 计量。条目、中央目录、签名块和对齐会使真正拆分出的变体大小与简单减法略有差异，因此下面的精简数字只作为上限估算。

## lite 可行性

分词词库本身占 APK `67.80%`；连同 HMM 参数，分词栈占 `4,487,415` bytes (`71.97%`)。直接删掉两者的理论剩余大小约为 `1,747,346` bytes (1.67 MiB)。体积收益显著，但当前不可作为无感优化：

- `segment` 是已发布选项；去掉分词词库会让该选项报错或静默退化，均改变现有契约。
- AutoJs6 当前按 `pinyin` engine 选择服务，并在脚本 APK 打包时预期四份资产；宿主尚无 full/lite 变体选择语义。
- 只删分词数据仍保留约 1.3 MB 的词组库，但普通长文本没有 Jieba 切词后无法稳定命中词组，准确性取舍不容易向用户解释。
- 已有约 0.3 MB 的姊妹 Pinyin4j 插件承接轻量逐字转换需求，无需在本插件内立即复制一个能力重叠且容易误选的变体。

## 决策

当前保持单一 `default` universal APK，并完整保留单字、词组、分词与 HMM 四份离线数据；不发布 lite 变体。这个结论是“暂不拆分”，不是永久否决。满足以下任一条件时重新评估：宿主提供显式 variant 选择与能力协商；full APK 超过 8 MiB；分词栈超过 APK 的 75%；或出现有代表性的用户需求且 Pinyin4j 无法覆盖。

若未来实施 lite，必须使用独立 variant/清晰名称，`segment` 在能力协商阶段即显示为不支持，full 仍为默认，并分别执行 Binder、文档、打包资产与升级兼容测试；不得让同一 `default` 包静默缩水。

复测命令：

```powershell
.\gradlew.bat :app:assembleRelease
py scripts\ci\analyze_apk_size.py app\build\outputs\apk\release\app-release.apk --report docs\size\packaging-strategy-2026-09-01.md
```
