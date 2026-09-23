# 🚀 UNSW-NB15 Cybersecurity Analytics Platform

> **منصة تحليل الأمن السيبراني باستخدام تقنيات Big Data**

---

## 🎯 الملخص التنفيذي

يهدف هذا المشروع إلى بناء **منصة متكاملة لتحليل بيانات الأمن السيبراني** باستخدام تقنيات **Big Data**، بدءاً من استيعاب البيانات الخام (Raw Data Ingestion)، مروراً بعمليات النقل والمعالجة والتنظيف والتحليل، وانتهاءً بتخزين البيانات وعرض النتائج من خلال **Interactive Dashboard**.

يعتمد المشروع على مجموعة بيانات **UNSW-NB15**، وهي مجموعة بيانات أكاديمية معيارية تُستخدم في أبحاث وتحليلات الأمن السيبراني، وتحتوي على أكثر من **2.54 مليون سجل لحركة الشبكة** (2,540,047 سجل بعد المعالجة) مصنفة إلى **Normal Traffic** و **Attack Traffic**، مع تصنيف الهجمات إلى **9 فئات رئيسية**.

تم تصميم المشروع لتطبيق مفهوم **End-to-End Big Data Pipeline** باستخدام **Apache NiFi** لاستيعاب البيانات، و **Apache Kafka** لنقل البيانات، و **Apache Spark** للمعالجة والتحليل، و **PostgreSQL** لتخزين البيانات المعالجة، و **Power BI** لإنشاء لوحات معلومات تفاعلية.

---

## 👤 معلومات المشروع

<table dir="rtl" width="100%">
  <thead>
    <tr>
      <th>العنصر</th>
      <th>التفاصيل</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>اسم الطالب</td><td>يوسف مختار أنعم الجرادي</td></tr>
    <tr><td>اسم المشروع</td><td>UNSW-NB15 Cybersecurity Analytics Platform</td></tr>
    <tr><td>نوع المشروع</td><td>مشروع شخصي (Self-Directed Project)</td></tr>
    <tr><td>المجال</td><td>Big Data + Cybersecurity</td></tr>
    <tr><td>اللغة</td><td>Arabic + English Technical Terms</td></tr>
    <tr><td>السنة</td><td>2026</td></tr>
  </tbody>
</table>

---

## 🎯 أهداف المشروع

### 1. الأهداف التقنية

- بناء **End-to-End Data Pipeline** لمعالجة بيانات الأمن السيبراني.
- تطبيق تقنيات **Big Data**: Apache NiFi، Apache Kafka، Apache Spark.
- تنفيذ عمليات **Data Ingestion** و **Batch Processing** و **Data Transformation**.
- تخزين البيانات المعالجة في **PostgreSQL**.
- إنشاء **Interactive Dashboard** لعرض النتائج.
- استخدام **Docker** لإنشاء بيئة موحدة قابلة لإعادة الإنتاج.

### 2. الأهداف التحليلية

- تنظيف وتجهيز بيانات حركة الشبكة (Data Cleaning).
- إجراء **Exploratory Data Analysis (EDA)** باستخدام Apache Spark.
- تحليل توزيع حركة الشبكة والهجمات.
- دراسة البروتوكولات والخدمات المرتبطة.
- مقارنة **Normal Traffic** مع **Attack Traffic**.
- استخراج **Actionable Insights** من البيانات.

### 3. الأهداف الأكاديمية

- تطبيق مفاهيم **Big Data** في مشروع عملي متكامل.
- استخدام أدوات مستخدمة في بيئات **Data Engineering**.
- بناء بيئة قابلة لإعادة الإنتاج باستخدام **Docker**.
- توثيق مراحل المشروع بطريقة احترافية.
- نشر المشروع على **GitHub** كجزء من **Technical Portfolio**.

---

## 🛠️ التقنيات المستخدمة

<table dir="rtl" width="100%">
  <thead>
    <tr>
      <th>المرحلة</th>
      <th>التقنية</th>
      <th>الإصدار</th>
      <th>الوظيفة</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>Data Ingestion</td><td>Apache NiFi</td><td>2.10.0</td><td>استيعاب البيانات والمعالجة الأولية</td></tr>
    <tr><td>Data Streaming</td><td>Apache Kafka</td><td>2.8.1</td><td>نقل البيانات عبر نظام Streaming موزع</td></tr>
    <tr><td>Data Processing</td><td>Apache Spark</td><td>3.1.2</td><td>معالجة وتنظيف وتحليل البيانات</td></tr>
    <tr><td>Data Storage</td><td>PostgreSQL</td><td>13</td><td>تخزين البيانات المعالجة</td></tr>
    <tr><td>Data Visualization</td><td>Power BI Desktop</td><td>2.157.1354.0</td><td>إنشاء Interactive Dashboards</td></tr>
    <tr><td>Containerization</td><td>Docker Desktop</td><td>28.3.2</td><td>بيئة تشغيل موحدة</td></tr>
    <tr><td>Programming</td><td>Python</td><td>3.6</td><td>PySpark وتحليل البيانات</td></tr>
  </tbody>
