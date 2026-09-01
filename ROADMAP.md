# AutoJs6 Pinyin 插件 Roadmap

更新日期: 2026-09-01

本文档是 Pinyin 插件从"可用的拼音转换服务"逐步演进为"文档完善, 工程可靠, 能力可扩展"的汉语拼音方案的执行清单. 每个条目只有在代码/文档与可验证的验收条件同时满足后才可勾选.

## 状态与证据规则

- `[x]`: 已完成, 且本仓库存在可复核证据 (代码, 测试, 脚本或生成产物).
- `[ ]`: 尚未完成; 括号中的 `插件` / `API` / `宿主` / `测试` / `CI` / `发布` / `依赖` 表示主要落点.
- 未勾选条目属于规划意向, 不代表当前版本能力; 标注 "宿主先行" 的条目需等待 AutoJs6 宿主先行支持, 标注 "契约升级" 的条目涉及 AIDL 契约变更, 需插件与宿主协同演进.

## 总览

| 里程碑 | 状态 | 核心结果 | 主要落点 |
|---|---|---|---|
| M0 基线插件 | 已完成 | 拼音转换服务, 分词与多音字能力, 多语言资源 | 插件/发布 |
| M1 文档与发布体验 | 已完成 | 用户导向文档, 文档自动生成与校验, v1.0.1 | 发布 |
| M2 工程化与持续集成 | 已完成 | 单元/仪器测试, 构建与文档 CI, 发布物料脚本化 | 测试/CI/发布 |
| M3 转换能力增强 | 进行中 | 精选语料驱动的 PLACE_NAME 地名模式, 分词器复用, 自定义词典评估, 宿主先行项 | API/插件/宿主 |
| M4 词典与数据演进 | 已完成 | 词典上游锁定与再生成门禁, 多音字质量基线, full/lite 体积决策 | 依赖/插件/发布 |

依赖顺序:

```text
M0 ──> M1 ──> M2 ──> M3 (宿主先行条目需 AutoJs6 先行)
        └──────────> M4 (词典/数据项可与 M2/M3 并行)
```

## M0: 基线插件 (v1.0.0, 已完成)

- [x] (插件) Pinyin 插件服务与 AIDL 契约: `PinyinPluginService` 响应 `org.autojs.plugin.PINYIN` (category `pinyin`), Binder 接口为 `IPinyinPlugin`, 提供 `getInfo()` / `convert(text, options)` / `simple(text, enableNumericTone, enableSegment)` / `fromCodePoint(codePoint)` / `fromPhrase(phrase)` 五个方法 (`app/src/main/java/io/github/supermonster003/autojs6/plugin/pinyin/PinyinPluginService.kt`); 另提供 `WakeActivity` 供宿主唤醒插件进程.
- [x] (插件) 6 种拼音风格 (TONE / TONE2 / TO3NE / NORMAL / INITIALS / FIRST_LETTER) 与 NORMAL / SURNAME / PLACE_NAME 三种转换模式; convert 通过 Bundle 接收 style / mode / segment / heteronym / group 数值选项, 字符串名称与非法取值的规范化/报错由 AutoJs6 宿主负责; PLACE_NAME 的精选语料范围与回退语义见 M3.
- [x] (插件) 内置词典与分词: 单字/词组/分词词典以 gzip SQLite 随包分发 (约 0.3 / 1.3 / 4.2 MB), 词级分词基于 huaban/jieba-analysis 的 Kotlin 移植 (`app/src/main/java/com/huaban/analysis/jieba/`), 未登录词回退 HMM 参数 (prob_emit); segment 选项按短词粒度 (cutSmall, 词长不超过 4) 切分后逐词标注.
- [x] (插件) API 语义对齐 hotoo/pinyin JS 库: convert 返回二维数组 (每字一组候选读音), heteronym 开启时返回全部候选; 宿主全局 `pinyin(text)` 即 `pinyin.convert`, 且返回结果绑定 `compact()` 方法.
- [x] (插件) `PluginInfo` 完整上报: id/engine/variant (`pinyin` / `pinyin` / `default`), 版本名与版本号, 作者, `@raw/plugin_instruction` 使用说明, 纯 JVM 空 ABI 列表及最低宿主版本 (versionCode 3923, 即 AutoJs6 6.7.1 Alpha4) (`app/src/main/java/io/github/supermonster003/autojs6/plugin/pinyin/PluginRuntimeInfo.kt`).
- [x] (发布) 纯 JVM 实现, 单一 universal APK (约 6.2 MB), 无原生库依赖; 多语言资源: `strings.xml` 与 `plugin_instruction.md` 覆盖 10 种语言.

