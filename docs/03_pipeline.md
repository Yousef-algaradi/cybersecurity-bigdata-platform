# 🔄 مراحل التنفيذ | Data Pipeline

> **توثيق كامل لمراحل بناء End-to-End Data Pipeline**

---

## 🎯 نظرة عامة

تم تنفيذ المشروع على **6 مراحل أساسية** متسلسلة، بدءاً من تجهيز البيئة (Docker) وانتهاءً بلوحة تحكم Power BI. كل مرحلة تعتمد على مخرجات المرحلة السابقة.

---

## 📋 المراحل الست

<table dir="rtl" style="width: 100%; border-collapse: collapse; text-align: right;">
  <thead>
    <tr>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">#</th>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">المرحلة</th>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">التقنية</th>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">المخرج</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">1</td><td style="padding: 8px; border: 1px solid #ddd;">Environment Setup</td><td style="padding: 8px; border: 1px solid #ddd;">Docker Desktop</td><td style="padding: 8px; border: 1px solid #ddd;">8 Containers Running</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">2</td><td style="padding: 8px; border: 1px solid #ddd;">Data Ingestion</td><td style="padding: 8px; border: 1px solid #ddd;">Apache NiFi</td><td style="padding: 8px; border: 1px solid #ddd;">CSV → Kafka</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">3</td><td style="padding: 8px; border: 1px solid #ddd;">Data Streaming</td><td style="padding: 8px; border: 1px solid #ddd;">Apache Kafka</td><td style="padding: 8px; border: 1px solid #ddd;">Topic: unsw-nb15-v2</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">4</td><td style="padding: 8px; border: 1px solid #ddd;">Data Cleaning</td><td style="padding: 8px; border: 1px solid #ddd;">Apache Spark</td><td style="padding: 8px; border: 1px solid #ddd;">Parquet Cleaned Dataset</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">5</td><td style="padding: 8px; border: 1px solid #ddd;">Data Storage</td><td style="padding: 8px; border: 1px solid #ddd;">PostgreSQL</td><td style="padding: 8px; border: 1px solid #ddd;">Table: unsw_nb15</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">6</td><td style="padding: 8px; border: 1px solid #ddd;">Visualization</td><td style="padding: 8px; border: 1px solid #ddd;">Power BI</td><td style="padding: 8px; border: 1px solid #ddd;">3-Page Dashboard</td></tr>
  </tbody>
</table>

---

## 🚀 المرحلة 1: Environment Setup

### الهدف
تجهيز بيئة Docker تحتوي على كل الحاويات اللازمة.

### الحاويات المستخدمة

<table dir="rtl" style="width: 100%; border-collapse: collapse; text-align: right;">
  <thead>
    <tr>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">#</th>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">Container</th>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">Image</th>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">Port</th>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">الوظيفة</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">1</td><td style="padding: 8px; border: 1px solid #ddd;">nifi</td><td style="padding: 8px; border: 1px solid #ddd;">apache/nifi</td><td style="padding: 8px; border: 1px solid #ddd;">7443</td><td style="padding: 8px; border: 1px solid #ddd;">Data Ingestion</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">2</td><td style="padding: 8px; border: 1px solid #ddd;">zoo1</td><td style="padding: 8px; border: 1px solid #ddd;">wurstmeister/zookeeper</td><td style="padding: 8px; border: 1px solid #ddd;">2181</td><td style="padding: 8px; border: 1px solid #ddd;">Kafka Coordination</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">3</td><td style="padding: 8px; border: 1px solid #ddd;">kafka1</td><td style="padding: 8px; border: 1px solid #ddd;">wurstmeister/kafka</td><td style="padding: 8px; border: 1px solid #ddd;">9092</td><td style="padding: 8px; border: 1px solid #ddd;">Broker 1</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">4</td><td style="padding: 8px; border: 1px solid #ddd;">kafka2</td><td style="padding: 8px; border: 1px solid #ddd;">wurstmeister/kafka</td><td style="padding: 8px; border: 1px solid #ddd;">9093</td><td style="padding: 8px; border: 1px solid #ddd;">Broker 2</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">5</td><td style="padding: 8px; border: 1px solid #ddd;">kafka3</td><td style="padding: 8px; border: 1px solid #ddd;">wurstmeister/kafka</td><td style="padding: 8px; border: 1px solid #ddd;">9094</td><td style="padding: 8px; border: 1px solid #ddd;">Broker 3</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">6</td><td style="padding: 8px; border: 1px solid #ddd;">kafka-ui</td><td style="padding: 8px; border: 1px solid #ddd;">provectuslabs/kafka-ui</td><td style="padding: 8px; border: 1px solid #ddd;">8090</td><td style="padding: 8px; border: 1px solid #ddd;">Kafka Monitoring</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">7</td><td style="padding: 8px; border: 1px solid #ddd;">itvdelab</td><td style="padding: 8px; border: 1px solid #ddd;">itversity/itvdelab</td><td style="padding: 8px; border: 1px solid #ddd;">8888</td><td style="padding: 8px; border: 1px solid #ddd;">Spark + JupyterLab</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">8</td><td style="padding: 8px; border: 1px solid #ddd;">dockerfilespark-cluster_util_db-1</td><td style="padding: 8px; border: 1px solid #ddd;">postgres:13</td><td style="padding: 8px; border: 1px solid #ddd;">6432</td><td style="padding: 8px; border: 1px solid #ddd;">Storage</td></tr>
  </tbody>
