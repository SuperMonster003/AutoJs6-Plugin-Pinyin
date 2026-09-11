<!--suppress HtmlDeprecatedAttribute, HttpUrlsUsage -->

<div align="center">
  <p>
    <picture>
      <source srcset="https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/app/src/main/res/mipmap-night/ic_launcher.png?raw=true" media="(prefers-color-scheme: dark)" />
      <img src="https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/app/src/main/res/mipmap/ic_launcher.png?raw=true" alt="autojs6-plugin-pinyin-ic-launcher" border="0" width="128" />
    </picture>
  </p>

  <p>ملحق Pinyin لتحويل النص الصيني الى بينيين</p>

  <p>
    <a href="https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/releases"><img alt="GitHub release (latest by date)" src="https://img.shields.io/github/v/release/SuperMonster003/AutoJs6-Plugin-Pinyin?label=Release"/></a>
    <a href="https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/issues"><img alt="GitHub closed issues" src="https://img.shields.io/github/issues/SuperMonster003/AutoJs6-Plugin-Pinyin?color=A24232&label=Issues"/></a>
    <a href="https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/LICENSE"><img alt="GitHub License" src="https://img.shields.io/github/license/SuperMonster003/AutoJs6-Plugin-Pinyin?color=534BAE&label=License"/></a>
  </p>
</div>

******

### اللغات (Languages)

******

يدعم README.md الحالي اللغات التالية:

- [简体中文 [zh-Hans]](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/.readme/README-zh-Hans.md)
- [繁體中文 (香港) [zh-Hant-HK]](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/.readme/README-zh-Hant-HK.md)
- [繁體中文 (台灣) [zh-Hant-TW]](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/.readme/README-zh-Hant-TW.md)
- [English [en]](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/.readme/README-en.md)
- [Français [fr]](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/.readme/README-fr.md)
- [Español [es]](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/.readme/README-es.md)
- [日本語 [ja]](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/.readme/README-ja.md)
- [한국어 [ko]](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/.readme/README-ko.md)
- [Русский [ru]](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/.readme/README-ru.md)
- العربية [ar] # الحالية

******

### مقدمة

******

يوفر مكون Pinyin الإضافي (Pinyin Plugin) لـ AutoJs6 قدرة تحويل النص الصيني إلى بينيين دون اتصال. بعد التثبيت, يمكن للبرامج النصية عبر الكائن العام `pinyin` تحويل النص الصيني إلى بينيين بأنماط متعددة, مع دعم مرشحات الأحرف متعددة القراءات, وقاموس العبارات, وتقسيم الكلمات بواسطة Jieba, ووضع الألقاب, مما يناسب سيناريوهات الأتمتة مثل الفرز والبحث والفهرسة بالحرف الأول والتدوين الصوتي.

