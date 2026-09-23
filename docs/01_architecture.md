# 🏗️ معمارية المشروع | Project Architecture

> **البنية التقنية الكاملة لمنصة تحليل الأمن السيبراني**

---

## 🎯 نظرة عامة

يعتمد المشروع على معمارية **End-to-End Data Pipeline** تتكون من **6 مراحل مترابطة**، تبدأ من البيانات الخام (Raw Data) وتنتهي بـ Interactive Dashboard.

كل مرحلة تعتمد على تقنية متخصصة، وتمر البيانات بين المراحل بطريقة **موثقة وقابلة لإعادة الإنتاج**.

---

## 🏗️ المعمارية العامة

```text
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│              UNSW-NB15 Dataset (642 MB)                     │
│                   7 CSV Files                               │
│                                                             │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
        ┌────────────────────────────────┐
        │      📂 RAW DATA STORAGE       │
        │      /data/raw/                │
        │      (Source Files)            │
        └───────────────┬────────────────┘
                        │
                        ▼
        ┌────────────────────────────────┐
        │       🚚 APACHE NIFI           │
        │  - GetFile                     │
        │  - SplitText                   │
        │  - UpdateAttribute             │
        │  - PublishKafka                │
        └───────────────┬────────────────┘
                        │
                        ▼
        ┌────────────────────────────────┐
        │       📨 APACHE KAFKA          │
        │  Topic: unsw-nb15-v2           │
        │  3 Brokers + ZooKeeper         │
        │  3 Partitions (RF=1)           │
        └───────────────┬────────────────┘
                        │
                        ▼
        ┌────────────────────────────────┐
        │       ⚡ APACHE SPARK          │
        │  - Read from Kafka             │
        │  - Cleaning                    │
        │  - Schema Application          │
        │  - Type Casting                │
        │  - EDA (14 Analyses)           │
        └───────────────┬────────────────┘
                        │
                        ▼
        ┌────────────────────────────────┐
        │       🐘 POSTGRESQL            │
        │  Database: postgres            │
        │  Table: unsw_nb15              │
        │  2,540,047 Records             │
        └───────────────┬────────────────┘
                        │
                        ▼
        ┌────────────────────────────────┐
        │       📊 POWER BI              │
        │  3 Pages Dashboard             │
        │  - Executive Overview          │
        │  - Attack Analysis             │
        │  - Network Traffic             │
        └────────────────────────────────┘
```

---

## 🧩 المكونات التفصيلية

### 1. Raw Data Storage

<table dir="rtl" style="width: 100%; border-collapse: collapse; text-align: right;">
  <thead>
    <tr>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">العنصر</th>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">التفاصيل</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">الموقع</td><td style="padding: 8px; border: 1px solid #ddd;">data/raw/</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">المحتوى</td><td style="padding: 8px; border: 1px solid #ddd;">7 CSV Files</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">الحجم</td><td style="padding: 8px; border: 1px solid #ddd;">~642 MB</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">الصيغة</td><td style="padding: 8px; border: 1px solid #ddd;">CSV (بدون Header)</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">الوصول</td><td style="padding: 8px; border: 1px solid #ddd;">عبر Docker Volume</td></tr>
  </tbody>
</table>

---

### 2. Apache NiFi (Data Ingestion)

<table dir="rtl" style="width: 100%; border-collapse: collapse; text-align: right;">
  <thead>
    <tr>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">العنصر</th>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">التفاصيل</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">الإصدار</td><td style="padding: 8px; border: 1px solid #ddd;">2.10.0</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">Port</td><td style="padding: 8px; border: 1px solid #ddd;">7443 (HTTPS)</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">User</td><td style="padding: 8px; border: 1px solid #ddd;">admin</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">الوظيفة</td><td style="padding: 8px; border: 1px solid #ddd;">قراءة CSV + SplitText + Publish to Kafka</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">الإعداد الرئيسي</td><td style="padding: 8px; border: 1px solid #ddd;">Line Split Count = 1000</td></tr>
  </tbody>
</table>

#### Processors المستخدمة