</table>

---

## 📊 البيانات المستخدمة

<table dir="rtl" width="100%">
  <thead>
    <tr>
      <th>العنصر</th>
      <th>القيمة</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>Dataset</td><td>UNSW-NB15</td></tr>
    <tr><td>المصدر</td><td>UNSW Canberra, Australia</td></tr>
    <tr><td>الحجم</td><td>~642 MB</td></tr>
    <tr><td>عدد الملفات</td><td>7 CSV Files (4 أساسية + 3 مساعدة)</td></tr>
    <tr><td>عدد السجلات</td><td>2,540,047 سجل (بعد المعالجة)</td></tr>
    <tr><td>عدد الأعمدة</td><td>49 Features (48 Features + Label)</td></tr>
    <tr><td>الفترة الزمنية</td><td>2015-01-21 → 2015-02-17</td></tr>
  </tbody>
</table>

### 📁 الملفات المستخدمة

<table dir="rtl" width="100%">
  <thead>
    <tr>
      <th>#</th>
      <th>الملف</th>
      <th>الحجم</th>
      <th>الوصف</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>1</td><td>UNSW-NB15_1.csv</td><td>~162 MB</td><td>الملف الأساسي الأول</td></tr>
    <tr><td>2</td><td>UNSW-NB15_2.csv</td><td>~158 MB</td><td>الملف الأساسي الثاني</td></tr>
    <tr><td>3</td><td>UNSW-NB15_3.csv</td><td>~148 MB</td><td>الملف الأساسي الثالث</td></tr>
    <tr><td>4</td><td>UNSW-NB15_4.csv</td><td>~94 MB</td><td>الملف الأساسي الرابع</td></tr>
    <tr><td>5</td><td>UNSW-NB15_GT.csv</td><td>~83 MB</td><td>Ground Truth Labels</td></tr>
    <tr><td>6</td><td>UNSW-NB15_features.csv</td><td>~4 KB</td><td>وصف الأعمدة الـ 49</td></tr>
    <tr><td>7</td><td>UNSW-NB15_LIST_EVENTS.csv</td><td>~4.6 KB</td><td>قائمة الأحداث</td></tr>
  </tbody>
</table>

### 🛡️ فئات الهجمات

<table dir="rtl" width="100%">
  <thead>
    <tr>
      <th>#</th>
      <th>الفئة</th>
      <th>الوصف</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>1</td><td>Generic</td><td>هجمات عامة</td></tr>
    <tr><td>2</td><td>Exploits</td><td>استغلال الثغرات</td></tr>
    <tr><td>3</td><td>Fuzzers</td><td>هجمات Fuzzing</td></tr>
    <tr><td>4</td><td>DoS</td><td>Denial of Service</td></tr>
    <tr><td>5</td><td>Reconnaissance</td><td>عمليات الاستطلاع</td></tr>
    <tr><td>6</td><td>Analysis</td><td>أنشطة التحليل</td></tr>
    <tr><td>7</td><td>Backdoors</td><td>هجمات Backdoors</td></tr>
    <tr><td>8</td><td>Shellcode</td><td>هجمات Shellcode</td></tr>
    <tr><td>9</td><td>Worms</td><td>هجمات الديدان</td></tr>
    <tr><td>—</td><td>Normal</td><td>حركة شبكة طبيعية</td></tr>
  </tbody>
</table>

---

## 🏗️ معمارية المشروع

يعتمد المشروع على **Distributed Data Ingestion and Batch Processing Pipeline**، حيث تمر البيانات عبر عدة مراحل مترابطة:

```text
UNSW-NB15 Dataset (642 MB / 7 Files)
              │
              ▼
      📂 RAW DATA (Source)
              │
              ▼
      🚚 Apache NiFi (Ingestion + SplitText)
              │
              ▼
      📨 Apache Kafka (Distributed Streaming)
              │
              ▼
      ⚡ Apache Spark (Processing + Cleaning + EDA)
              │
              ▼
      🐘 PostgreSQL (Storage)
              │
              ▼
      📊 Power BI (Interactive Dashboard)
```

<table dir="rtl" width="100%">
  <thead>
    <tr>
      <th>المرحلة</th>
      <th>المكون</th>
      <th>الدور</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>1</td><td>UNSW-NB15</td><td>مصدر البيانات الخام</td></tr>
    <tr><td>2</td><td>Apache NiFi</td><td>Data Ingestion + SplitText</td></tr>
    <tr><td>3</td><td>Apache Kafka</td><td>Distributed Data Streaming</td></tr>
    <tr><td>4</td><td>Apache Spark</td><td>Processing + Cleaning + EDA</td></tr>
    <tr><td>5</td><td>PostgreSQL</td><td>Storage</td></tr>
    <tr><td>6</td><td>Power BI</td><td>Visualization</td></tr>
  </tbody>
</table>

---

## ✅ ما تم إنجازه