</table>

### الخطوات
1. تثبيت **Docker Desktop** (28.3.2).
2. إعداد `docker-compose.yml`.
3. تشغيل كل الحاويات: `docker-compose up -d`.
4. التأكد: `docker ps`.

### المخرج
✅ **8 حاويات** تعمل على نفس الشبكة.

---

## 🚚 المرحلة 2: Data Ingestion (NiFi)

### الهدف
قراءة ملفات CSV وإرسالها إلى Kafka.

### Flow في NiFi

```text
┌──────────────┐    ┌───────────┐    ┌────────────────┐    ┌──────────────┐
│   GetFile    │───>│ SplitText │───>│ UpdateAttribute│───>│ PublishKafka │
│  /data/raw/  │    │ Count=1000│    │ + Metadata     │    │ unsw-nb15-v2 │
└──────────────┘    └───────────┘    └────────────────┘    └──────────────┘
```

### إعدادات Processors

<table dir="rtl" style="width: 100%; border-collapse: collapse; text-align: right;">
  <thead>
    <tr>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">Processor</th>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">الإعداد الرئيسي</th>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">القيمة</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">GetFile</td><td style="padding: 8px; border: 1px solid #ddd;">Input Directory</td><td style="padding: 8px; border: 1px solid #ddd;">/data/raw/</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">GetFile</td><td style="padding: 8px; border: 1px solid #ddd;">File Filter</td><td style="padding: 8px; border: 1px solid #ddd;">UNSW-NB15_[1-4]\.csv</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">SplitText</td><td style="padding: 8px; border: 1px solid #ddd;">Line Split Count</td><td style="padding: 8px; border: 1px solid #ddd;">1000</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">SplitText</td><td style="padding: 8px; border: 1px solid #ddd;">Header Line Count</td><td style="padding: 8px; border: 1px solid #ddd;">0</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">PublishKafka</td><td style="padding: 8px; border: 1px solid #ddd;">Topic</td><td style="padding: 8px; border: 1px solid #ddd;">unsw-nb15-v2</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">PublishKafka</td><td style="padding: 8px; border: 1px solid #ddd;">Max Request Size</td><td style="padding: 8px; border: 1px solid #ddd;">5 MB</td></tr>
  </tbody>
</table>

### المخرج
✅ **2,544 Kafka Messages** (تحتوي إجمالاً على **2,540,047 record**).

> **ملاحظة تقنية:** NiFi يرسل البيانات على شكل دفعات (Batches) بحجم 1,000 سطر لكل Message. لذلك عدد Messages ≠ عدد Records.

---

## 📨 المرحلة 3: Data Streaming (Kafka)

### الهدف
نقل البيانات من NiFi إلى Spark عبر Kafka.

### Topic Configuration

