يوفر مكون Pinyin الإضافي (Pinyin Plugin) لـ AutoJs6 قدرة تحويل النص الصيني إلى بينيين دون اتصال. بعد التثبيت, يمكن للبرامج النصية عبر الكائن العام `pinyin` تحويل النص الصيني إلى بينيين بأنماط متعددة, مع دعم مرشحات الأحرف متعددة القراءات, وقاموس العبارات, وتقسيم الكلمات بواسطة Jieba, ووضع الألقاب, مما يناسب سيناريوهات الأتمتة مثل الفرز والبحث والفهرسة بالحرف الأول والتدوين الصوتي.

### البداية السريعة

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

### أنماط بينيين

يتحكم خيار `style` في نمط إخراج بينيين, والمثال هنا للحرف "中" (zhōng):

```text
TONE (zhōng)  TONE2 (zhong1)  TO3NE (zho1ng)
NORMAL (zhong)  INITIALS (zh)  FIRST_LETTER (z)
```

تشمل الخيارات المدعومة `style` (نمط بينيين), و `mode` (الوضع العادي/الألقاب/أسماء الأماكن), و `segment` (تقسيم الكلمات), و `heteronym` (تعدد القراءات), و `group` (الدمج حسب العبارات).

### الفحص الذاتي

بعد تثبيت المكون وتفعيله, شغل هذا البرنامج النصي المكون من سطر واحد:

```javascript
console.log(pinyin.simple("拼音"));
```

ظهور `pinyin` في الإخراج يعني أن المكون يعمل بشكل سليم.

لمزيد من تفاصيل الاستخدام والخيارات, راجع [وثائق AutoJs6 Pinyin](https://docs.autojs6.com/#/pinyin) و [صفحة المشروع](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin).
