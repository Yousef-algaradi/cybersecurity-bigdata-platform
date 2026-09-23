# 🔧 المشاكل والحلول | Troubleshooting Guide

> **توثيق كامل للمشاكل التي واجهت المشروع وحلولها**

---

## 🎯 نظرة عامة

خلال بناء المشروع، واجهنا **17 مشكلة تقنية** في مراحل مختلفة (NiFi، Kafka، Spark، PostgreSQL، Power BI). هذا الملف يوثّق كل مشكلة مع **السبب الجذري** و**الحل الفعّال** الذي تم تطبيقه.

**القيمة العلمية:** توثيق هذه المشاكل يوفّر على أي شخص يبني مشروعاً مشابهاً عشرات الساعات من التجربة والخطأ.

---

## 📋 ملخص المشاكل (17 مشكلة)

<table dir="rtl" style="width: 100%; border-collapse: collapse; text-align: right;">
  <thead>
    <tr>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">#</th>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">المرحلة</th>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">المشكلة</th>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">الحالة</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">1</td><td style="padding: 8px; border: 1px solid #ddd;">NiFi</td><td style="padding: 8px; border: 1px solid #ddd;">OutOfMemoryError في SplitJson</td><td style="padding: 8px; border: 1px solid #ddd;">✅</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">2</td><td style="padding: 8px; border: 1px solid #ddd;">Kafka</td><td style="padding: 8px; border: 1px solid #ddd;">max.message.size exceeded</td><td style="padding: 8px; border: 1px solid #ddd;">✅</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">3</td><td style="padding: 8px; border: 1px solid #ddd;">Spark</td><td style="padding: 8px; border: 1px solid #ddd;">No such struct field 132</td><td style="padding: 8px; border: 1px solid #ddd;">✅</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">4</td><td style="padding: 8px; border: 1px solid #ddd;">Spark</td><td style="padding: 8px; border: 1px solid #ddd;">NameError: json_strings not defined</td><td style="padding: 8px; border: 1px solid #ddd;">✅</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">5</td><td style="padding: 8px; border: 1px solid #ddd;">Spark</td><td style="padding: 8px; border: 1px solid #ddd;">CSV does not support array&lt;string&gt;</td><td style="padding: 8px; border: 1px solid #ddd;">✅</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">6</td><td style="padding: 8px; border: 1px solid #ddd;">Docker</td><td style="padding: 8px; border: 1px solid #ddd;">ملفات Jupyter لا تظهر على Windows</td><td style="padding: 8px; border: 1px solid #ddd;">✅</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">7</td><td style="padding: 8px; border: 1px solid #ddd;">Jupyter</td><td style="padding: 8px; border: 1px solid #ddd;">IOPub data rate exceeded</td><td style="padding: 8px; border: 1px solid #ddd;">✅</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">8</td><td style="padding: 8px; border: 1px solid #ddd;">Jupyter</td><td style="padding: 8px; border: 1px solid #ddd;">No module named 'pandas'</td><td style="padding: 8px; border: 1px solid #ddd;">✅</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">9</td><td style="padding: 8px; border: 1px solid #ddd;">NiFi</td><td style="padding: 8px; border: 1px solid #ddd;">NumberFormatException: "-"</td><td style="padding: 8px; border: 1px solid #ddd;">✅</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">10</td><td style="padding: 8px; border: 1px solid #ddd;">NiFi</td><td style="padding: 8px; border: 1px solid #ddd;">NumberFormatException: "7850517.5"</td><td style="padding: 8px; border: 1px solid #ddd;">✅</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">11</td><td style="padding: 8px; border: 1px solid #ddd;">NiFi</td><td style="padding: 8px; border: 1px solid #ddd;">SchemaValidationException: sport cannot be null</td><td style="padding: 8px; border: 1px solid #ddd;">✅</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">12</td><td style="padding: 8px; border: 1px solid #ddd;">NiFi</td><td style="padding: 8px; border: 1px solid #ddd;">No resolvable bootstrap urls</td><td style="padding: 8px; border: 1px solid #ddd;">✅</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">13</td><td style="padding: 8px; border: 1px solid #ddd;">Spark</td><td style="padding: 8px; border: 1px solid #ddd;">AnalysisException: No such struct field srcip</td><td style="padding: 8px; border: 1px solid #ddd;">✅</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">14</td><td style="padding: 8px; border: 1px solid #ddd;">Spark</td><td style="padding: 8px; border: 1px solid #ddd;">Can't extract value from single_row</td><td style="padding: 8px; border: 1px solid #ddd;">✅</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">15</td><td style="padding: 8px; border: 1px solid #ddd;">Spark</td><td style="padding: 8px; border: 1px solid #ddd;">ازدواجية في البيانات (مثل "6055":"7832")</td><td style="padding: 8px; border: 1px solid #ddd;">✅</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">16</td><td style="padding: 8px; border: 1px solid #ddd;">Spark</td><td style="padding: 8px; border: 1px solid #ddd;">جميع الأعمدة null</td><td style="padding: 8px; border: 1px solid #ddd;">✅</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">17</td><td style="padding: 8px; border: 1px solid #ddd;">Power BI</td><td style="padding: 8px; border: 1px solid #ddd;">{None, None, None...} في Power BI</td><td style="padding: 8px; border: 1px solid #ddd;">✅</td></tr>
  </tbody>
