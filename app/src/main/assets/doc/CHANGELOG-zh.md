******

### 发行历史

******

# v1.0.2

###### 2026/09/13

* `修复` 插件版本日期固定使用英文, 不随构建机器的语言变化
* `优化` 统一多语言资源, 明确插件激活契约并校验发布产物

# v1.0.1

###### 2026/09/11

* `提示` 本版本仅改进文档与配套工程, 拼音转换行为与全部脚本 API 保持不变
* `优化` 重构 10 种语言的 README: 新增使用方法, 快速上手, 拼音风格与选项速查表, 脚本 API, 快速自检, 常见问题, 权限与安全, 姊妹插件对比及插件接口等章节
* `优化` 文档生成脚本升级为同族插件统一实现: 支持 `--check` 漂移检测, 跨语言键位与形状对齐校验, 全角符号拦截以及版本对齐校验
* `优化` 插件中心使用说明 (`plugin_instruction.md`) 纳入同一套多语言 JSON 生成链路, 消除双源维护
* `优化` 新增 ROADMAP.md 开发路线图, 并与姊妹插件 Pinyin4j 建立双向互链与选型对比
* `优化` 统一 README 版式与 Gradle 平台版本管理方式
* `优化` 构建阶段阻止意外引入原生依赖, 并输出 JSON 校验报告

# v1.0.0

###### 2026/07/15

* `新增` Pinyin 插件服务: 插件 ID 为 `pinyin`, 由 AutoJs6 通过 `org.autojs.plugin.PINYIN` 自动发现并调用
* `新增` 拼音转换 API: `pinyin.convert(text, options)` 返回二维候选数组并附带 `compact()` 组合方法, `pinyin.simple(text)` 返回紧凑字符串
* `新增` 字典查询 API: `pinyin.fromCodePoint(codePoint)` 查询单字读音记录, `pinyin.fromPhrase(phrase)` 查询词组读音
* `新增` 六种拼音风格 (`NORMAL` / `TONE` / `TONE2` / `TO3NE` / `INITIALS` / `FIRST_LETTER`) 与姓氏模式 (`SURNAME`)
* `新增` 多音字与分词支持: 内置单字, 词组, 分词三份字典及 HMM 模型, 可按需启用 `segment` / `heteronym` / `group` 选项
* `新增` 多语言资源: 插件信息与使用说明覆盖 10 种语言
* `新增` README 与 CHANGELOG 由 JSON 源文件与 `.python/generate_markdown.py` 生成多语言 Markdown
