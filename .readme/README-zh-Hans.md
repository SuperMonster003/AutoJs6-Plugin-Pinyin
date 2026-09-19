<!--suppress HtmlDeprecatedAttribute, HttpUrlsUsage -->

<div align="center">
  <p>
    <picture>
      <source srcset="https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/app/src/main/res/mipmap-night/ic_launcher.png?raw=true" media="(prefers-color-scheme: dark)" />
      <img src="https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/app/src/main/res/mipmap/ic_launcher.png?raw=true" alt="autojs6-plugin-pinyin-ic-launcher" border="0" width="128" />
    </picture>
  </p>

  <p>用于汉语拼音转换的 Pinyin 插件</p>

  <p>
    <a href="https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/releases"><img alt="GitHub release (latest by date)" src="https://img.shields.io/github/v/release/SuperMonster003/AutoJs6-Plugin-Pinyin?label=Release"/></a>
    <a href="https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/issues"><img alt="GitHub closed issues" src="https://img.shields.io/github/issues/SuperMonster003/AutoJs6-Plugin-Pinyin?color=A24232&label=Issues"/></a>
    <a href="https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/LICENSE"><img alt="GitHub License" src="https://img.shields.io/github/license/SuperMonster003/AutoJs6-Plugin-Pinyin?color=534BAE&label=License"/></a>
  </p>
</div>

******

### 语言 (Languages)

******

当前 README.md 支持以下语言:

- 简体中文 [zh-Hans] # 当前
- [繁體中文 (香港) [zh-Hant-HK]](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/.readme/README-zh-Hant-HK.md)
- [繁體中文 (台灣) [zh-Hant-TW]](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/.readme/README-zh-Hant-TW.md)
- [English [en]](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/.readme/README-en.md)
- [Français [fr]](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/.readme/README-fr.md)
- [Español [es]](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/.readme/README-es.md)
- [日本語 [ja]](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/.readme/README-ja.md)
- [한국어 [ko]](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/.readme/README-ko.md)
- [Русский [ru]](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/.readme/README-ru.md)
- [العربية [ar]](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/.readme/README-ar.md)

******

### 简介

******

Pinyin 插件 (Pinyin Plugin) 为 AutoJs6 提供离线汉语拼音转换能力. 安装后, 脚本可通过全局对象 `pinyin` 将中文文本转换为多种风格的拼音, 支持多音字候选, 词组词典, Jieba 分词与姓氏模式, 适用于排序, 检索, 首字母索引, 注音标注等自动化场景.

