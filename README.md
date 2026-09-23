# 🛡️ UNSW-NB15 Cybersecurity Analytics Platform

> **منصة تحليل الأمن السيبراني باستخدام تقنيات Big Data**

---

## 🎯 نظرة عامة

مشروع **End-to-End Big Data Pipeline** لتحليل بيانات الأمن السيبراني من مجموعة **UNSW-NB15** (المتاحة مسبقاً كملفات CSV ثابتة)، بدءاً من استيعاب البيانات الخام، مروراً بالمعالجة والتنظيف والتحليل، وانتهاءً بـ **Interactive Dashboard**.

يعتمد المشروع على **2,540,047 سجلاً** (بعد المعالجة والتنظيف) مصنفة إلى **Normal Traffic** و **Attack Traffic**، مع **9 فئات رئيسية** من الهجمات.

---

## 🔄 خط معالجة البيانات

```text
UNSW-NB15 Dataset (642 MB / 7 Files)
              │
              ▼
      📂 RAW DATA (Source)
              │
              ▼
      🚚 Apache NiFi (Ingestion)
              │
              ▼
      📨 Apache Kafka (Message Broker)
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

---

## 🛠️ التقنيات المستخدمة

<table dir="rtl" style="width: 100%; border-collapse: collapse; text-align: right;">
  <thead>
    <tr>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">المرحلة</th>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">التقنية</th>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">الإصدار</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">Data Ingestion</td><td style="padding: 8px; border: 1px solid #ddd;">Apache NiFi</td><td style="padding: 8px; border: 1px solid #ddd;">2.10.0</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">Message Broker</td><td style="padding: 8px; border: 1px solid #ddd;">Apache Kafka</td><td style="padding: 8px; border: 1px solid #ddd;">2.8.1</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">Data Processing</td><td style="padding: 8px; border: 1px solid #ddd;">Apache Spark</td><td style="padding: 8px; border: 1px solid #ddd;">3.1.2</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">Data Storage</td><td style="padding: 8px; border: 1px solid #ddd;">PostgreSQL</td><td style="padding: 8px; border: 1px solid #ddd;">13</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">Data Visualization</td><td style="padding: 8px; border: 1px solid #ddd;">Power BI Desktop</td><td style="padding: 8px; border: 1px solid #ddd;">2.157.1354.0</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">Containerization</td><td style="padding: 8px; border: 1px solid #ddd;">Docker Desktop</td><td style="padding: 8px; border: 1px solid #ddd;">28.3.2</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">Programming</td><td style="padding: 8px; border: 1px solid #ddd;">Python</td><td style="padding: 8px; border: 1px solid #ddd;">3.6 (بيئة المشروع)</td></tr>
  </tbody>
</table>

---

## 📊 البيانات المستخدمة

<table dir="rtl" style="width: 100%; border-collapse: collapse; text-align: right;">
  <thead>
    <tr>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">العنصر</th>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">القيمة</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">Dataset</td><td style="padding: 8px; border: 1px solid #ddd;">UNSW-NB15</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">الحجم</td><td style="padding: 8px; border: 1px solid #ddd;">~642 MB</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">عدد الملفات</td><td style="padding: 8px; border: 1px solid #ddd;">7 CSV Files (4 أساسية + 3 مساعدة)</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">عدد السجلات</td><td style="padding: 8px; border: 1px solid #ddd;">2,540,047 (بعد المعالجة والتنظيف)</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">عدد الأعمدة</td><td style="padding: 8px; border: 1px solid #ddd;">49 (48 features + 1 label)</td></tr>
  </tbody>
</table>

**تحميل البيانات:** [UNSW-NB15 Dataset — UNSW Canberra](https://research.unsw.edu.au/projects/unsw-nb15-dataset)

---

## 📁 هيكل المشروع

```text
cybersecurity-bigdata-platform/
├── data/                    # البيانات (Raw, Staging, Rejected, Curated)
├── docs/                    # التوثيق (6 ملفات)
│   ├── 00_overview.md
│   ├── 01_architecture.md
│   ├── 02_dataset.md
│   ├── 03_pipeline.md
│   ├── 04_results.md
│   └── 05_troubleshooting.md
├── kafka/                   # Kafka Scripts
├── nifi/                    # NiFi Templates + Schemas
├── postgres/                # SQL Scripts
├── spark/                   # PySpark Notebooks
├── powerbi/                 # Power BI Files + Screenshots
├── images/                  # Architecture + Screenshots
├── README.md
├── .gitignore
└── requirements.txt
```

---

## 🚀 التشغيل السريع

### 1. تشغيل البيئة

```bash
docker-compose up -d
docker ps
```

### 2. إنشاء Kafka Topic

```bash
bash kafka/create_topic.sh
```

### 3. الوصول للخدمات

> ⚠️ **ملاحظة أمنية:** جميع بيانات الدخول أدناه هي **قيم افتراضية لبيئة التطوير المحلية فقط**، ولا يجب استخدامها في بيئة إنتاجية.

<table dir="rtl" style="width: 100%; border-collapse: collapse; text-align: right;">
  <thead>
    <tr>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">الخدمة</th>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">الرابط</th>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">ملاحظة</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">NiFi</td><td style="padding: 8px; border: 1px solid #ddd;">https://localhost:7443</td><td style="padding: 8px; border: 1px solid #ddd;">بيانات الدخول في متغيرات البيئة</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">JupyterLab</td><td style="padding: 8px; border: 1px solid #ddd;">http://localhost:8888</td><td style="padding: 8px; border: 1px solid #ddd;">Spark Environment</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">Kafka UI</td><td style="padding: 8px; border: 1px solid #ddd;">http://localhost:8090</td><td style="padding: 8px; border: 1px solid #ddd;">Kafka Monitoring</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">PostgreSQL</td><td style="padding: 8px; border: 1px solid #ddd;">localhost:6432</td><td style="padding: 8px; border: 1px solid #ddd;">بيانات الدخول في متغيرات البيئة</td></tr>
  </tbody>
</table>

---

## 📚 التوثيق

<table dir="rtl" style="width: 100%; border-collapse: collapse; text-align: right;">
  <thead>
    <tr>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">#</th>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">الملف</th>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">الموضوع</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">1</td><td style="padding: 8px; border: 1px solid #ddd;"><a href="docs/00_overview.md">00_overview.md</a></td><td style="padding: 8px; border: 1px solid #ddd;">نظرة عامة</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">2</td><td style="padding: 8px; border: 1px solid #ddd;"><a href="docs/01_architecture.md">01_architecture.md</a></td><td style="padding: 8px; border: 1px solid #ddd;">المعمارية والبنية التقنية</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">3</td><td style="padding: 8px; border: 1px solid #ddd;"><a href="docs/02_dataset.md">02_dataset.md</a></td><td style="padding: 8px; border: 1px solid #ddd;">تفاصيل البيانات</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">4</td><td style="padding: 8px; border: 1px solid #ddd;"><a href="docs/03_pipeline.md">03_pipeline.md</a></td><td style="padding: 8px; border: 1px solid #ddd;">مراحل التنفيذ</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">5</td><td style="padding: 8px; border: 1px solid #ddd;"><a href="docs/04_results.md">04_results.md</a></td><td style="padding: 8px; border: 1px solid #ddd;">النتائج والرؤى</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">6</td><td style="padding: 8px; border: 1px solid #ddd;"><a href="docs/05_troubleshooting.md">05_troubleshooting.md</a></td><td style="padding: 8px; border: 1px solid #ddd;">المشاكل والحلول</td></tr>
  </tbody>
</table>

---

## 📈 أبرز النتائج

<table dir="rtl" style="width: 100%; border-collapse: collapse; text-align: right;">
  <thead>
    <tr>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">#</th>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">الرؤية</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">1</td><td style="padding: 8px; border: 1px solid #ddd;">من إجمالي السجلات: 87.35% Normal و 12.65% Attack</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">2</td><td style="padding: 8px; border: 1px solid #ddd;">من إجمالي الهجمات: فئة Generic تمثل 67%</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">3</td><td style="padding: 8px; border: 1px solid #ddd;">من إجمالي سجلات UDP: 22.6% هجمات (مقابل 3.9% في TCP)</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">4</td><td style="padding: 8px; border: 1px solid #ddd;">من إجمالي السجلات: TCP + UDP = 98%</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">5</td><td style="padding: 8px; border: 1px solid #ddd;">ذروة الهجمات عند الساعة 05:00 صباحاً (بتوقيت Dataset)</td></tr>
  </tbody>
</table>

---

## 📌 المتطلبات

<table dir="rtl" style="width: 100%; border-collapse: collapse; text-align: right;">
  <thead>
    <tr>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">المتطلب</th>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">الحد الأدنى</th>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">الموصى به</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">Docker Desktop</td><td style="padding: 8px; border: 1px solid #ddd;">28.3.2+</td><td style="padding: 8px; border: 1px solid #ddd;">أحدث إصدار</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">RAM</td><td style="padding: 8px; border: 1px solid #ddd;">8 GB</td><td style="padding: 8px; border: 1px solid #ddd;">16 GB</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">Storage</td><td style="padding: 8px; border: 1px solid #ddd;">20 GB</td><td style="padding: 8px; border: 1px solid #ddd;">40 GB</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">Power BI Desktop</td><td style="padding: 8px; border: 1px solid #ddd;">2.157+</td><td style="padding: 8px; border: 1px solid #ddd;">أحدث إصدار</td></tr>
  </tbody>
</table>

---

## 📞 التواصل

<table dir="rtl" style="width: 100%; border-collapse: collapse; text-align: right;">
  <thead>
    <tr>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">القناة</th>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">الرابط</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">GitHub</td><td style="padding: 8px; border: 1px solid #ddd;"><a href="https://github.com/Yousef-algaradi">@Yousef-algaradi</a></td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">Email</td><td style="padding: 8px; border: 1px solid #ddd;">yosefalgradi690@gmail.com</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">Location</td><td style="padding: 8px; border: 1px solid #ddd;">Yemen</td></tr>
  </tbody>
</table>

---

## 📝 الرخصة

هذا المشروع مرخص تحت **MIT License** — للاستخدام الأكاديمي والتعليمي.

---

### 🛡️ UNSW-NB15 Cybersecurity Analytics Platform

**Big Data × Cybersecurity × Data Analytics**

**© 2026 — يوسف مختار أنعم الجرادي**