<table dir="rtl" style="width: 100%; border-collapse: collapse; text-align: right;">
  <thead>
    <tr>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">#</th>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">Processor</th>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">الوظيفة</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">1</td><td style="padding: 8px; border: 1px solid #ddd;">GetFile</td><td style="padding: 8px; border: 1px solid #ddd;">قراءة الملفات من /data/raw/</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">2</td><td style="padding: 8px; border: 1px solid #ddd;">SplitText</td><td style="padding: 8px; border: 1px solid #ddd;">تقسيم الملفات الكبيرة إلى سجلات صغيرة</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">3</td><td style="padding: 8px; border: 1px solid #ddd;">UpdateAttribute</td><td style="padding: 8px; border: 1px solid #ddd;">إضافة Metadata (dataset, ingestion_time)</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">4</td><td style="padding: 8px; border: 1px solid #ddd;">PublishKafka</td><td style="padding: 8px; border: 1px solid #ddd;">إرسال البيانات إلى Kafka Topic</td></tr>
  </tbody>
</table>

---

### 3. Apache Kafka (Distributed Streaming)

<table dir="rtl" style="width: 100%; border-collapse: collapse; text-align: right;">
  <thead>
    <tr>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">العنصر</th>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">التفاصيل</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">الإصدار</td><td style="padding: 8px; border: 1px solid #ddd;">2.8.1</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">عدد Brokers</td><td style="padding: 8px; border: 1px solid #ddd;">3 (kafka1, kafka2, kafka3)</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">ZooKeeper</td><td style="padding: 8px; border: 1px solid #ddd;">zoo1</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">Ports</td><td style="padding: 8px; border: 1px solid #ddd;">9092, 9093, 9094</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">Topic</td><td style="padding: 8px; border: 1px solid #ddd;">unsw-nb15-v2</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">Partitions</td><td style="padding: 8px; border: 1px solid #ddd;">3</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">Replication Factor</td><td style="padding: 8px; border: 1px solid #ddd;">1</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">Max Message Size</td><td style="padding: 8px; border: 1px solid #ddd;">5 MB</td></tr>
  </tbody>
</table>

> ⚠️ **ملاحظة تقنية:** تم استخدام `Replication Factor = 1` مع 3 Brokers بهدف **توزيع الحمل (Load Distribution)** بين الـ Partitions، وليس لتحقيق **Fault Tolerance**. لتحقيق Fault Tolerance حقيقي، يجب رفع `Replication Factor` إلى 2 أو 3.

---

### 4. Apache Spark (Processing)

<table dir="rtl" style="width: 100%; border-collapse: collapse; text-align: right;">
  <thead>
    <tr>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">العنصر</th>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">التفاصيل</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">الإصدار</td><td style="padding: 8px; border: 1px solid #ddd;">3.1.2</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">الواجهة</td><td style="padding: 8px; border: 1px solid #ddd;">JupyterLab (PySpark 3)</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">Driver Memory</td><td style="padding: 8px; border: 1px solid #ddd;">2 GB</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">Max Result Size</td><td style="padding: 8px; border: 1px solid #ddd;">1 GB</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">Shuffle Partitions</td><td style="padding: 8px; border: 1px solid #ddd;">8</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">Jobs</td><td style="padding: 8px; border: 1px solid #ddd;">3 Notebooks</td></tr>
  </tbody>
</table>

#### Spark Jobs

<table dir="rtl" style="width: 100%; border-collapse: collapse; text-align: right;">
  <thead>
    <tr>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">#</th>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">Notebook</th>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">الوظيفة</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">1</td><td style="padding: 8px; border: 1px solid #ddd;">01_cleaning.ipynb</td><td style="padding: 8px; border: 1px solid #ddd;">قراءة Kafka + تنظيف + حفظ Parquet</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">2</td><td style="padding: 8px; border: 1px solid #ddd;">02_eda.ipynb</td><td style="padding: 8px; border: 1px solid #ddd;">14 تحليل استكشافي</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">3</td><td style="padding: 8px; border: 1px solid #ddd;">03_load_postgres.ipynb</td><td style="padding: 8px; border: 1px solid #ddd;">تحميل PostgreSQL</td></tr>
  </tbody>
</table>

---

### 5. PostgreSQL (Storage)

<table dir="rtl" style="width: 100%; border-collapse: collapse; text-align: right;">
  <thead>
    <tr>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">العنصر</th>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">التفاصيل</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">الإصدار</td><td style="padding: 8px; border: 1px solid #ddd;">13</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">Port</td><td style="padding: 8px; border: 1px solid #ddd;">6432 (خارجي)</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">Database</td><td style="padding: 8px; border: 1px solid #ddd;">postgres</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">Table</td><td style="padding: 8px; border: 1px solid #ddd;">unsw_nb15</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">Records</td><td style="padding: 8px; border: 1px solid #ddd;">2,540,047</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">Columns</td><td style="padding: 8px; border: 1px solid #ddd;">49</td></tr>
  </tbody>