插件是一个独立安装的 APK, 运行于自身进程, 由 AutoJs6 通过插件机制自动发现并以 AIDL 通信. 单字, 词组与分词字典全部内置 (安装包约 6 MB), 转换完全在设备本地完成, 无需网络. 自 AutoJs6 v6.8.0 起, 宿主的 `pinyin` 模块由本插件提供实现. API 设计对齐 JavaScript 生态广泛使用的 [pinyin](https://github.com/hotoo/pinyin) 库, 熟悉该库的用户可直接上手.

本插件与 [Pinyin4j](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin4j) 互为姊妹插件: 本插件字典完备, 支持多音字与分词, 适合追求读音准确性的场景; Pinyin4j 基于经典 Java 库 pinyin4j, 体积仅约 0.3 MB, 适合轻量逐字注音. 两者可同时安装, 详见下方 `姊妹插件对比`.

******

### 功能亮点

******

- 开箱即用: 安装后由 AutoJs6 自动发现, 无需重启宿主, 脚本直接使用全局对象 `pinyin`.
- 字典完备: 内置单字, 词组与分词三份字典及 HMM 模型, 完全离线, 不发起任何网络请求.
- 多音字支持: `heteronym` 选项返回每个字的全部候选读音, 词组词典自动选取常用读音.
- Jieba 分词: `segment` 选项启用分词, 按词组消歧多音字, 提升整句注音准确率.
- 六种拼音风格: 声调符号, 数字声调, 数字紧随韵母, 无声调, 声母, 首字母, 覆盖排序/检索/注音等场景.
- 专名模式: `SURNAME` 优先采用姓氏专用读音; `PLACE_NAME` 先应用有来源可追溯的精选地名语料, 未命中再回退普通转换.
- 结果可组合: `convert` 返回的二维候选数组附带 `compact()` 方法, 一步展开全部读音组合.
- 多语言: 插件信息, 使用说明, README 与更新日志覆盖 10 种语言.

******

### 使用方法

******

1. 将 AutoJs6 升级到内部版本号 3923 (6.7.1 Alpha4) 及以上; 自 v6.8.0 起拼音能力完全由插件承担, 推荐直接使用最新版本.
2. 从 [Releases](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/releases) 页面下载插件 APK 安装到运行 AutoJs6 的设备上, 或直接在 AutoJs6 的插件中心在线安装.
3. 打开 AutoJs6 的插件中心, 确认 `Pinyin` 插件已被识别, 完成授权并处于启用状态.
4. 在脚本中直接调用 `pinyin` 全局对象, 参考下方 `快速上手` 示例; 也可先运行 `快速自检` 确认插件生效.

> 插件仅提供一个通用安装包 (纯 JVM 实现, 不区分 CPU 架构), 支持 Android 7.0 (API 24) 及以上的设备. 插件无独立界面, 安装后不在桌面创建图标, 由 AutoJs6 统一发现与管理.

******

### 快速上手

******

基础转换: `convert` 返回二维候选数组, `simple` 返回紧凑字符串:

```javascript
console.log(pinyin.convert("中心"));                     // [["zhōng"], ["xīn"]]
console.log(pinyin.convert("中心", { style: "TONE2" })); // [["zhong1"], ["xin1"]]
console.log(pinyin.simple("拼音插件"));                  // "pinyinchajian"
console.log(pinyin.simple("拼音插件", true));            // "pin1yin1cha1jian4"
```

多音字: `heteronym` 选项返回全部候选读音, `compact()` 展开为读音组合:

```javascript
let result = pinyin.convert("重庆", { heteronym: true });
console.log(result);
console.log(result.compact());
```

分词消歧, 姓氏模式与地名模式:

```javascript
console.log(pinyin.simple("音乐重要", false, true));
console.log(pinyin.convert("单田芳", { mode: "SURNAME" }));
console.log(pinyin.convert("六安", { mode: "PLACE_NAME" })); // [["lù"], ["ān"]]
console.log(pinyin.convert("六安", {
  customDictionary: { "六安": [["liú"], ["ān"]] },
})); // [["liú"], ["ān"]]
```

******

### 拼音风格

******

`style` 选项控制拼音输出风格, 以 "中" (zhōng) 为例:

| 风格 | 输出 | 说明 |
|---|---|---|
| `TONE` | `zhōng` | 声调符号标注在韵母上 (默认) |
| `TONE2` | `zhong1` | 声调以数字 0-4 附加在拼音末尾 |
| `TO3NE` | `zho1ng` | 声调数字紧跟在韵母之后 |
| `NORMAL` | `zhong` | 不带声调 |
| `INITIALS` | `zh` | 仅返回声母 (零声母字返回空字符串) |
| `FIRST_LETTER` | `z` | 仅返回拼音首字母 |

`style` 取值不区分大小写, 可传字符串 (如 `"TONE2"`) 或常量 (如 `pinyin.STYLE_TONE2`).

******

### 选项

******

`pinyin.convert(text, options)` 支持以下选项:

| 选项 | 默认值 | 说明 |
|---|---|---|
| `style` | `TONE` | 拼音风格, 见上方 `拼音风格` |
| `mode` | `NORMAL` | 转换模式: `NORMAL` 普通模式, `SURNAME` 姓氏模式, `PLACE_NAME` 精选地名读音模式 |
| `segment` | `false` | 启用 Jieba 分词, 借助词组词典消歧多音字 |
| `heteronym` | `false` | 返回每个字的全部候选读音, 而非仅首选读音 |
| `group` | `false` | 按分词得到的词组合并拼音候选 (需配合 `segment`) |
| `customDictionary` | `{}` | 当前调用的汉字读音覆盖, 格式为 `{ 词: [[带调候选], ...] }`; 最长匹配优先且不持久化, 需兼容的 AutoJs6 宿主与插件 |

模式也可传常量 (如 `pinyin.MODE_PLACE_NAME`). `PLACE_NAME` 对小规模人工复核语料执行最长匹配, 未收录文本回退 `NORMAL`; 它不是全国标准地名全量库, 覆盖范围与出处参见 [语料及来源](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/docs/dictionaries/place-names.md).

******

### 脚本 API

******

`pinyin` 全局对象提供以下方法 (直接调用 `pinyin(text, options)` 等价于 `pinyin.convert`):

```text
pinyin(text, options?)                   -> string[][]
pinyin.convert(text, options?)           -> string[][]
pinyin.simple(text, numeric?, segment?)  -> string
pinyin.compare(textA, textB)             -> number
pinyin.compact(matrix)                   -> string[][]
pinyin.fromCodePoint(codePoint)          -> string | null
pinyin.fromPhrase(phrase)                -> string[][]
pinyin.STYLE_* / pinyin.MODE_*           -> constants
```

- `convert` 返回二维数组: 每个汉字或词组字位占一行, 行内为候选读音; 未收录字符与非中文字符原样占一行. 返回数组附带 `compact()` 方法, 可展开为全部读音组合.
- `simple` 返回紧凑字符串: 每字取首选读音直接拼接; 第 2 参数为 `true` 时输出数字声调 (TONE2 风格), 否则不带声调; 第 3 参数为 `true` 时启用分词.
- `fromCodePoint` 查询单字码点在字典中的原始读音记录 (逗号分隔的带调候选), 未收录时返回 `null`.
- `fromPhrase` 查询词组词典, 返回该词组每个字位的候选读音; 未收录时返回空数组.
- 全部方法同步返回; 首次调用需初始化内置字典, 可能稍有延迟.

#### Node.js

在 Node.js 运行时中, 通过公开 `autojs6:bridge` facade 调用同一 provider, 并显式声明 `pinyin` capability:

```javascript
const { callAutoJs } = require("autojs6:bridge");

(async () => {
  const result = await callAutoJs(
    "pinyin",
    "convert",
    ["中心", { style: "TONE2" }],
    { permissions: ["pinyin"] },
  );
  console.log(result); // [["zhong1"], ["xin1"]]
})();
```

******

### 快速自检

******

安装并启用插件后, 运行以下单行脚本:

```javascript
console.log(pinyin.simple("拼音"));
```

输出 `pinyin` 即表示插件已正常工作.

******

### 常见问题

******

#### 如何确认插件已经生效?

打开 AutoJs6 的插件中心, 能看到 `Pinyin` 插件并处于启用状态即表示宿主已识别; 再运行上方 `快速自检` 脚本, 输出 `pinyin` 即为生效.

#### 脚本报错提示缺少插件或 `pinyin` 不可用?

请确认 AutoJs6 内部版本号不低于 3923, 且插件已在插件中心完成安装, 授权与启用. 自 AutoJs6 v6.8.0 起, 宿主不再内置拼音实现, 拼音能力完全由本插件承担.

#### 为什么应用列表和桌面上没有插件图标?

这是正常现象. 插件没有独立界面, 也不在桌面创建启动图标, 安装后由 AutoJs6 在后台自动发现和调用, 全部交互都在 AutoJs6 内完成.

#### 多音字读音不符合预期?

默认按单字首选读音转换. 建议开启 `segment` 选项借助词组词典与分词消歧 (如 `pinyin.simple(text, false, true)`); 需要全部候选时使用 `heteronym` 选项. 若常用词读音仍不正确, 欢迎通过 [Issues](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/issues) 反馈以完善词典.

#### 与姊妹插件 Pinyin4j 如何选择?

需要多音字, 分词, 词组或姓氏读音时选择本插件; 只需轻量逐字注音且在意安装包体积时选择 [Pinyin4j](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin4j). 两者互不冲突, 可同时安装, 详见下方 `姊妹插件对比`.

#### 插件会联网或申请敏感权限吗?

不会. 全部字典内置于安装包, 转换在设备本地完成; 插件清单仅声明与 AutoJs6 通信所需的插件权限, 不申请网络, 存储等任何敏感系统权限.

#### 安装包为什么有约 6 MB?

安装包内置单字字典, 词组字典, 分词词库与 HMM 模型四份数据, 以此换取完全离线与更高的注音准确率. 若更在意体积, 可考虑约 0.3 MB 的姊妹插件 [Pinyin4j](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin4j).

#### 为什么 `customDictionary` 或 Node.js 拼音调用被拒绝?

这些路由要求兼容的 AutoJs6 与 Pinyin 插件版本. Node.js 调用必须声明 `permissions: ["pinyin"]`. 自定义词典仅对当前调用生效, 且必须满足文档中的条目数, 候选数, 组合数与 64 KiB 限制.

******

### 权限与安全

******

插件在设计上尽可能收窄数据面与权限面:

- 最小权限: 插件清单仅声明 AutoJs6 插件权限 (`org.autojs.permission.PLUGIN`), 不申请网络, 存储, 相机等任何敏感系统权限.
- 本地转换: 待转换文本仅经 Binder 在设备内传递, 字典全部内置, 全程离线, 数据不出设备.
- 签名与授权: AutoJs6 会校验插件签名, 插件需在插件中心授权并启用后才能被脚本调用; 服务与唤醒入口均受插件权限保护, 第三方应用无法直接调用.
- 开源可审计: 插件代码, 字典打包与文档生成链路全部开源.

请仅从官方 [Releases](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/releases) 页面或 AutoJs6 插件中心获取插件安装包; 来源不明的安装包即使名称与版本号相同, 也可能被篡改.

******

### 姊妹插件对比

******

AutoJs6 官方提供两个拼音插件, 各有侧重, 可同时安装:

| 对比项 | [Pinyin](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin) | [Pinyin4j](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin4j) |
|---|---|---|
| 底层实现 | 内置字典 + Jieba 分词 | 经典 Java 库 `pinyin4j` |
| 全局对象 | `pinyin` | `pinyin4j` |
| 多音字 | 支持, 可返回全部候选 | 不支持, 固定取首个读音 |
| 分词与词组 | 支持 (词组词典 + Jieba) | 不支持, 逐字转换 |
| 姓氏模式 | 支持 | 不支持 |
| 输出形式 | 二维候选数组 (可 `compact()` 组合) 或紧凑字符串 | 字符串, 可配置分隔符 |
| 风格与格式 | 6 种拼音风格 | 3 种声调格式 + 大小写 + `ü` 表示方式 |
| 安装包体积 | 约 6 MB (内置字典) | 约 0.3 MB |
| 适用场景 | 读音准确性优先: 多音字, 词组, 人名 | 体积与简单性优先: 快速逐字注音 |

两个插件互不依赖也互不冲突; 同时安装后, 脚本可按需分别调用 `pinyin` 与 `pinyin4j`. Pinyin4j 插件详见 [AutoJs6-Plugin-Pinyin4j](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin4j).

******

### 插件接口

******

以下信息面向 AutoJs6 宿主与插件开发者, 宿主通过这些标识发现插件并完成能力协商:

```text
application id: io.github.supermonster003.autojs6.plugin.pinyin
plugin id: pinyin
engine: pinyin
variant: default
discovery action: org.autojs.plugin.PINYIN
discovery category: pinyin
wake action: org.autojs.plugin.action.WAKE
binder interface: IPinyinPlugin
binder methods: getInfo / convert / simple / fromCodePoint / fromPhrase
minimum host build: 3923
native library: none (pure JVM, all ABIs)
```

`PinyinPluginService` 响应 `org.autojs.plugin.PINYIN` action (category `pinyin`), 通过 AIDL 接口 `IPinyinPlugin` 暴露 5 个方法; `convert` 与 `fromPhrase` 以 JSON 字符串返回二维数组, 选项经 `Bundle` 传递 (键: `mode` / `style` / `segment` / `heteronym` / `group` / `custom_dictionary_json`). 自定义词典要求 `pinyin.customDictionary.v1` capability. 服务与 `WakeActivity` 均受 `org.autojs.permission.PLUGIN` 权限保护, 第三方应用无法直接调用.

******

### 开发路线图

******

插件的能力规划与完成情况以可勾选清单维护在 ROADMAP.md 中, 按里程碑组织并附验收条件, 涵盖地名模式, 词典演进, 自定义词典, 性能优化与持续集成等方向. 未勾选条目表示规划意向而非当前版本能力, 欢迎通过 Issues 参与讨论.

- [查看 ROADMAP.md](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/ROADMAP.md)

******

### 发行历史

******

#### v1.0.3

_2026/09/19_

- `修复` AGP 9.1 构建时的 SDK XML v4 解析警告及 JVM 单元测试组装任务误触发 APK 原生库对齐检查的问题 (共享构建插件 1.8.3)
- `优化` 将 compileSdk 与 targetSdk 提升到 37 (Android 17), 插件行为不受新目标版本影响

#### v1.0.2

_2026/09/13_

- `修复` 插件版本日期固定使用英文, 不随构建机器的语言变化
- `优化` 统一多语言资源, 明确插件激活契约并校验发布产物

#### v1.0.1

_2026/09/11_

- `提示` 本版本仅改进文档与配套工程, 拼音转换行为与全部脚本 API 保持不变
- `优化` 重构 10 种语言的 README: 新增使用方法, 快速上手, 拼音风格与选项速查表, 脚本 API, 快速自检, 常见问题, 权限与安全, 姊妹插件对比及插件接口等章节
- `优化` 文档生成脚本升级为同族插件统一实现: 支持 `--check` 漂移检测, 跨语言键位与形状对齐校验, 全角符号拦截以及版本对齐校验
- `优化` 插件中心使用说明 (`plugin_instruction.md`) 纳入同一套多语言 JSON 生成链路, 消除双源维护
- `优化` 新增 ROADMAP.md 开发路线图, 并与姊妹插件 Pinyin4j 建立双向互链与选型对比
- `优化` 统一 README 版式与 Gradle 平台版本管理方式
- `优化` 构建阶段阻止意外引入原生依赖, 并输出 JSON 校验报告

##### 更多发行历史可参阅

* [CHANGELOG.md](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/app/src/main/assets/doc/CHANGELOG-zh-Hans.md)

******

### 构建

******

本节面向希望从源码构建插件的开发者.

构建 debug APK:

```powershell
.\gradlew.bat :app:assembleDebug
```

运行 JVM 单元测试并构建 instrumentation 测试 APK:

```powershell
.\gradlew.bat :app:testDebugUnitTest :app:assembleDebugAndroidTest
```

构建 release APK (单一通用包; 在不入库的 `sign.properties` 中配置签名后自动签名):

```powershell
.\gradlew.bat :app:assembleRelease
```

一键构建并校验已签名的 universal APK, 生成 `SHA256SUMS.txt` 与基于英文 CHANGELOG 的 `RELEASE_NOTES.md`:

```powershell
py scripts\release\prepare_release.py
```

校验多语言文档源与生成产物是否同步 (持续集成亦会执行):

```powershell
py .python\generate_markdown.py --check
```

构建参数集中于 `version.properties`: 最低 SDK 24 (Android 7.0), 目标 SDK 37, 当前版本 1.0.3.

******

### 本地化与文档生成

******

```text
.readme/common.json
.readme/lang_*.json
.readme/template_readme.md
.readme/template_plugin_instruction.md
.changelog/lang_*.json
.changelog/template_changelog.md
.python/generate_markdown.py
app/src/main/assets/doc/CHANGELOG-*.md
app/src/main/res/values-*/strings.xml
app/src/main/res/raw-*/plugin_instruction.md
```

`strings.xml` 提供本地化插件描述, `plugin_instruction.md` 提供宿主插件中心展示的使用说明. README, 更新日志与使用说明均由 JSON 源生成: 修改 `.readme/` 与 `.changelog/` 下的源文件后运行 `py .python/generate_markdown.py` 重新生成全部产物, 生成产物不手工编辑; 运行 `py .python/generate_markdown.py --check` 可校验源文件与产物是否同步.

******

### 许可

******

项目代码使用 [Mozilla Public License 2.0](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/LICENSE). 内置分词实现移植自 [jieba-analysis](https://github.com/huaban/jieba-analysis) 项目, API 设计对齐 [pinyin](https://github.com/hotoo/pinyin) 库.

******

### 相关链接

******

- AutoJs6 Pinyin 文档: https://docs.autojs6.com/#/pinyin
- AutoJs6 项目: https://github.com/SuperMonster003/AutoJs6
- 姊妹插件 Pinyin4j: https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin4j
- pinyin 库 (API 设计参考): https://github.com/hotoo/pinyin
- jieba-analysis 项目: https://github.com/huaban/jieba-analysis


[16 KB page alignment and build verification](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/docs/16kb.md)