</table>

---

## 🔴 المشاكل التفصيلية

### المشكلة 1: OutOfMemoryError في SplitJson

<table dir="rtl" style="width: 100%; border-collapse: collapse; text-align: right;">
  <thead>
    <tr>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">العنصر</th>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">التفاصيل</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">المرحلة</td><td style="padding: 8px; border: 1px solid #ddd;">NiFi</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">الخطأ</td><td style="padding: 8px; border: 1px solid #ddd;">java.lang.OutOfMemoryError: Java heap space</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">السبب</td><td style="padding: 8px; border: 1px solid #ddd;">SplitJson تسبب في استهلاك مرتفع للذاكرة أثناء معالجة الملف (162 MB)، مما أدى إلى Java heap space</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">الحل الناجح</td><td style="padding: 8px; border: 1px solid #ddd;">استخدام SplitText مع Line Split Count = 1000</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">ما فشل</td><td style="padding: 8px; border: 1px solid #ddd;">زيادة ذاكرة NiFi</td></tr>
  </tbody>
</table>

---

### المشكلة 2: max.message.size exceeded في Kafka

<table dir="rtl" style="width: 100%; border-collapse: collapse; text-align: right;">
  <thead>
    <tr>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">العنصر</th>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">التفاصيل</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">المرحلة</td><td style="padding: 8px; border: 1px solid #ddd;">Kafka</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">الخطأ</td><td style="padding: 8px; border: 1px solid #ddd;">max.message.size 1048576 exceeded (found 1819563)</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">السبب</td><td style="padding: 8px; border: 1px solid #ddd;">حجم الرسالة تجاوز القيمة المهيأة لـ max.message.size والتي كانت 1 MB في بيئة المشروع</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">الحل الناجح</td><td style="padding: 8px; border: 1px solid #ddd;">زيادة Max Request Size في NiFi + Kafka إلى 5 MB</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">ما فشل</td><td style="padding: 8px; border: 1px solid #ddd;">تقليل Line Split Count إلى 3000 و 1500</td></tr>
  </tbody>
</table>

---

### المشكلة 3: No such struct field 132 في Spark

