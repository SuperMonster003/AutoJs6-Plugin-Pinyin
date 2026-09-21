******

### 发行历史

******

# v1.0.3

###### 2026/09/19

* `修复` AGP 9.1 构建时的 SDK XML v4 解析警告, 以及 JVM 单元测试误触发 APK 原生库对齐检查的问题 (共享构建插件 1.8.3)
* `优化` compileSdk/targetSdk 升级至 37 (Android 17)

# v1.0.2

###### 2026/09/13

* `修复` 插件版本日期受构建环境语言影响, 未统一使用英文格式的问题
* `优化` 统一多语言资源, 明确插件激活契约并校验发布产物

# v1.0.1

###### 2026/09/11

* `提示` 本版本仅改进文档与配套工程, 拼音转换行为与全部脚本 API 保持不变
* `优化` 完善多语言 README, 补充入门, 风格及选项, 接口, 常见问题和插件对比
* `优化` 文档生成器增加 --check 检查, 校验语言结构, 标点及版本一致性
* `优化` 插件中心使用说明 (plugin_instruction.md) 纳入同一套多语言 JSON 生成链路, 消除双源维护
* `优化` 补充开发路线图及 Pinyin4j 插件对比
* `优化` 统一 README 版式与 Gradle 平台版本管理方式
* `优化` 构建阶段阻止意外引入原生依赖, 并输出 JSON 校验报告

# v1.0.0

###### 2026/07/15

* `新增` Pinyin 插件服务: 插件 ID 为 pinyin, 由 AutoJs6 通过 org.autojs.plugin.PINYIN 自动发现并调用
* `新增` 拼音转换 API: `pinyin.convert(text, options)` 返回二维候选数组并附带 `compact()` 组合方法, `pinyin.simple(text)` 返回紧凑字符串
* `新增` 字典查询 API: `pinyin.fromCodePoint(codePoint)` 查询单字读音记录, `pinyin.fromPhrase(phrase)` 查询词组读音
* `新增` 六种拼音风格 (NORMAL / TONE / TONE2 / TO3NE / INITIALS / FIRST_LETTER) 与姓氏模式 (SURNAME)
* `新增` 多音字与分词支持: 内置单字, 词组, 分词三份字典及 HMM 模型, 可按需启用 segment / heteronym / group 选项
* `新增` 多语言资源: 插件信息与使用说明覆盖 10 种语言
* `新增` README 与 CHANGELOG 由 JSON 源文件与 `.python/generate_markdown.py` 生成多语言 Markdown