</table>

#### Indexes

<table dir="rtl" style="width: 100%; border-collapse: collapse; text-align: right;">
  <thead>
    <tr>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">#</th>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">Index</th>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">Column</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">1</td><td style="padding: 8px; border: 1px solid #ddd;">idx_attack_cat</td><td style="padding: 8px; border: 1px solid #ddd;">attack_cat</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">2</td><td style="padding: 8px; border: 1px solid #ddd;">idx_label</td><td style="padding: 8px; border: 1px solid #ddd;">label</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">3</td><td style="padding: 8px; border: 1px solid #ddd;">idx_proto</td><td style="padding: 8px; border: 1px solid #ddd;">proto</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">4</td><td style="padding: 8px; border: 1px solid #ddd;">idx_service</td><td style="padding: 8px; border: 1px solid #ddd;">service</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">5</td><td style="padding: 8px; border: 1px solid #ddd;">idx_state</td><td style="padding: 8px; border: 1px solid #ddd;">state</td></tr>
  </tbody>
</table>

---

### 6. Power BI (Visualization)

<table dir="rtl" style="width: 100%; border-collapse: collapse; text-align: right;">
  <thead>
    <tr>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">العنصر</th>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">التفاصيل</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">الإصدار</td><td style="padding: 8px; border: 1px solid #ddd;">2.157.1354.0</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">Connection</td><td style="padding: 8px; border: 1px solid #ddd;">Import Mode</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">Pages</td><td style="padding: 8px; border: 1px solid #ddd;">3 Pages</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">Theme</td><td style="padding: 8px; border: 1px solid #ddd;">Custom Cyber Dark</td></tr>
  </tbody>
</table>

#### Dashboard Pages

<table dir="rtl" style="width: 100%; border-collapse: collapse; text-align: right;">
  <thead>
    <tr>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">#</th>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">الصفحة</th>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">المحتوى</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">1</td><td style="padding: 8px; border: 1px solid #ddd;">Executive Overview</td><td style="padding: 8px; border: 1px solid #ddd;">5 KPIs + Donut + Bar + Line + Pie</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">2</td><td style="padding: 8px; border: 1px solid #ddd;">Attack Analysis</td><td style="padding: 8px; border: 1px solid #ddd;">3 KPIs + Bars + Stacked Column</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">3</td><td style="padding: 8px; border: 1px solid #ddd;">Network Traffic</td><td style="padding: 8px; border: 1px solid #ddd;">3 KPIs + Pie + Bars + Treemap</td></tr>
  </tbody>
</table>

---

## 🌐 Docker Containers

<table dir="rtl" style="width: 100%; border-collapse: collapse; text-align: right;">
  <thead>
    <tr>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">#</th>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">Container</th>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">Image</th>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">Port</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">1</td><td style="padding: 8px; border: 1px solid #ddd;">nifi</td><td style="padding: 8px; border: 1px solid #ddd;">apache/nifi:latest</td><td style="padding: 8px; border: 1px solid #ddd;">7443</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">2</td><td style="padding: 8px; border: 1px solid #ddd;">zoo1</td><td style="padding: 8px; border: 1px solid #ddd;">wurstmeister/zookeeper</td><td style="padding: 8px; border: 1px solid #ddd;">2181</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">3</td><td style="padding: 8px; border: 1px solid #ddd;">kafka1</td><td style="padding: 8px; border: 1px solid #ddd;">wurstmeister/kafka</td><td style="padding: 8px; border: 1px solid #ddd;">9092</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">4</td><td style="padding: 8px; border: 1px solid #ddd;">kafka2</td><td style="padding: 8px; border: 1px solid #ddd;">wurstmeister/kafka</td><td style="padding: 8px; border: 1px solid #ddd;">9093</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">5</td><td style="padding: 8px; border: 1px solid #ddd;">kafka3</td><td style="padding: 8px; border: 1px solid #ddd;">wurstmeister/kafka</td><td style="padding: 8px; border: 1px solid #ddd;">9094</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">6</td><td style="padding: 8px; border: 1px solid #ddd;">kafka-ui</td><td style="padding: 8px; border: 1px solid #ddd;">provectuslabs/kafka-ui</td><td style="padding: 8px; border: 1px solid #ddd;">8090</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">7</td><td style="padding: 8px; border: 1px solid #ddd;">itvdelab</td><td style="padding: 8px; border: 1px solid #ddd;">itversity/itvdelab</td><td style="padding: 8px; border: 1px solid #ddd;">8888, 4040</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">8</td><td style="padding: 8px; border: 1px solid #ddd;">dockerfilespark-cluster_util_db-1</td><td style="padding: 8px; border: 1px solid #ddd;">postgres:13</td><td style="padding: 8px; border: 1px solid #ddd;">6432</td></tr>
  </tbody>