يأتي المكون الإضافي كحزمة APK مستقلة التثبيت تعمل في عمليتها الخاصة; يكتشفه AutoJs6 تلقائيا عبر آلية المكونات الإضافية ويتواصل معه عبر AIDL. قواميس الأحرف المفردة والعبارات وتقسيم الكلمات مضمنة كلها (حجم الحزمة نحو 6 MB), فيجري التحويل بالكامل محليا على الجهاز دون أي شبكة. ومنذ AutoJs6 v6.8.0, يوفر هذا المكون تنفيذ وحدة `pinyin` في المضيف. صمم API بما يتوافق مع مكتبة [pinyin](https://github.com/hotoo/pinyin) واسعة الانتشار في بيئة JavaScript, فيمكن لمن يعرفها البدء مباشرة.

هذا المكون و [Pinyin4j](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin4j) مكونان إضافيان شقيقان: هذا المكون قواميسه كاملة ويدعم تعدد القراءات وتقسيم الكلمات, فيناسب السيناريوهات التي تتطلب دقة اللفظ; بينما يقوم Pinyin4j على مكتبة Java الكلاسيكية pinyin4j وحجمه نحو 0.3 MB فقط, فيناسب التحويل الخفيف حرفا بحرف. يمكن تثبيتهما معا, وانظر `مقارنة المكونين الشقيقين` أدناه.

******

### أبرز الميزات

******

- جاهز فور التثبيت: يكتشفه AutoJs6 تلقائيا بعد التثبيت دون إعادة تشغيل المضيف, وتستخدم البرامج النصية الكائن العام `pinyin` مباشرة.
- قواميس كاملة: ثلاثة قواميس مضمنة (الأحرف المفردة والعبارات وتقسيم الكلمات) مع نموذج HMM, بعمل كامل دون اتصال ولا أي طلبات شبكة.
- دعم تعدد القراءات: يعيد خيار `heteronym` كل القراءات المرشحة لكل حرف, ويختار قاموس العبارات القراءات الشائعة تلقائيا.
- تقسيم كلمات Jieba: يفعل خيار `segment` تقسيم الكلمات لإزالة لبس القراءات المتعددة حسب العبارة, فيرفع دقة التدوين الصوتي للجمل الكاملة.
- ستة أنماط بينيين: علامات النغمة, والنغمة الرقمية, والرقم بعد النهائية مباشرة, وبلا نغمة, والبادئات فقط, والحرف الأول فقط, لتغطية سيناريوهات الفرز والبحث والتدوين.
- أوضاع الأسماء الخاصة: يفضل `SURNAME` قراءات الألقاب, بينما يطبق `PLACE_NAME` أولا مجموعة منتقاة من أسماء الأماكن ذات مصادر قابلة للتتبع ثم يعود إلى التحويل العادي.
- نتائج قابلة للتركيب: تحمل المصفوفة ثنائية الأبعاد التي يعيدها `convert` طريقة `compact()` تفرد كل توليفات القراءات بخطوة واحدة.
- متعدد اللغات: بيانات المكون الإضافي, والتعليمات, و README, وسجل التغييرات متوفرة بعشر لغات.

******

### الاستخدام

******

1. قم بترقية AutoJs6 إلى البنية الداخلية 3923 (6.7.1 Alpha4) أو أعلى; فمنذ v6.8.0 تتولى المكونات الإضافية قدرة بينيين بالكامل, وينصح باستخدام أحدث إصدار مباشرة.
2. نزل حزمة APK للمكون من صفحة [Releases](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/releases) وثبتها على الجهاز الذي يشغل AutoJs6, أو ثبتها مباشرة عبر الإنترنت من مركز المكونات الإضافية في AutoJs6.
3. افتح مركز المكونات الإضافية في AutoJs6 وتأكد من أن مكون `Pinyin` معروف وممنوح الإذن ومفعل.
4. استدع الكائن العام `pinyin` مباشرة في البرامج النصية مسترشدا بأمثلة `البداية السريعة` أدناه; ويمكنك أولا تشغيل `الفحص الذاتي` للتأكد من عمل المكون.

> يوفر المكون الإضافي حزمة تثبيت عامة واحدة فقط (تنفيذ JVM خالص لا يفرق بين معماريات CPU), ويدعم الأجهزة العاملة بنظام Android 7.0 (واجهة API 24) وما فوق. لا يملك المكون واجهة مستقلة ولا ينشئ أيقونة على الشاشة الرئيسية بعد التثبيت, ويتولى AutoJs6 اكتشافه وإدارته بشكل موحد.

******

### البداية السريعة

******

التحويل الأساسي: يعيد `convert` مصفوفة مرشحات ثنائية الأبعاد, ويعيد `simple` سلسلة مدمجة:

```javascript
console.log(pinyin.convert("中心"));                     // [["zhōng"], ["xīn"]]
console.log(pinyin.convert("中心", { style: "TONE2" })); // [["zhong1"], ["xin1"]]
console.log(pinyin.simple("拼音插件"));                  // "pinyinchajian"
console.log(pinyin.simple("拼音插件", true));            // "pin1yin1cha1jian4"
```

تعدد القراءات: يعيد خيار `heteronym` كل القراءات المرشحة, وتفرد `compact()` توليفات القراءات:

```javascript
let result = pinyin.convert("重庆", { heteronym: true });
console.log(result);
console.log(result.compact());
```

إزالة اللبس بتقسيم الكلمات ووضع الألقاب ووضع أسماء الأماكن:

```javascript
console.log(pinyin.simple("音乐重要", false, true));
console.log(pinyin.convert("单田芳", { mode: "SURNAME" }));
console.log(pinyin.convert("六安", { mode: "PLACE_NAME" })); // [["lù"], ["ān"]]
console.log(pinyin.convert("六安", {
  customDictionary: { "六安": [["liú"], ["ān"]] },
})); // [["liú"], ["ān"]]
```

******

### أنماط بينيين

******

يتحكم خيار `style` في نمط إخراج بينيين, والمثال هنا للحرف "中" (zhōng):

| النمط | الإخراج | الوصف |
|---|---|---|
| `TONE` | `zhōng` | علامة النغمة فوق النهائية (الافتراضي) |
| `TONE2` | `zhong1` | النغمة رقما 0-4 في نهاية المقطع |
| `TO3NE` | `zho1ng` | رقم النغمة بعد النهائية مباشرة |
| `NORMAL` | `zhong` | بلا نغمة |
| `INITIALS` | `zh` | إرجاع البادئة فقط (سلسلة فارغة للمقاطع بلا بادئة) |
| `FIRST_LETTER` | `z` | إرجاع الحرف الأول من المقطع فقط |

قيمة `style` غير حساسة لحالة الأحرف, ويمكن تمريرها كسلسلة (مثل `"TONE2"`) أو كثابت (مثل `pinyin.STYLE_TONE2`).

******

### الخيارات

******

تدعم `pinyin.convert(text, options)` الخيارات التالية:

| الخيار | الافتراضي | الوصف |
|---|---|---|
| `style` | `TONE` | نمط بينيين, انظر `أنماط بينيين` أعلاه |
| `mode` | `NORMAL` | وضع التحويل: `NORMAL` للنص العادي, و `SURNAME` لقراءات الألقاب, و `PLACE_NAME` لقراءات أسماء الأماكن المنتقاة |
| `segment` | `false` | تفعيل تقسيم كلمات Jieba والاستعانة بقاموس العبارات لإزالة لبس القراءات |
| `heteronym` | `false` | إرجاع كل القراءات المرشحة لكل حرف بدل الأولى فقط |
| `group` | `false` | دمج مرشحات بينيين حسب الكلمات المقسمة (يستخدم مع `segment`) |
| `customDictionary` | `{}` | تجاوزات لقراءات حروف هان في هذا الاستدعاء فقط بالصيغة `{ العبارة: [[مرشحات مضبوطة النغمات], ...] }`; تفوز أطول مطابقة ولا تحفظ البيانات, ويلزم مضيف AutoJs6 ومكون إضافي متوافقان |

تقبل الأوضاع الثوابت أيضا (مثل `pinyin.MODE_PLACE_NAME`). يستخدم `PLACE_NAME` أطول تطابق في مجموعة صغيرة مراجعة يدويا, ويعود النص غير المدرج إلى `NORMAL`. هذه ليست قائمة وطنية شاملة; راجع [المجموعة ومصادرها](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/docs/dictionaries/place-names.md).

******

### واجهة برمجة النصوص

******

يوفر الكائن العام `pinyin` الطرق التالية (استدعاء `pinyin(text, options)` مباشرة يكافئ `pinyin.convert`):

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

- تعيد `convert` مصفوفة ثنائية الأبعاد: يشغل كل حرف صيني أو موضع حرف في عبارة صفا واحدا يضم قراءاته المرشحة; وتشغل الأحرف غير المدرجة وغير الصينية صفا كما هي. وتحمل المصفوفة المعادة طريقة `compact()` تفرد كل توليفات القراءات.
- تعيد `simple` سلسلة مدمجة: تؤخذ القراءة الأولى لكل حرف وتوصل مباشرة; مرر `true` كمعامل ثان للنغمات الرقمية (نمط TONE2, وإلا فبلا نغمة), و `true` كمعامل ثالث لتفعيل تقسيم الكلمات.
- تستعلم `fromCodePoint` عن سجل القراءة الأصلي لنقطة رمز مفردة في القاموس (مرشحات بالنغمات مفصولة بفواصل), وتعيد `null` إذا لم تكن مدرجة.
- تستعلم `fromPhrase` عن قاموس العبارات وتعيد القراءات المرشحة لكل موضع حرف في العبارة; وتعيد مصفوفة فارغة إذا لم تكن مدرجة.
- تعيد كل الطرق نتائجها بشكل متزامن; ويحتاج أول استدعاء إلى تهيئة القواميس المضمنة فقد يتأخر قليلا.

#### Node.js

في بيئة Node.js استدع المزود نفسه عبر واجهة `autojs6:bridge` العامة وصرح صراحة بقدرة `pinyin`:

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

### الفحص الذاتي

******

بعد تثبيت المكون وتفعيله, شغل هذا البرنامج النصي المكون من سطر واحد:

```javascript
console.log(pinyin.simple("拼音"));
```

ظهور `pinyin` في الإخراج يعني أن المكون يعمل بشكل سليم.

******

### الأسئلة الشائعة

******

#### كيف أتأكد من أن المكون الإضافي يعمل?

افتح مركز المكونات الإضافية في AutoJs6; رؤية مكون `Pinyin` مفعلا هناك تعني أن المضيف تعرف عليه. ثم شغل برنامج `الفحص الذاتي` النصي أعلاه; وظهور `pinyin` في الإخراج يعني أنه يعمل.

#### يبلغ البرنامج النصي عن مكون مفقود أو أن `pinyin` غير متاح?

تأكد من أن البنية الداخلية لـ AutoJs6 ليست أدنى من 3923, وأن المكون ثبت ومنح الإذن وفعل في مركز المكونات الإضافية. فمنذ AutoJs6 v6.8.0 لم يعد المضيف يضمن تنفيذا لبينيين, وصارت قدرة بينيين بالكامل على عاتق هذا المكون.

#### لماذا لا توجد أيقونة للمكون في قائمة التطبيقات أو الشاشة الرئيسية?

هذا متوقع. لا يملك المكون واجهة مستقلة ولا ينشئ أيقونة تشغيل على الشاشة الرئيسية; وبعد التثبيت يكتشفه AutoJs6 ويستدعيه في الخلفية, ويجري كل تفاعل داخل AutoJs6.

#### قراءة حرف متعدد القراءات لا تطابق المتوقع?

يجري التحويل افتراضيا بالقراءة الأولى للحرف المفرد. ينصح بتفعيل خيار `segment` للاستعانة بقاموس العبارات وتقسيم الكلمات لإزالة اللبس (مثل `pinyin.simple(text, false, true)`); وعند الحاجة إلى كل المرشحات استخدم خيار `heteronym`. وإذا بقيت قراءة كلمة شائعة غير صحيحة, فنرحب بالإبلاغ عبر [Issues](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/issues) لتحسين القواميس.

#### كيف أختار بين هذا المكون وشقيقه Pinyin4j?

اختر هذا المكون عند الحاجة إلى تعدد القراءات أو تقسيم الكلمات أو العبارات أو قراءات الألقاب; واختر [Pinyin4j](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin4j) إذا كنت تحتاج فقط تحويلا خفيفا حرفا بحرف وتهتم بحجم الحزمة. لا يتعارض المكونان ويمكن تثبيتهما معا, وانظر `مقارنة المكونين الشقيقين` أدناه.

#### هل يتصل المكون الإضافي بالشبكة أو يطلب أذونات حساسة?

لا. كل القواميس مضمنة في حزمة التثبيت ويجري التحويل محليا على الجهاز; ولا يعلن بيان المكون إلا إذن المكون الإضافي اللازم للتواصل مع AutoJs6, دون أي أذونات نظام حساسة كالشبكة أو التخزين.

#### لماذا يبلغ حجم حزمة التثبيت نحو 6 MB?

تضم الحزمة أربع مجموعات بيانات: قاموس الأحرف المفردة, وقاموس العبارات, ومعجم تقسيم الكلمات, ونموذج HMM, مقابل عمل كامل دون اتصال ودقة أعلى في التدوين الصوتي. وإن كان الحجم أهم لديك, ففكر في المكون الشقيق [Pinyin4j](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin4j) البالغ نحو 0.3 MB.

#### لماذا يرفض `customDictionary` أو استدعاء Pinyin من Node.js?

تتطلب هذه المسارات إصدارين متوافقين من AutoJs6 ومكون Pinyin الإضافي. ويجب أن تعلن استدعاءات Node.js عن `permissions: ["pinyin"]`. يقتصر القاموس المخصص على استدعاء واحد ويلتزم بالحدود الموثقة لعدد الإدخالات والمرشحات والتوليفات و 64 KiB.

******

### الأذونات والأمان

******

صمم المكون الإضافي بحيث يضيق سطح البيانات وسطح الأذونات قدر الإمكان:

- أذونات دنيا: لا يعلن بيان المكون إلا إذن مكون AutoJs6 الإضافي (`org.autojs.permission.PLUGIN`), دون أي أذونات نظام حساسة كالشبكة أو التخزين أو الكاميرا.
- تحويل محلي: ينتقل النص المراد تحويله عبر Binder داخل الجهاز فقط, والقواميس كلها مضمنة, والعملية بأكملها دون اتصال, فلا تغادر البيانات الجهاز.
- التوقيع والتفويض: يتحقق AutoJs6 من توقيع المكون, ولا يمكن للبرامج النصية استدعاء المكون إلا بعد منحه الإذن وتفعيله في مركز المكونات الإضافية; والخدمة ونقطة الإيقاظ محميتان بإذن المكون الإضافي, فلا تستطيع تطبيقات الجهات الخارجية استدعاءهما مباشرة.
- مفتوح وقابل للتدقيق: كود المكون وتغليف القواميس وخط إنتاج الوثائق كلها مفتوحة المصدر.

ثبت حزمة المكون الإضافي فقط من صفحة [Releases](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/releases) الرسمية أو من مركز المكونات الإضافية في AutoJs6; فقد تكون الحزم مجهولة المصدر معدلة حتى لو تطابق الاسم ورقم الإصدار.

******

### مقارنة المكونين الشقيقين

******

يوفر AutoJs6 رسميا مكوني بينيين إضافيين لكل منهما تركيزه, ويمكن تثبيتهما معا:

| وجه المقارنة | [Pinyin](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin) | [Pinyin4j](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin4j) |
|---|---|---|
| التنفيذ الأساسي | قواميس مضمنة + تقسيم كلمات Jieba | مكتبة Java الكلاسيكية `pinyin4j` |
| الكائن العام | `pinyin` | `pinyin4j` |
| تعدد القراءات | مدعوم, مع إمكانية إرجاع كل المرشحات | غير مدعوم, القراءة الأولى دائما |
| تقسيم الكلمات والعبارات | مدعوم (قاموس العبارات + Jieba) | غير مدعوم, تحويل حرفا بحرف |
| وضع الألقاب | مدعوم | غير مدعوم |
| شكل الإخراج | مصفوفة مرشحات ثنائية الأبعاد (قابلة للتركيب عبر `compact()`) أو سلسلة مدمجة | سلسلة بفاصل قابل للضبط |
| الأنماط والتنسيقات | 6 أنماط بينيين | 3 تنسيقات نغمة + حالة الأحرف + تمثيل `ü` |
| حجم الحزمة | نحو 6 MB (قواميس مضمنة) | نحو 0.3 MB |
| الأنسب لـ | أولوية دقة اللفظ: تعدد القراءات والعبارات وأسماء الأشخاص | أولوية الحجم والبساطة: تحويل سريع حرفا بحرف |

لا يعتمد المكونان أحدهما على الآخر ولا يتعارضان; وبعد تثبيتهما معا يمكن للبرامج النصية استدعاء `pinyin` و `pinyin4j` كل حسب الحاجة. ولتفاصيل مكون Pinyin4j انظر [AutoJs6-Plugin-Pinyin4j](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin4j).

******

### واجهة المكون الإضافي

******

المعلومات التالية موجهة لمطوري مضيف AutoJs6 والمكونات الإضافية; يستخدم المضيف هذه المعرفات لاكتشاف المكون والتفاوض على القدرات:

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

تستجيب `PinyinPluginService` لـ action باسم `org.autojs.plugin.PINYIN` (والفئة category هي `pinyin`), وتكشف 5 طرق عبر واجهة AIDL باسم `IPinyinPlugin`; تعيد `convert` و `fromPhrase` مصفوفات ثنائية الأبعاد كسلاسل JSON, وتمرر الخيارات عبر `Bundle` (المفاتيح: `mode` / `style` / `segment` / `heteronym` / `group` / `custom_dictionary_json`). تتطلب القواميس المخصصة capability باسم `pinyin.customDictionary.v1`. الخدمة و `WakeActivity` كلتاهما محميتان بإذن `org.autojs.permission.PLUGIN`, فلا تستطيع تطبيقات الجهات الخارجية استدعاءهما مباشرة.

******

### خارطة الطريق

******

تدار قدرات المكون المخطط لها وحالة إنجازها كقائمة قابلة للتأشير في ROADMAP.md, منظمة حسب مراحل رئيسية مع معايير قبول, وتغطي وضع أسماء الأماكن, وتطور القواميس, والقواميس المخصصة, وتحسين الأداء, والتكامل المستمر. البنود غير المؤشرة نوايا مخطط لها وليست قدرات الإصدار الحالي; والنقاش عبر Issues موضع ترحيب.

- [عرض ROADMAP.md](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/ROADMAP.md)

******

### سجل الإصدارات

******

#### v1.0.1

_2026/09/11_

- `تلميح` يحسن هذا الإصدار الوثائق والأدوات المصاحبة فقط; ويبقى سلوك تحويل بينيين وكل واجهات البرمجة النصية دون تغيير
- `تحسين` أعيدت هيكلة README بعشر لغات: أضيفت فصول الاستخدام, والبداية السريعة, وجداول مرجعية لأنماط بينيين والخيارات, وواجهة برمجة النصوص, والفحص الذاتي, والأسئلة الشائعة, والأذونات والأمان, ومقارنة المكونين الشقيقين, وواجهة المكون الإضافي
- `تحسين` رقي مولد الوثائق إلى التنفيذ الموحد المشترك بين المكونات الشقيقة: كشف الانحراف عبر `--check`, والتحقق من تطابق المفاتيح والأشكال بين اللغات, وصد الرموز كاملة العرض, والتحقق من تطابق الإصدارات
- `تحسين` أدرجت تعليمات مركز المكونات الإضافية (`plugin_instruction.md`) في خط إنتاج JSON متعدد اللغات نفسه, بما يزيل صيانة المصدر المزدوج
- `تحسين` أضيفت خارطة الطريق ROADMAP.md وأنشئت روابط متبادلة ومقارنة اختيار مع المكون الشقيق Pinyin4j
- `تحسين` توحيد تخطيط README وطريقة إدارة إصدارات منصة Gradle
- `تحسين` التحقق أثناء البناء لمنع إدخال تبعيات أصلية غير مقصودة, مع تقرير JSON

#### v1.0.0

_2026/07/15_

- `ميزة` خدمة مكون Pinyin الإضافي: معرف المكون هو `pinyin`, ويكتشفه AutoJs6 ويستدعيه تلقائيا عبر `org.autojs.plugin.PINYIN`
- `ميزة` واجهة تحويل بينيين: تعيد `pinyin.convert(text, options)` مصفوفة مرشحات ثنائية الأبعاد مع طريقة التركيب `compact()`, وتعيد `pinyin.simple(text)` سلسلة مدمجة
- `ميزة` واجهة استعلام القواميس: تستعلم `pinyin.fromCodePoint(codePoint)` عن سجل قراءة الحرف المفرد, وتستعلم `pinyin.fromPhrase(phrase)` عن قراءات العبارة
- `ميزة` ستة أنماط بينيين (`NORMAL` / `TONE` / `TONE2` / `TO3NE` / `INITIALS` / `FIRST_LETTER`) مع وضع الألقاب (`SURNAME`)
- `ميزة` دعم تعدد القراءات وتقسيم الكلمات: قواميس مضمنة للأحرف المفردة والعبارات وتقسيم الكلمات مع نموذج HMM, وتفعل خيارات `segment` / `heteronym` / `group` حسب الحاجة
- `ميزة` موارد متعددة اللغات: بيانات المكون الإضافي والتعليمات تغطي 10 لغات
- `ميزة` ينشأ README و CHANGELOG كملفات Markdown متعددة اللغات من مصادر JSON عبر `.python/generate_markdown.py`

##### لمزيد من سجل الإصدارات

* [CHANGELOG.md](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/app/src/main/assets/doc/CHANGELOG-ar.md)

******

### البناء

******

هذا القسم موجه للمطورين الراغبين في بناء المكون من المصدر.

بناء حزمة APK بوضع debug:

```powershell
.\gradlew.bat :app:assembleDebug
```

تشغيل اختبارات JVM الوحدوية وبناء ملف APK لاختبارات instrumentation:

```powershell
.\gradlew.bat :app:testDebugUnitTest :app:assembleDebugAndroidTest
```

بناء حزمة APK بوضع release (حزمة عامة واحدة; اضبط التوقيع في ملف `sign.properties` غير المتتبع ليجري التوقيع تلقائيا):

```powershell
.\gradlew.bat :app:assembleRelease
```

بناء ملف APK العام الموقع والتحقق منه بأمر واحد, ثم إنشاء `SHA256SUMS.txt` و`RELEASE_NOTES.md` من CHANGELOG الإنجليزي:

```powershell
py scripts\release\prepare_release.py
```

التحقق من تزامن مصادر الوثائق متعددة اللغات مع النواتج المولدة (يفرضه CI أيضا):

```powershell
py .python\generate_markdown.py --check
```

معاملات البناء مجمعة في `version.properties`: الحد الأدنى من SDK هو 24 (Android 7.0), و SDK الهدف 36, والإصدار الحالي 1.0.1.

******

### الترجمة وإنشاء الوثائق

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

يوفر `strings.xml` وصف المكون الإضافي المترجم, ويوفر `plugin_instruction.md` تعليمات الاستخدام المعروضة في مركز المكونات الإضافية بالمضيف. ينشأ README وسجل التغييرات والتعليمات كلها من مصادر JSON: عدل المصادر تحت `.readme/` و `.changelog/`, ثم شغل `py .python/generate_markdown.py` لإعادة إنشاء كل المخرجات, ولا تحرر المخرجات المولدة يدويا; وشغل `py .python/generate_markdown.py --check` للتحقق من تزامن المصادر والمخرجات.

******

### الترخيص

******

كود المشروع مرخص بموجب [Mozilla Public License 2.0](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/LICENSE). ونقل تنفيذ تقسيم الكلمات المضمن من مشروع [jieba-analysis](https://github.com/huaban/jieba-analysis), وصمم API بما يتوافق مع مكتبة [pinyin](https://github.com/hotoo/pinyin).

******

### روابط

******

- وثائق AutoJs6 Pinyin: https://docs.autojs6.com/#/pinyin
- مشروع AutoJs6: https://github.com/SuperMonster003/AutoJs6
- المكون الشقيق Pinyin4j: https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin4j
- مكتبة pinyin (مرجع تصميم API): https://github.com/hotoo/pinyin
- مشروع jieba-analysis: https://github.com/huaban/jieba-analysis


[16 KB page alignment and build verification](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/docs/16kb.md)
