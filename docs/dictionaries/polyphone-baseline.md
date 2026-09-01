# 常见多音字质量基线

版本: `2026-09-01`

本基线固定“重、长、行、乐、单”五个常见多音字的候选顺序，并覆盖词组分词消歧和姓氏/复姓模式。它的用途是阻止后续词典升级悄悄改变既有行为，不代表对开放域中文或全国人名的总体准确率声明。

| 类别 | 用例数 | 当前门禁 | 覆盖示例 |
|---|---:|---|---|
| 单字候选顺序 | 5 | 5/5 数据库逐项一致 | `重 -> zhòng, chóng`; `乐 -> lè, yuè, yào, lào` |
| 词组消歧 | 7 | 7/7 词组数据库逐项一致，并经 Binder + Jieba 路径复核 | 重庆、重要、长大、行走、音乐、快乐、单于 |
| 姓氏/复姓 | 3 | 3/3 真实 Binder 转换断言 | 单田芳、长孙无忌、乐正子 |
| 合计 | 15 | 15/15 精确输出断言 | 全部使用带调拼音二维数组 |

源语料位于 `app/src/androidTest/assets/polyphone-baseline.json`。其中单字与词组用例由 `scripts/dictionaries/verify_polyphone_baseline.py` 直接对锁定 SQLite 数据验证；同一份 JSON 由 `PinyinPluginServiceTest` 通过真实服务发现、绑定和 Binder `convert` 调用再次执行，因此同时覆盖 Bundle 选项解析、分词、词组查询与姓氏逻辑。

运行方式：

```powershell
py scripts\dictionaries\verify_polyphone_baseline.py
.\gradlew.bat :app:assembleDebugAndroidTest
```

CI 的 API 35 模拟器会运行 instrumentation APK。任何候选顺序或词级读音变化都必须显式更新语料、说明来源并经人工审阅，不能只把新输出改成“绿灯”。