验收条件: 在 versionCode 不低于 3923 的 AutoJs6 中安装, 授权并启用后, 脚本可直接调用 `pinyin` 全局对象完成各风格拼音转换. (已满足)

## M1: 文档与发布体验 (v1.0.1, 已完成)

- [x] (发布) README 重构为用户导向结构 (2026-08-31): 简介 / 功能亮点 / 使用方法 / 快速上手 / 拼音风格 / 选项 / 脚本 API / 快速自检 / 常见问题 / 权限与安全 / 姊妹插件对比 / 插件接口 / 开发路线图 / 构建 / 本地化与文档生成, 10 种语言全部由 JSON 源自动生成.
- [x] (发布) CHANGELOG 文案面向用户重写: 每条先讲可感知的结果, 再补技术细节, 10 种语言同步.
- [x] (发布) 文档生成脚本升级至同族插件最新实现 (`.python/generate_markdown.py`): 新增 `--check` 漂移检测, 跨语言键位与列表形状对齐校验, 全角符号拦截, 以及 `version.properties` 与最新 CHANGELOG 条目的版本对齐校验; 配套 `.python/check_markdown.bat`.
- [x] (发布) `plugin_instruction.md` 纳入生成链路: `.readme/template_plugin_instruction.md` 与同一组 10 语言 JSON 生成全部 11 份 Android 资源产物, 消除双源维护.
- [x] (发布) 新增与姊妹项目 [AutoJs6-Plugin-Pinyin4j](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin4j) 的互链与逐项对比表, 帮助用户按需选择实现.
- [x] (发布) 新建本 ROADMAP.md 并在 README 增加 "开发路线图" 章节挂链; 版本提升至 v1.0.1 (versionBuild 10), CHANGELOG 同步记录本次文档整改.

验收条件: `.python/generate_markdown.py --check` 本地全绿; 新用户仅凭 README 即可独立完成安装, 生效确认与首次转换. (已满足)

## M2: 工程化与持续集成 (2026-09-01, 已完成)