<table dir="rtl" style="width: 100%; border-collapse: collapse; text-align: right;">
  <thead>
    <tr>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">العنصر</th>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">التفاصيل</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">المرحلة</td><td style="padding: 8px; border: 1px solid #ddd;">Spark</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">الخطأ</td><td style="padding: 8px; border: 1px solid #ddd;">AnalysisException: No such struct field 132</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">السبب</td><td style="padding: 8px; border: 1px solid #ddd;">البيانات في Kafka تحتوي على Header فقط</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">الحل الناجح</td><td style="padding: 8px; border: 1px solid #ddd;">تصفية Header + إعادة تشغيل NiFi</td></tr>
  </tbody>
</table>

---

### المشكلة 4: NameError: json_strings not defined

<table dir="rtl" style="width: 100%; border-collapse: collapse; text-align: right;">
  <thead>
    <tr>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">العنصر</th>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">التفاصيل</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">المرحلة</td><td style="padding: 8px; border: 1px solid #ddd;">Jupyter / Spark</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">الخطأ</td><td style="padding: 8px; border: 1px solid #ddd;">NameError: name 'json_strings' is not defined</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">السبب</td><td style="padding: 8px; border: 1px solid #ddd;">إعادة تشغيل Kernel + عدم تنفيذ الخلايا بالترتيب</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">الحل الناجح</td><td style="padding: 8px; border: 1px solid #ddd;">Restart & Run All</td></tr>
  </tbody>
</table>

---

### المشكلة 5: CSV does not support array&lt;string&gt;

<table dir="rtl" style="width: 100%; border-collapse: collapse; text-align: right;">
  <thead>
    <tr>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">العنصر</th>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">التفاصيل</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">المرحلة</td><td style="padding: 8px; border: 1px solid #ddd;">Spark</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">الخطأ</td><td style="padding: 8px; border: 1px solid #ddd;">CSV data source does not support array&lt;string&gt;</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">السبب</td><td style="padding: 8px; border: 1px solid #ddd;">بعض الأعمدة من نوع Array</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">الحل الناجح</td><td style="padding: 8px; border: 1px solid #ddd;">استخدام concat_ws لتحويل Array إلى String</td></tr>
  </tbody>
</table>

---

### المشكلة 6: ملفات Jupyter لا تظهر على Windows

<table dir="rtl" style="width: 100%; border-collapse: collapse; text-align: right;">
  <thead>
    <tr>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">العنصر</th>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">التفاصيل</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">المرحلة</td><td style="padding: 8px; border: 1px solid #ddd;">Docker + Jupyter</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">الخطأ</td><td style="padding: 8px; border: 1px solid #ddd;">الملفات في /workspace لا تظهر على Windows</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">السبب</td><td style="padding: 8px; border: 1px solid #ddd;">الملفات التي ينتجها Spark داخل الحاوية لا تنعكس دائماً على Bind Mount الخاص بـ Windows</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">الحل الناجح</td><td style="padding: 8px; border: 1px solid #ddd;">استخدام toPandas() + to_csv() كطريقة بديلة لتصدير البيانات</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">ما فشل</td><td style="padding: 8px; border: 1px solid #ddd;">الحفظ في /workspace/data/</td></tr>
  </tbody>
</table>

---

### المشكلة 7: IOPub data rate exceeded

<table dir="rtl" style="width: 100%; border-collapse: collapse; text-align: right;">
  <thead>
    <tr>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">العنصر</th>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">التفاصيل</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">المرحلة</td><td style="padding: 8px; border: 1px solid #ddd;">Jupyter</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">الخطأ</td><td style="padding: 8px; border: 1px solid #ddd;">IOPub data rate exceeded</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">السبب</td><td style="padding: 8px; border: 1px solid #ddd;">عرض JSON كبير (> 1 MB/sec)</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">الحل الناجح</td><td style="padding: 8px; border: 1px solid #ddd;">استخدام truncate=True + limit(3)</td></tr>
  </tbody>
</table>

---

### المشكلة 8: No module named 'pandas'