<table dir="rtl" style="width: 100%; border-collapse: collapse; text-align: right;">
  <thead>
    <tr>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">الإعداد</th>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">القيمة</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">Topic Name</td><td style="padding: 8px; border: 1px solid #ddd;">unsw-nb15-v2</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">Partitions</td><td style="padding: 8px; border: 1px solid #ddd;">3</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">Replication Factor</td><td style="padding: 8px; border: 1px solid #ddd;">1</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">Max Message Size</td><td style="padding: 8px; border: 1px solid #ddd;">5 MB</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">Bootstrap Servers</td><td style="padding: 8px; border: 1px solid #ddd;">kafka1:19092, kafka2:19093, kafka3:19094</td></tr>
  </tbody>
</table>

> ⚠️ **ملاحظة تقنية:** تم استخدام `Replication Factor = 1` لتحقيق **توزيع الحمل (Load Distribution)** على 3 Partitions. هذا الإعداد **لا يوفّر Fault Tolerance** حقيقي، لأن النسخ الاحتياطية غير موجودة عند تعطّل أحد Brokers.

### إنشاء Topic

```bash
docker exec kafka1 kafka-topics.sh \
  --bootstrap-server kafka1:19092 \
  --create --topic unsw-nb15-v2 \
  --partitions 3 --replication-factor 1
```

### المخرج
✅ Topic جاهز مع 3 Partitions.

---

## ⚡ المرحلة 4: Data Cleaning (Spark)

### الهدف
قراءة البيانات من Kafka وتنظيفها وتحويلها إلى Parquet.

### Notebook: 01_cleaning.ipynb

#### الخطوات:
1. **Read from Kafka**: قراءة 2,544 رسالة.
2. **Explode Messages**: تفجير الرسائل إلى 2,540,047 سطر.
3. **Apply Schema**: تطبيق 49 عموداً.
4. **Clean Values**: استبدال `-` و `""` بـ null.
5. **Type Casting**: تحويل الأنواع (Integer, Double).
6. **Save Parquet**: حفظ 166 MB.

### المخرج
✅ ملف `unsw_cleaned.parquet` (166 MB).

---

## 📊 المرحلة 4.5: Exploratory Data Analysis (Spark)

### Notebook: 02_eda.ipynb

### 14 تحليل

<table dir="rtl" style="width: 100%; border-collapse: collapse; text-align: right;">
  <thead>
    <tr>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">#</th>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">التحليل</th>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">المخرج</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">1</td><td style="padding: 8px; border: 1px solid #ddd;">Label Distribution</td><td style="padding: 8px; border: 1px solid #ddd;">01_label_distribution.png</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">2</td><td style="padding: 8px; border: 1px solid #ddd;">Attack Categories</td><td style="padding: 8px; border: 1px solid #ddd;">02_attack_cat.png</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">3</td><td style="padding: 8px; border: 1px solid #ddd;">Protocol Distribution</td><td style="padding: 8px; border: 1px solid #ddd;">03_proto.png</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">4</td><td style="padding: 8px; border: 1px solid #ddd;">Service Distribution</td><td style="padding: 8px; border: 1px solid #ddd;">04_service.png</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">5</td><td style="padding: 8px; border: 1px solid #ddd;">State Distribution</td><td style="padding: 8px; border: 1px solid #ddd;">05_state.png</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">6</td><td style="padding: 8px; border: 1px solid #ddd;">Descriptive Statistics</td><td style="padding: 8px; border: 1px solid #ddd;">06_statistics.csv</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">7</td><td style="padding: 8px; border: 1px solid #ddd;">Correlation Matrix</td><td style="padding: 8px; border: 1px solid #ddd;">07_correlation.png</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">8</td><td style="padding: 8px; border: 1px solid #ddd;">Time Series</td><td style="padding: 8px; border: 1px solid #ddd;">08_time_series.png</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">9</td><td style="padding: 8px; border: 1px solid #ddd;">Top Source IPs</td><td style="padding: 8px; border: 1px solid #ddd;">09_top_src_ip.png</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">10</td><td style="padding: 8px; border: 1px solid #ddd;">Top Destination IPs</td><td style="padding: 8px; border: 1px solid #ddd;">10_top_dst_ip.png</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">11</td><td style="padding: 8px; border: 1px solid #ddd;">Hour Traffic</td><td style="padding: 8px; border: 1px solid #ddd;">11_hour_traffic.png</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">12</td><td style="padding: 8px; border: 1px solid #ddd;">Protocol Attack Ratio</td><td style="padding: 8px; border: 1px solid #ddd;">12_proto_attack.png</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">13</td><td style="padding: 8px; border: 1px solid #ddd;">Service Attack Ratio</td><td style="padding: 8px; border: 1px solid #ddd;">13_service_attack.png</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">14</td><td style="padding: 8px; border: 1px solid #ddd;">Volume Analysis</td><td style="padding: 8px; border: 1px solid #ddd;">14_volume_analysis.png</td></tr>
  </tbody>
