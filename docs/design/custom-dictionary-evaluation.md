# 自定义用户词典协议评估

- 评估日期: `2026-09-01`
- 状态: 设计完成，尚未实现；需要 AutoJs6 宿主与共享 `pinyin-api` 契约先行配合。

## 当前边界

现有 `IPinyinPlugin.convert(String, Bundle)` AIDL 方法无需新增事务即可携带新选项，但当前共享 `PinyinOptionKeys` 只有 `mode/style/segment/heteronym/group`，宿主 `Pinyin.toPluginOptions()` 也只复制这五项。因此仅修改插件无法让脚本中的自定义词典到达插件进程；这不是插件单仓库可以安全发布的功能。

Android 官方文档说明 Binder 事务缓冲区当前约 1 MB，且由进程内所有在途事务共享。把大型词典直接塞入每次 `Bundle` 会重复序列化，并可能触发 `TransactionTooLargeException`；设计必须主动采用远低于系统极限的边界，而不能把 1 MB 当作可用配额。参考：[Android Parcelables and Bundles](https://developer.android.com/guide/components/activities/parcelables-and-bundles)。

## 推荐的 v1 方案

首版采用“小型、单次转换作用域、内联 JSON”的保守协议：

| 项目 | 决策 |
|---|---|
| 载体 | 继续使用 `convert` 的 `Bundle`，新增共享键 `custom_dictionary_json`；不增加 AIDL 方法，不传自定义 Parcelable |
| 格式 | UTF-8 JSON object：键为 1–32 个 Unicode code point 的字/词，值为按字位排列的二维带调拼音候选数组 |
| 上限 | 编码后最多 64 KiB、最多 1,024 个词条、每字位最多 8 个候选；宿主与插件双重校验 |
| 生命周期 | 仅当前一次 `convert` 调用；不落盘、不跨调用缓存、不跨脚本共享 |
| 优先级 | 自定义精确/最长词组 > `SURNAME` 或 `PLACE_NAME` 专用读音 > 内置词组 > 内置单字；模式仍互斥 |
| 未命中 | 保持当前模式与 NORMAL 回退，不改变未知/非汉字保留语义 |
| 分词关系 | 自定义多字词先做最长匹配，剩余片段再走 Jieba；不修改进程级 Jieba 单例词典，避免跨调用污染 |
| 错误 | 超限、空候选、字位数不符或非法拼音时，由宿主在发起 Binder 前抛出确定性参数错误；插件再次 fail-closed 校验 |
| 兼容 | 新宿主只向声明 `custom_dictionary_v1` capability 的插件发送该键；旧宿主不发送，旧插件继续忽略未知键 |

64 KiB 是项目策略上限而非 Binder 保证值，给待转换文本、返回 JSON 和并发 IPC 留出显著余量。若实际需求证明需要更大的长期词典，应另立 v2：通过新增 AIDL 方法传 `ParcelFileDescriptor`/流、显式 session token 和可撤销生命周期，不能悄悄放大内联 Bundle。

## 协同实现顺序

1. 在共享 `pinyin-api` 增加 option key 与 capability key，追加协议文档和宿主/插件契约测试。
2. 宿主把 JavaScript object 规范化为稳定 JSON，执行 64 KiB/条目/字位/候选校验，并仅对声明能力的插件转发。
3. 插件实现不可变的 per-call trie/最长匹配；转换结束立即释放，不写入 `WordDictionary` 单例。
4. 增加旧宿主→新插件、新宿主→旧插件、新宿主→新插件三组兼容测试，以及 64 KiB 边界和恶意输入 Binder 测试。
5. 完成宿主发布后再在 README 宣布该能力；在此之前 Roadmap 只标记“评估完成”，不标记“功能可用”。

## 未采用的方案

- 随包 assets：只能提供开发者构建时词典，不是用户运行时词典，并会产生无法隔离的全局状态。
- 插件持久化文件：需要新增存储、版本、清理和多脚本所有权模型，超出首版需求。
- 直接修改 Jieba 单例：词条会跨脚本/调用泄漏，且并发撤销困难。
- 不设上限的 Bundle/Parcelable：与 Binder 的共享固定缓冲区约束冲突。

结论：v1 方案可行且不需要改变现有 AIDL 方法签名，但必须先升级共享 API 常量、能力协商和宿主转发逻辑。本仓库暂不单方面实现半条链路。