- [x] (测试) 单元测试基础设施与首批 JVM 用例: `PinyinConverterTest` 覆盖 6 种风格, 默认与覆盖选项, heteronym/segment/group 组合, 分词多词输出, 中英文/emoji 混排, 姓氏与 simple 模式, 直接词典查询及空输入; `PluginRuntimeInfoTest` 断言版本, 作者, id/engine/variant, 使用说明引用, 纯 JVM ABI 字段与 `REQUIRES_HOST_VERSION`.
- [x] (测试) instrumentation 用例: `PinyinPluginServiceTest` 通过 `org.autojs.plugin.PINYIN` action 与 `pinyin` category 发现并绑定真实 Binder 服务, 断言 `getInfo()` 运行时字段, 对 convert/simple/fromCodePoint/fromPhrase 逐一往返, 覆盖实际 Bundle 选项, 6 种风格, 分词, 多音字, 分组, 姓氏模式, PLACE_NAME 差分读音/格式/回退及 null/越界输入; 已在 API 36 x86_64 隔离模拟器通过, CI 使用 API 35 Google APIs 模拟器复核.
- [x] (CI) GitHub Actions 文档工作流 `.github/workflows/markdown.yml`: push/PR/手动运行 `.python/check_markdown.bat`, 阻止 10 种语言的源文件与 36 份生成产物发生漂移.
- [x] (CI) GitHub Actions 构建流水线 `.github/workflows/build.yml`: push/PR/手动运行 `:app:testDebugUnitTest`, `:app:assembleDebug` 与 `:app:assembleDebugAndroidTest`; `scripts/ci/verify_universal_apk.py` 校验单 APK, 纯 JVM 与四份必要词典/参数资源, 上传构建产物后由 `scripts/ci/verify_binder_round_trip.sh` 在模拟器执行真实 Binder 往返.
- [x] (CI) 清洁环境可复现性: 平台版本插件从仅开发机可解析的旧坐标迁移到 Maven Central 上的 `io.github.supermonster003.autojs6-platform-versions` 1.6.0; 已使用全新 Gradle 用户目录与空 Maven Local 冷启动完成单元测试, Debug APK 与 instrumentation APK 构建.
- [x] (发布) Release 产物脚本化: `scripts/release/prepare_release.py` 一键构建并归集已签名 universal APK, 校验英文 CHANGELOG 与 `version.properties`, APK Manifest 版本名/版本号, ZIP/DEX/词典内容, 纯 JVM 约束, CRC32, SHA-256 与 APK 签名, 原子生成 `SHA256SUMS.txt` 及基于英文 CHANGELOG 的 `RELEASE_NOTES.md`; 9 个标准库测试覆盖完整流程与关键拒绝路径, 真实 v1.0.1 签名包流程已通过.

验收条件: 主分支每次提交自动完成构建, 单元测试与文档校验; 发布产物由脚本生成且哈希可追溯. (已满足)

## M3: 转换能力增强 (进行中)

- [x] (插件/测试) PLACE_NAME 地名模式落地 (2026-09-01): `data/place-names.json` 首批收录 15 个从政府网站逐条复核、与普通逐字首选读音存在差异的地名 (如 蚌埠 bèng bù, 六安 lù ān, 铅山 yán shān), 由 `scripts/dictionaries/generate_place_names.py` 校验并生成运行时映射与 `docs/dictionaries/place-names.md`; 转换按最长地名匹配, 未命中片段回退 NORMAL, SURNAME / PLACE_NAME 为互斥模式. JVM 差分/最长匹配/格式/回退测试与真实 Binder instrumentation 用例固定行为; CI 阻止语料生成产物漂移. 该语料明确为精选集而非全国地名全量库.
- [x] (插件/测试) 分词器实例复用 (2026-09-01): 服务通过 `ReusablePinyinSegmenter` 在首次 segment 调用时构建并在服务生命周期复用同一 `JiebaSegmenter`; `PinyinSegmenterReuseTest` 以 64 个并发调用证明委托仅初始化一次. 代码审计同时修正原规划的假设: `WordDictionary` / `FinalSeg` 原本已是进程单例, 旧实现每次只新建轻量包装对象而非重复装载词典; API 36 AVD 的同输入前后冷/热/PSS/堆数据与不夸大性能收益的结论记录于 `docs/benchmarks/segmenter-reuse-2026-09-01.md`.
- [x] (API/宿主/插件) 自定义用户词典协议评估 (2026-09-01): `docs/design/custom-dictionary-evaluation.md` 对照现有 AIDL / `PinyinOptionKeys` / 宿主 Bundle 转发路径, 选定小型 per-call JSON 方案 (64 KiB, 1,024 条, 不持久化), 明确最长匹配、优先级、生命周期、双端校验、能力协商与旧版回退; 大型词典预留 ParcelFileDescriptor/session v2, 不把 Binder 约 1 MB 共享缓冲区当可用配额.
- [ ] (宿主先行/契约升级) 自定义用户词典实现: 先在共享 `pinyin-api` 增加 option/capability key, 再由宿主完成 JavaScript 对象规范化与能力感知转发, 插件实现不可变 per-call trie; 覆盖新旧宿主/插件组合与恶意/边界输入后方可发布. 当前插件不单方面暴露半成品能力.
- [ ] (宿主先行) 宿主顶层 `pinyin.compare` 与 `pinyin.compact` 完善: 宿主当前顶层入口为返回空串的占位实现 (仅 convert 结果上绑定的 `compact()` 可用), 插件侧数据已可支撑; 待宿主补齐路由后同步更新文档与 FAQ.
- [ ] (宿主先行) Node.js 运行时支持: 宿主侧 `pinyin` 目前为 Rhino 专属; 待宿主完成调用路由与资源边界设计后复用同一插件能力, 并更新 FAQ.