</table>

---

## 📊 Performance Metrics

<table dir="rtl" style="width: 100%; border-collapse: collapse; text-align: right;">
  <thead>
    <tr>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">المقياس</th>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">القيمة</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">حجم البيانات الخام</td><td style="padding: 8px; border: 1px solid #ddd;">642 MB</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">عدد السجلات الأصلية</td><td style="padding: 8px; border: 1px solid #ddd;">~2.54M</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">حجم Parquet بعد التنظيف</td><td style="padding: 8px; border: 1px solid #ddd;">166 MB</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">عدد السجلات بعد التنظيف</td><td style="padding: 8px; border: 1px solid #ddd;">2,540,047</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">عدد الأعمدة</td><td style="padding: 8px; border: 1px solid #ddd;">49</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">عدد Indexes في PostgreSQL</td><td style="padding: 8px; border: 1px solid #ddd;">5</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">عدد صفحات Power BI</td><td style="padding: 8px; border: 1px solid #ddd;">3</td></tr>
  </tbody>
</table>

---

## 🎯 خصائص المعمارية

- ✅ **Modular Design**: كل مرحلة مستقلة وموثقة.
- ✅ **Distributed Ingestion**: NiFi + Kafka Cluster.
- ✅ **Extensible**: يمكن توسيع Pipeline بإضافة مراحل جديدة.
- ✅ **Reproducible**: Docker يضمن بيئة موحدة.
- ✅ **Documented**: كل مرحلة موثقة بالتفصيل.
- ⚠️ **Load Distribution**: Kafka 3 Brokers مع RF=1 يوزّع الحمل لكن لا يحقق Fault Tolerance.

---

## 📌 ملاحظات تقنية

### 1. NiFi PublishKafka
- لا يستخدم Record Reader.
- يرسل CSV كنص خام.
- يتفادى مشاكل Schema Validation.

### 2. Kafka Topic
- اسم مختلف (v2) لتفادي المشاكل القديمة.
- 3 Partitions لتوزيع الحمل.
- Replication Factor = 1 (توزيع حمل فقط).

### 3. Spark Memory
- Driver: 2 GB.
- Max Result: 1 GB.
- يتفادى OutOfMemoryError.

### 4. Power BI Import Mode
- أسرع من DirectQuery.
- يعمل بدون اتصال مباشر بالـ DB.

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
    <tr><td style="padding: 8px; border: 1px solid #ddd;">2</td><td style="padding: 8px; border: 1px solid #ddd;"><b>01_architecture.md</b></td><td style="padding: 8px; border: 1px solid #ddd;">المعمارية (هذا الملف)</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">3</td><td style="padding: 8px; border: 1px solid #ddd;"><b>02_dataset.md</b></td><td style="padding: 8px; border: 1px solid #ddd;">تفاصيل Dataset</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">4</td><td style="padding: 8px; border: 1px solid #ddd;"><b>03_pipeline.md</b></td><td style="padding: 8px; border: 1px solid #ddd;">مراحل التنفيذ</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">5</td><td style="padding: 8px; border: 1px solid #ddd;"><b>04_results.md</b></td><td style="padding: 8px; border: 1px solid #ddd;">النتائج والرؤى</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">6</td><td style="padding: 8px; border: 1px solid #ddd;"><b>05_troubleshooting.md</b></td><td style="padding: 8px; border: 1px solid #ddd;">المشاكل والحلول</td></tr>
  </tbody>
</table>

---

### 🛡️ UNSW-NB15 Cybersecurity Analytics Platform

**Big Data × Cybersecurity × Data Analytics**

**© 2026 — يوسف مختار أنعم الجرادي**