<table dir="rtl" style="width: 100%; border-collapse: collapse; text-align: right;">
  <thead>
    <tr>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">العنصر</th>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">التفاصيل</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">المرحلة</td><td style="padding: 8px; border: 1px solid #ddd;">Jupyter</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">الخطأ</td><td style="padding: 8px; border: 1px solid #ddd;">ModuleNotFoundError: No module named 'pandas'</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">السبب</td><td style="padding: 8px; border: 1px solid #ddd;">مكتبة Pandas غير مثبتة في بيئة Spark</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">الحل الناجح</td><td style="padding: 8px; border: 1px solid #ddd;">pip install pandas</td></tr>
  </tbody>
</table>

---

### المشكلة 9: NumberFormatException: "-"

<table dir="rtl" style="width: 100%; border-collapse: collapse; text-align: right;">
  <thead>
    <tr>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">العنصر</th>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">التفاصيل</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">المرحلة</td><td style="padding: 8px; border: 1px solid #ddd;">NiFi</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">الخطأ</td><td style="padding: 8px; border: 1px solid #ddd;">NumberFormatException: For input string: "-"</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">السبب</td><td style="padding: 8px; border: 1px solid #ddd;">ملفات CSV تحتوي على "-" في أعمدة رقمية</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">الحل الناجح</td><td style="padding: 8px; border: 1px solid #ddd;">Null String = "-" في CSVReader</td></tr>
  </tbody>
</table>

---

### المشكلة 10: NumberFormatException: "7850517.5"

<table dir="rtl" style="width: 100%; border-collapse: collapse; text-align: right;">
  <thead>
    <tr>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">العنصر</th>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">التفاصيل</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">المرحلة</td><td style="padding: 8px; border: 1px solid #ddd;">NiFi</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">الخطأ</td><td style="padding: 8px; border: 1px solid #ddd;">NumberFormatException: For input string: "7850517.5"</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">السبب</td><td style="padding: 8px; border: 1px solid #ddd;">Infer Schema ظن أنها Integer وهي Double</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">الحل الناجح</td><td style="padding: 8px; border: 1px solid #ddd;">استخدام Schema يدوي</td></tr>
  </tbody>
</table>

---

### المشكلة 11: SchemaValidationException: sport cannot be null

<table dir="rtl" style="width: 100%; border-collapse: collapse; text-align: right;">
  <thead>
    <tr>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">العنصر</th>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">التفاصيل</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">المرحلة</td><td style="padding: 8px; border: 1px solid #ddd;">NiFi</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">الخطأ</td><td style="padding: 8px; border: 1px solid #ddd;">SchemaValidationException: Field sport cannot be null</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">السبب</td><td style="padding: 8px; border: 1px solid #ddd;">الـ Schema يمنع null</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">الحل الناجح</td><td style="padding: 8px; border: 1px solid #ddd;">تغيير "type": "string" إلى ["string", "null"]</td></tr>
  </tbody>
</table>

---

### المشكلة 12: No resolvable bootstrap urls

<table dir="rtl" style="width: 100%; border-collapse: collapse; text-align: right;">
  <thead>
    <tr>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">العنصر</th>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">التفاصيل</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">المرحلة</td><td style="padding: 8px; border: 1px solid #ddd;">NiFi</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">الخطأ</td><td style="padding: 8px; border: 1px solid #ddd;">No resolvable bootstrap urls given in bootstrap.servers</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">السبب</td><td style="padding: 8px; border: 1px solid #ddd;">NiFi لم يتمكن من حل/الوصول إلى عناوين bootstrap.servers المحددة (قد يكون السبب: DNS، اسم المضيف، الشبكة، أو إعدادات Kafka)</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">الحل الناجح</td><td style="padding: 8px; border: 1px solid #ddd;">التأكد من صحة bootstrap.servers + الشبكة + إعادة تشغيل الحاويات</td></tr>
  </tbody>
</table>

---

### المشكلة 13: No such struct field srcip