</table>

### المخرج
✅ 14 ملفاً (10 صور PNG + 2 CSV + 2 مصفوفة).

---

## 🐘 المرحلة 5: Data Storage (PostgreSQL)

### Notebook: 03_load_postgres.ipynb

### إنشاء الجدول

```sql
CREATE TABLE unsw_nb15 (
    id SERIAL PRIMARY KEY,
    srcip VARCHAR(50),
    sport INTEGER,
    ...
    label INTEGER
);
```

### Indexes

<table dir="rtl" style="width: 100%; border-collapse: collapse; text-align: right;">
  <thead>
    <tr>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">Index</th>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">Column</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">idx_attack_cat</td><td style="padding: 8px; border: 1px solid #ddd;">attack_cat</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">idx_label</td><td style="padding: 8px; border: 1px solid #ddd;">label</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">idx_proto</td><td style="padding: 8px; border: 1px solid #ddd;">proto</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">idx_service</td><td style="padding: 8px; border: 1px solid #ddd;">service</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">idx_state</td><td style="padding: 8px; border: 1px solid #ddd;">state</td></tr>
  </tbody>
</table>

### تحميل البيانات
- **Method**: JDBC (Spark → PostgreSQL).
- **Batch Size**: 10,000.
- **Mode**: Append.
- **Records**: 2,540,047.

### المخرج
✅ جدول `unsw_nb15` مع 5 Indexes.

---

## 📊 المرحلة 6: Visualization (Power BI)

### الاتصال
- **Server**: localhost:6432
- **Database**: postgres
- **Table**: unsw_nb15
- **Mode**: Import

### Dashboard Pages

<table dir="rtl" style="width: 100%; border-collapse: collapse; text-align: right;">
  <thead>
    <tr>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">#</th>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">الصفحة</th>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">المحتوى</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">1</td><td style="padding: 8px; border: 1px solid #ddd;">Executive Overview</td><td style="padding: 8px; border: 1px solid #ddd;">5 KPIs + 4 Charts</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">2</td><td style="padding: 8px; border: 1px solid #ddd;">Attack Analysis</td><td style="padding: 8px; border: 1px solid #ddd;">3 KPIs + 4 Charts</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">3</td><td style="padding: 8px; border: 1px solid #ddd;">Network Traffic</td><td style="padding: 8px; border: 1px solid #ddd;">3 KPIs + 4 Charts</td></tr>
  </tbody>
</table>

### DAX Measures (12 Total)

<table dir="rtl" style="width: 100%; border-collapse: collapse; text-align: right;">
  <thead>
    <tr>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">#</th>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">Measure</th>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">الوظيفة</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">1</td><td style="padding: 8px; border: 1px solid #ddd;">Total Records</td><td style="padding: 8px; border: 1px solid #ddd;">عدد السجلات</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">2</td><td style="padding: 8px; border: 1px solid #ddd;">Attack Count</td><td style="padding: 8px; border: 1px solid #ddd;">عدد الهجمات</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">3</td><td style="padding: 8px; border: 1px solid #ddd;">Normal Count</td><td style="padding: 8px; border: 1px solid #ddd;">عدد Normal</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">4</td><td style="padding: 8px; border: 1px solid #ddd;">Attack %</td><td style="padding: 8px; border: 1px solid #ddd;">نسبة الهجمات</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">5</td><td style="padding: 8px; border: 1px solid #ddd;">Normal %</td><td style="padding: 8px; border: 1px solid #ddd;">نسبة Normal</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">6</td><td style="padding: 8px; border: 1px solid #ddd;">Total Bytes</td><td style="padding: 8px; border: 1px solid #ddd;">إجمالي البايتات</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">7</td><td style="padding: 8px; border: 1px solid #ddd;">Total Packets</td><td style="padding: 8px; border: 1px solid #ddd;">إجمالي الحزم</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">8</td><td style="padding: 8px; border: 1px solid #ddd;">Avg Duration</td><td style="padding: 8px; border: 1px solid #ddd;">متوسط المدة</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">9</td><td style="padding: 8px; border: 1px solid #ddd;">Attack Avg Bytes</td><td style="padding: 8px; border: 1px solid #ddd;">متوسط بايتات الهجمات</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">10</td><td style="padding: 8px; border: 1px solid #ddd;">Normal Avg Bytes</td><td style="padding: 8px; border: 1px solid #ddd;">متوسط بايتات Normal</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">11</td><td style="padding: 8px; border: 1px solid #ddd;">Attack Avg Packets</td><td style="padding: 8px; border: 1px solid #ddd;">متوسط حزم الهجمات</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">12</td><td style="padding: 8px; border: 1px solid #ddd;">Normal Avg Packets</td><td style="padding: 8px; border: 1px solid #ddd;">متوسط حزم Normal</td></tr>
  </tbody>