<table dir="rtl" width="100%">
  <thead>
    <tr>
      <th>#</th>
      <th>المرحلة</th>
      <th>الحالة</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>1</td><td>Docker Environment Setup</td><td>✅</td></tr>
    <tr><td>2</td><td>NiFi Ingestion Flow</td><td>✅</td></tr>
    <tr><td>3</td><td>Kafka Streaming — 3 Brokers</td><td>✅</td></tr>
    <tr><td>4</td><td>Spark Processing — 2.54M Records</td><td>✅</td></tr>
    <tr><td>5</td><td>EDA — 14 Analyses in Spark</td><td>✅</td></tr>
    <tr><td>6</td><td>PostgreSQL Storage — 2.54M Records</td><td>✅</td></tr>
    <tr><td>7</td><td>Power BI Dashboard — 3 Pages</td><td>✅</td></tr>
    <tr><td>8</td><td>Documentation — 6 Files</td><td>✅</td></tr>
  </tbody>
</table>

---

## 📁 هيكل المشروع

```text
cybersecurity-bigdata-platform/
├── data/                # البيانات (Raw, Staging, Curated)
├── docs/                # التوثيق (6 ملفات)
├── kafka/               # Kafka Scripts
├── nifi/                # NiFi Templates + Schemas
├── postgres/            # SQL Scripts
├── spark/               # PySpark Notebooks
├── powerbi/             # Power BI Files + Screenshots
├── images/              # Architecture + Screenshots
├── README.md
├── .gitignore
└── requirements.txt
```

---

## 📌 متطلبات التشغيل

<table dir="rtl" width="100%">
  <thead>
    <tr>
      <th>المتطلب</th>
      <th>القيمة</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>Docker Desktop</td><td>مطلوب</td></tr>
    <tr><td>RAM</td><td>8 GB أو أكثر</td></tr>
    <tr><td>Storage</td><td>20 GB فارغة</td></tr>
    <tr><td>OS</td><td>Windows / macOS / Linux</td></tr>
    <tr><td>Python</td><td>3.6 (بيئة المشروع الحالية)</td></tr>
  </tbody>
</table>

### 📦 Dataset

نظراً لحجم البيانات، لا تُضمّن ملفات **UNSW-NB15** داخل المستودع.

**تحميل البيانات من المصدر الرسمي:**
🔗 https://research.unsw.edu.au/projects/unsw-nb15-dataset

---

## 📚 التوثيق

<table dir="rtl" width="100%">
  <thead>
    <tr>
      <th>#</th>
      <th>الملف</th>
      <th>الموضوع</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>1</td><td><b>00_overview.md</b></td><td>نظرة عامة (هذا الملف)</td></tr>
    <tr><td>2</td><td><b>01_architecture.md</b></td><td>المعمارية والبنية التقنية</td></tr>
    <tr><td>3</td><td><b>02_dataset.md</b></td><td>تفاصيل Dataset والـ 49 Features</td></tr>
    <tr><td>4</td><td><b>03_pipeline.md</b></td><td>مراحل Data Pipeline والتنفيذ</td></tr>
    <tr><td>5</td><td><b>04_results.md</b></td><td>النتائج والتحليلات والرؤى</td></tr>
    <tr><td>6</td><td><b>05_troubleshooting.md</b></td><td>المشاكل التي ظهرت والحلول</td></tr>
  </tbody>
</table>

---

## 🔗 المراجع

- **UNSW-NB15 Dataset** — [UNSW Canberra](https://research.unsw.edu.au/projects/unsw-nb15-dataset)
- **Apache NiFi Documentation** — [nifi.apache.org](https://nifi.apache.org/docs.html)
- **Apache Kafka Documentation** — [kafka.apache.org](https://kafka.apache.org/documentation/)
- **Apache Spark Documentation** — [spark.apache.org](https://spark.apache.org/docs/)
- **PostgreSQL Documentation** — [postgresql.org/docs](https://www.postgresql.org/docs/)
- **Power BI Documentation** — [learn.microsoft.com](https://learn.microsoft.com/en-us/power-bi/)

---

## 📞 التواصل

<table dir="rtl" width="100%">
  <thead>
    <tr>
      <th>القناة</th>
      <th>الرابط</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>GitHub</td><td><a href="https://github.com/Yousef-algaradi">@Yousef-algaradi</a></td></tr>
    <tr><td>Email</td><td>yosefalgradi690@gmail.com</td></tr>
    <tr><td>Location</td><td>Yemen</td></tr>
    <tr><td>Bio</td><td>Data Science Student | AI & Machine Learning Enthusiast</td></tr>
  </tbody>
</table>

---

## 📝 الرخصة

هذا المشروع مرخص تحت **MIT License** — للاستخدام الأكاديمي والتعليمي.

---

### 🛡️ UNSW-NB15 Cybersecurity Analytics Platform

**Big Data × Cybersecurity × Data Analytics**

**© 2026 — يوسف مختار أنعم الجرادي**