<table dir="rtl" style="width: 100%; border-collapse: collapse; text-align: right;">
  <thead>
    <tr>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">العنصر</th>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">التفاصيل</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">المرحلة</td><td style="padding: 8px; border: 1px solid #ddd;">Spark</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">الخطأ</td><td style="padding: 8px; border: 1px solid #ddd;">No such struct field srcip in Description, Name, No., Type</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">السبب</td><td style="padding: 8px; border: 1px solid #ddd;">بيانات قديمة في Kafka (features.csv)</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">الحل الناجح</td><td style="padding: 8px; border: 1px solid #ddd;">مسح Kafka Topic + إعادة إنشائه</td></tr>
  </tbody>
</table>

---

### المشكلة 14: Can't extract value from single_row

<table dir="rtl" style="width: 100%; border-collapse: collapse; text-align: right;">
  <thead>
    <tr>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">العنصر</th>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">التفاصيل</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">المرحلة</td><td style="padding: 8px; border: 1px solid #ddd;">Spark</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">الخطأ</td><td style="padding: 8px; border: 1px solid #ddd;">Can't extract value from single_row: need struct type but got string</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">السبب</td><td style="padding: 8px; border: 1px solid #ddd;">استخدام getItem على String</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">الحل الناجح</td><td style="padding: 8px; border: 1px solid #ddd;">استخدام split بدل getItem</td></tr>
  </tbody>
</table>

---

### المشكلة 15: ازدواجية في البيانات

<table dir="rtl" style="width: 100%; border-collapse: collapse; text-align: right;">
  <thead>
    <tr>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">العنصر</th>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">التفاصيل</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">المرحلة</td><td style="padding: 8px; border: 1px solid #ddd;">Spark</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">الخطأ</td><td style="padding: 8px; border: 1px solid #ddd;">ازدواجية في البيانات مثل "6055":"7832"</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">السبب</td><td style="padding: 8px; border: 1px solid #ddd;">كل رسالة تحتوي على سطرين</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">الحل الناجح</td><td style="padding: 8px; border: 1px solid #ddd;">استخدام explode(split(line, "\n"))</td></tr>
  </tbody>
</table>

---

### المشكلة 16: جميع الأعمدة null

<table dir="rtl" style="width: 100%; border-collapse: collapse; text-align: right;">
  <thead>
    <tr>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">العنصر</th>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">التفاصيل</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">المرحلة</td><td style="padding: 8px; border: 1px solid #ddd;">Spark</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">الخطأ</td><td style="padding: 8px; border: 1px solid #ddd;">جميع الأعمدة null بعد Schema</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">السبب</td><td style="padding: 8px; border: 1px solid #ddd;">مخطط موحّد (Schema) غير متطابق بين NiFi و Spark</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">الحل الناجح</td><td style="padding: 8px; border: 1px solid #ddd;">استخدام SplitText + مخطط موحّد</td></tr>
  </tbody>
</table>

---

### المشكلة 17: {None, None, None...} في Power BI

<table dir="rtl" style="width: 100%; border-collapse: collapse; text-align: right;">
  <thead>
    <tr>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">العنصر</th>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">التفاصيل</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">المرحلة</td><td style="padding: 8px; border: 1px solid #ddd;">Power BI</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">الخطأ</td><td style="padding: 8px; border: 1px solid #ddd;">ظهور {None, None, None...}</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">السبب</td><td style="padding: 8px; border: 1px solid #ddd;">استخدام Record Reader/Writer في NiFi أدى إلى تحويل البيانات بشكل غير متوافق مع ما يتوقعه Power BI من Content الخاص بالـ FlowFile</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">الحل الناجح</td><td style="padding: 8px; border: 1px solid #ddd;">إزالة Record Reader/Writer من PublishKafka + إرسال CSV كنص خام</td></tr>
  </tbody>
</table>

---

## 🧠 الدروس المستفادة