</table>

### Calculated Columns

<table dir="rtl" style="width: 100%; border-collapse: collapse; text-align: right;">
  <thead>
    <tr>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">#</th>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">Column</th>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">الوظيفة</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">1</td><td style="padding: 8px; border: 1px solid #ddd;">Attack Category</td><td style="padding: 8px; border: 1px solid #ddd;">توحيد attack_cat</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">2</td><td style="padding: 8px; border: 1px solid #ddd;">Attack Status</td><td style="padding: 8px; border: 1px solid #ddd;">Normal/Attack</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">3</td><td style="padding: 8px; border: 1px solid #ddd;">Hour</td><td style="padding: 8px; border: 1px solid #ddd;">ساعة الحدث</td></tr>
  </tbody>
</table>

### المخرج
✅ Dashboard من 3 صفحات.

---

## 📊 ملخص Pipeline

<table dir="rtl" style="width: 100%; border-collapse: collapse; text-align: right;">
  <thead>
    <tr>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">المرحلة</th>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">Input</th>
      <th style="text-align: right; padding: 8px; border: 1px solid #ddd;">Output</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">Setup</td><td style="padding: 8px; border: 1px solid #ddd;">Docker Desktop</td><td style="padding: 8px; border: 1px solid #ddd;">8 Containers</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">Ingestion</td><td style="padding: 8px; border: 1px solid #ddd;">7 CSV (642 MB)</td><td style="padding: 8px; border: 1px solid #ddd;">2,544 Kafka Messages</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">Streaming</td><td style="padding: 8px; border: 1px solid #ddd;">NiFi Messages</td><td style="padding: 8px; border: 1px solid #ddd;">Topic: unsw-nb15-v2</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">Cleaning</td><td style="padding: 8px; border: 1px solid #ddd;">Kafka Stream</td><td style="padding: 8px; border: 1px solid #ddd;">Parquet (166 MB)</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">EDA</td><td style="padding: 8px; border: 1px solid #ddd;">Parquet</td><td style="padding: 8px; border: 1px solid #ddd;">14 Analyses</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">Storage</td><td style="padding: 8px; border: 1px solid #ddd;">Parquet</td><td style="padding: 8px; border: 1px solid #ddd;">PostgreSQL (2,540,047 records)</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">Visualization</td><td style="padding: 8px; border: 1px solid #ddd;">PostgreSQL</td><td style="padding: 8px; border: 1px solid #ddd;">3-Page Dashboard</td></tr>
  </tbody>
</table>

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
    <tr><td style="padding: 8px; border: 1px solid #ddd;">4</td><td style="padding: 8px; border: 1px solid #ddd;"><b>03_pipeline.md</b></td><td style="padding: 8px; border: 1px solid #ddd;">مراحل التنفيذ (هذا الملف)</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">5</td><td style="padding: 8px; border: 1px solid #ddd;"><b>04_results.md</b></td><td style="padding: 8px; border: 1px solid #ddd;">النتائج</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;">6</td><td style="padding: 8px; border: 1px solid #ddd;"><b>05_troubleshooting.md</b></td><td style="padding: 8px; border: 1px solid #ddd;">المشاكل</td></tr>
  </tbody>
</table>

---

### 🛡️ UNSW-NB15 Cybersecurity Analytics Platform

**Big Data × Cybersecurity × Data Analytics**

**© 2026 — يوسف مختار أنعم الجرادي**