验收条件: 每项能力先有可复核的预期输出语料与测试, 再修改插件与宿主; 未发布的宿主能力不提前标记为插件现有功能.

## M4: 词典与数据演进 (2026-09-01, 已完成)

- [x] (依赖/CI) 词典上游跟进机制: `data/dictionaries.lock.json` 固定 hotoo/pinyin 与 huaban/jieba-analysis 的提交、源 blob/发布资产/解压数据库 SHA-256、大小、schema 与行数; `manage_dictionaries.py verify` 离线校验全部资产, `compare-upstream` 已对固定 Git 对象完成 41,244 / 127,820 / 349,045 行及 35,228 行 HMM 的逐项语义比对, `regenerate` 仅在 `build/` 生成候选与差分报告且绝不覆盖发布资产. 更新规则要求人工 PR, 测试和审阅, 不自动吸收或合并上游变化 (`docs/dictionaries/README.md`).
- [x] (插件/测试) 多音字质量基线: `polyphone-baseline.json` 固定 重/长/行/乐/单 的 5/5 单字候选顺序, 重庆/重要/长大/行走/音乐/快乐/单于 的 7/7 词组读音, 以及 单田芳/长孙无忌/乐正子 的 3/3 姓氏/复姓输出; Python 直接校验锁定数据库, instrumentation 通过真实 Binder 执行同一份 15 用例语料 (`docs/dictionaries/polyphone-baseline.md`). 这里的 15/15 是封闭回归集通过率, 不宣称开放域准确率.
- [x] (发布) 体积策略评估: 当前 release APK 实测 6,234,761 bytes, Jieba 分词词库在 APK ZIP 中占 67.80%, 连同 HMM 占 71.97%; lite 理论收益显著, 但会破坏已发布的 `segment` 选项, 且宿主尚无 full/lite variant 选择语义. 因已有约 0.3 MB 的 Pinyin4j 姊妹插件覆盖轻量逐字场景, 当前决定继续发布单一 full universal APK, 四份离线数据不缩水; 重评阈值与未来 lite 门禁记录于 `docs/size/packaging-strategy-2026-09-01.md`, 测量可由 `analyze_apk_size.py` 复现.

验收条件: 词典与数据的每次调整均有来源, 差分与测试证据; 任何精简变体不得默认牺牲既有功能.

## 边界 (非目标)

- 不做通用 NLP 工具箱: 分词能力仅服务于拼音标注场景, 不对外承诺独立的分词 API.
- 不提供独立界面与桌面入口: 插件仅通过 AutoJs6 插件权限被宿主调用, 不接受第三方应用访问.
- 不自定义宿主 API 形态: `pinyin` 全局对象的方法集与返回结构由 AutoJs6 宿主定义, 插件侧忠实提供转换数据.
- 不引入网络能力: 转换始终基于内置词典在设备本地完成.
- 不做注音符号或其他罗马化体系: 本插件聚焦汉语拼音; 其他体系的评估见姊妹项目 [AutoJs6-Plugin-Pinyin4j](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin4j) 的 Roadmap.