<table dir="rtl" style="width: 100%; border-collapse: collapse; text-align: right;">
  <thead>
    <tr>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">#</th>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">الدرس</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">1</td><td style="padding: 8px; border: 1px solid #ddd;">استخدام SplitText بدلاً من SplitJson لتجنب مشاكل الذاكرة.</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">2</td><td style="padding: 8px; border: 1px solid #ddd;">ضبط أحجام الرسائل أقل من حد Kafka المهيأ (5 MB).</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">3</td><td style="padding: 8px; border: 1px solid #ddd;">التحقق من البيانات في Kafka قبل معالجتها في Spark.</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">4</td><td style="padding: 8px; border: 1px solid #ddd;">الربط الصحيح للمجلدات (Mounts) بين Docker و Windows.</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">5</td><td style="padding: 8px; border: 1px solid #ddd;">استخدام toPandas() + to_csv() كطريقة بديلة لتصدير البيانات.</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">6</td><td style="padding: 8px; border: 1px solid #ddd;">تقليل كمية البيانات المعروضة في Jupyter (truncate + limit).</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">7</td><td style="padding: 8px; border: 1px solid #ddd;">تثبيت المكتبات المطلوبة (pandas, pyarrow) داخل الحاوية.</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">8</td><td style="padding: 8px; border: 1px solid #ddd;">استخدام مخطط موحّد (Schema) بين كل المراحل.</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">9</td><td style="padding: 8px; border: 1px solid #ddd;">إزالة Record Reader/Writer من PublishKafka لتفادي مشاكل Schema.</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">10</td><td style="padding: 8px; border: 1px solid #ddd;">مسح Kafka Topics قبل كل تجربة جديدة.</td></tr>
  </tbody>
</table>

---

## 🏁 الخلاصة

**تم استكمال تنفيذ المشروع بعد معالجة 17 مشكلة تقنية ظهرت خلال مراحل التطوير والاختبار.**

- ✅ NiFi للإدخال والتقسيم
- ✅ Kafka لمعالجة/نقل تدفقات البيانات (Streaming)
- ✅ Spark لتنظيف البيانات (Cleaning) والتحليل الاستكشافي للبيانات (EDA)
- ✅ PostgreSQL للتخزين
- ✅ Power BI للعرض

**النتيجة:** تمكنت المنصة من تنفيذ خط معالجة البيانات وتحليل **2,540,047 سجلاً** بنجاح ضمن بيئة الاختبار.

---

## 🔗 الملفات المرتبطة

<table dir="rtl" style="width: 100%; border-collapse: collapse; text-align: right;">
  <thead>
    <tr>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">#</th>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">الملف</th>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">الموضوع</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">1</td><td style="padding: 8px; border: 1px solid #ddd;"><b>00_overview.md</b></td><td style="padding: 8px; border: 1px solid #ddd;">نظرة عامة</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">2</td><td style="padding: 8px; border: 1px solid #ddd;"><b>01_architecture.md</b></td><td style="padding: 8px; border: 1px solid #ddd;">المعمارية</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">3</td><td style="padding: 8px; border: 1px solid #ddd;"><b>02_dataset.md</b></td><td style="padding: 8px; border: 1px solid #ddd;">البيانات</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">4</td><td style="padding: 8px; border: 1px solid #ddd;"><b>03_pipeline.md</b></td><td style="padding: 8px; border: 1px solid #ddd;">مراحل التنفيذ</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">5</td><td style="padding: 8px; border: 1px solid #ddd;"><b>04_results.md</b></td><td style="padding: 8px; border: 1px solid #ddd;">النتائج</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">6</td><td style="padding: 8px; border: 1px solid #ddd;"><b>05_troubleshooting.md</b></td><td style="padding: 8px; border: 1px solid #ddd;">المشاكل (هذا الملف)</td></tr>
  </tbody>
</table>

---

### 🛡️ UNSW-NB15 Cybersecurity Analytics Platform

**Big Data × Cybersecurity × Data Analytics**

**© 2026 — يوسف مختار أنعم الجرادي**