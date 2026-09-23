#!/usr/bin/env python
# coding: utf-8

# In[23]:


# =========================================================
# 01_cleaning.py — المرحلة 1: قراءة وتنظيف البيانات
# =========================================================

from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    col, when, trim, lower, upper,
    to_timestamp, from_unixtime,
    count, isnan, isnull
)
from pyspark.sql.types import (
    StructType, StructField,
    StringType, IntegerType, DoubleType, LongType
)
import os

print("✅ Imports OK")


# In[24]:


# =========================================================
# إنشاء SparkSession مع إعدادات Kafka
# =========================================================

spark = SparkSession.builder     .appName("UNSW-NB15-Cleaning")     .config("spark.jars.packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.0")     .config("spark.sql.shuffle.partitions", "8")     .config("spark.sql.adaptive.enabled", "true")     .getOrCreate()

spark.sparkContext.setLogLevel("WARN")

print(f"✅ Spark version: {spark.version}")
print(f"✅ App Name: {spark.sparkContext.appName}")


# In[25]:


# =========================================================
# اختبار الاتصال بـ Kafka
# =========================================================

kafka_df = spark.readStream     .format("kafka")     .option("kafka.bootstrap.servers", "kafka1:19092,kafka2:19093,kafka3:19094")     .option("subscribe", "unsw-nb15-v2")     .option("startingOffsets", "earliest")     .option("failOnDataLoss", "false")     .load()

print("✅ Kafka connection established")
print(f"Schema:")
kafka_df.printSchema()


# In[26]:


# =========================================================
# قراءة البيانات كـ Batch (بدل Streaming)
# =========================================================

# نقرأ كل الرسائل الموجودة حالياً في Kafka
df_raw = spark.read     .format("kafka")     .option("kafka.bootstrap.servers", "kafka1:19092,kafka2:19093,kafka3:19094")     .option("subscribe", "unsw-nb15-v2")     .option("startingOffsets", "earliest")     .option("endingOffsets", "latest")     .option("failOnDataLoss", "false")     .load()

print(f"✅ عدد السجلات في Kafka: {df_raw.count()}")
df_raw.printSchema()
df_raw.selectExpr("CAST(value AS STRING)").show(3, truncate=False)


# In[27]:


# =========================================================
# Schema الكامل (49 عمود)
# =========================================================

schema = StructType([
    StructField("srcip", StringType(), True),
    StructField("sport", StringType(), True),
    StructField("dstip", StringType(), True),
    StructField("dsport", StringType(), True),
    StructField("proto", StringType(), True),
    StructField("state", StringType(), True),
    StructField("dur", StringType(), True),
    StructField("sbytes", StringType(), True),
    StructField("dbytes", StringType(), True),
    StructField("sttl", StringType(), True),
    StructField("dttl", StringType(), True),
    StructField("sloss", StringType(), True),
    StructField("dloss", StringType(), True),
    StructField("service", StringType(), True),
    StructField("Sload", StringType(), True),
    StructField("Dload", StringType(), True),
    StructField("Spkts", StringType(), True),
    StructField("Dpkts", StringType(), True),
    StructField("swin", StringType(), True),
    StructField("dwin", StringType(), True),
    StructField("stcpb", StringType(), True),
    StructField("dtcpb", StringType(), True),
    StructField("smeansz", StringType(), True),
    StructField("dmeansz", StringType(), True),
    StructField("trans_depth", StringType(), True),
    StructField("res_bdy_len", StringType(), True),
    StructField("Sjit", StringType(), True),
    StructField("Djit", StringType(), True),
    StructField("Stime", StringType(), True),
    StructField("Ltime", StringType(), True),
    StructField("Sintpkt", StringType(), True),
    StructField("Dintpkt", StringType(), True),
    StructField("tcprtt", StringType(), True),
    StructField("synack", StringType(), True),
    StructField("ackdat", StringType(), True),
    StructField("is_sm_ips_ports", StringType(), True),
    StructField("ct_state_ttl", StringType(), True),
    StructField("ct_flw_http_mthd", StringType(), True),
    StructField("is_ftp_login", StringType(), True),
    StructField("ct_ftp_cmd", StringType(), True),
    StructField("ct_srv_src", StringType(), True),
    StructField("ct_srv_dst", StringType(), True),
    StructField("ct_dst_ltm", StringType(), True),
    StructField("ct_src_ltm", StringType(), True),
    StructField("ct_src_dport_ltm", StringType(), True),
    StructField("ct_dst_sport_ltm", StringType(), True),
    StructField("ct_dst_src_ltm", StringType(), True),
    StructField("attack_cat", StringType(), True),
    StructField("Label", StringType(), True),
])

print(f"✅ Schema defined: {len(schema.fields)} columns")


# In[28]:


# =========================================================
# تحويل البيانات من Kafka إلى String
# =========================================================

from pyspark.sql.functions import from_csv, col

# نحوّل قيمة Kafka (Binary) إلى String
df_string = df_raw.selectExpr("CAST(value AS STRING) as csv_line")

print(f"✅ عدد السطور: {df_string.count()}")
df_string.show(5, truncate=False)


# In[29]:


# =========================================================
# تقسيم CSV إلى 49 عمود
# =========================================================

# نقسم السطر على الفاصلة
from pyspark.sql.functions import split

df_split = df_string.withColumn("cols", split(col("csv_line"), ","))

print(f"✅ تم التقسيم")
df_split.select("csv_line").show(2, truncate=True)
print(f"عدد الأعمدة بعد التقسيم: {len(df_split.select('cols').first()['cols'])}")


# In[30]:


# =========================================================
# تطبيق Schema على الأعمدة
# =========================================================

# نحوّل المصفوفة إلى 49 عمود
df_columns = df_split.select(
    *[col("cols").getItem(i).alias(schema.fields[i].name) for i in range(49)]
)

print(f"✅ تم تطبيق Schema")
df_columns.printSchema()
df_columns.show(3, truncate=False)


# In[31]:


# =========================================================
# تنظيف القيم الناقصة
# =========================================================

from pyspark.sql.functions import when, trim

df_clean = df_columns

# استبدل "-" و "" بـ null
for field in schema.fields:
    col_name = field.name
    df_clean = df_clean.withColumn(
        col_name,
        when(
            (col(col_name) == "-") | (trim(col(col_name)) == ""),
            None
        ).otherwise(trim(col(col_name)))
    )

print(f"✅ تم تنظيف القيم الناقصة")
df_clean.show(3, truncate=False)


# In[32]:


# =========================================================
# تحويل الأنواع
# =========================================================

from pyspark.sql.types import IntegerType, DoubleType

# قائمة الأعمدة الرقمية (Integer)
int_cols = [
    "sport", "dsport", "sbytes", "dbytes", "sttl", "dttl",
    "sloss", "dloss", "Spkts", "Dpkts", "swin", "dwin",
    "stcpb", "dtcpb", "smeansz", "dmeansz", "trans_depth",
    "res_bdy_len", "Stime", "Ltime", "is_sm_ips_ports",
    "ct_state_ttl", "ct_flw_http_mthd", "is_ftp_login",
    "ct_ftp_cmd", "ct_srv_src", "ct_srv_dst", "ct_dst_ltm",
    "ct_src_ltm", "ct_src_dport_ltm", "ct_dst_sport_ltm",
    "ct_dst_src_ltm", "Label"
]

# قائمة الأعمدة العشرية (Double)
double_cols = [
    "dur", "Sload", "Dload", "Sjit", "Djit",
    "Sintpkt", "Dintpkt", "tcprtt", "synack", "ackdat"
]

# تحويل
for c in int_cols:
    df_clean = df_clean.withColumn(c, col(c).cast(IntegerType()))

for c in double_cols:
    df_clean = df_clean.withColumn(c, col(c).cast(DoubleType()))

print(f"✅ تم تحويل الأنواع")
df_clean.printSchema()


# In[22]:


pip install pandas numpy pyarrow


# In[33]:


# حفظ CSV عبر Pandas
import pandas as pd

df_pandas = df_clean.toPandas()

df_pandas.to_csv(
    "/workspace/data/curated/unsw_nb15_cleaned.csv",
    index=False,
    encoding="utf-8"
)

print(f"✅ عدد السجلات: {len(df_pandas)}")
print("✅ تم الحفظ: unsw_nb15_cleaned.csv")


# In[34]:


# =========================================================
# 1. تحقق من Kafka
# =========================================================

df_check = spark.read     .format("kafka")     .option("kafka.bootstrap.servers", "kafka1:19092,kafka2:19093,kafka3:19094")     .option("subscribe", "unsw-nb15-v2")     .option("startingOffsets", "earliest")     .option("endingOffsets", "latest")     .load()

total = df_check.count()
print(f"📊 عدد السجلات في Kafka: {total}")


# In[35]:


# =========================================================
# تحقق: كم سطر فعلي في Kafka؟
# =========================================================

# نقرأ أول 3 رسائل فقط لفحصها
df_sample = spark.read     .format("kafka")     .option("kafka.bootstrap.servers", "kafka1:19092,kafka2:19093,kafka3:19094")     .option("subscribe", "unsw-nb15-v2")     .option("startingOffsets", "earliest")     .option("endingOffsets", "latest")     .load()     .selectExpr("CAST(value AS STRING) as csv_batch")

# نأخذ أول رسالة
sample = df_sample.first()
if sample:
    csv_content = sample['csv_batch']
    lines = csv_content.split('\n')
    print(f"✅ عدد السطور في أول رسالة: {len(lines)}")
    print(f"✅ أول سطر: {lines[0][:100]}...")
    print(f"✅ آخر سطر: {lines[-1][:100]}...")


# In[36]:


# =========================================================
# قراءة كل Kafka + تفجير الرسائل إلى سطور
# =========================================================

from pyspark.sql.functions import explode, split, col

# 1. قراءة Kafka
df_batches = spark.read     .format("kafka")     .option("kafka.bootstrap.servers", "kafka1:19092,kafka2:19093,kafka3:19094")     .option("subscribe", "unsw-nb15-v2")     .option("startingOffsets", "earliest")     .option("endingOffsets", "latest")     .load()     .selectExpr("CAST(value AS STRING) as batch")

# 2. تفجير كل رسالة إلى سطور
df_lines = df_batches     .withColumn("line", explode(split(col("batch"), "\n")))     .select("line")     .filter(col("line") != "")

print(f"📊 عدد السطور الإجمالي: {df_lines.count()}")


# In[37]:


# =========================================================
# تطبيق 49 عمود Schema
# =========================================================

from pyspark.sql.functions import split, col

df_split = df_lines.withColumn("cols", split(col("line"), ","))

df_columns = df_split.select(
    *[col("cols").getItem(i).alias(schema.fields[i].name) for i in range(49)]
)

print(f"✅ تم تطبيق Schema")
df_columns.cache()
print(f"📊 عدد السجلات: {df_columns.count()}")


# In[38]:


# =========================================================
# تنظيف القيم "-" و ""
# =========================================================

from pyspark.sql.functions import when, trim

df_clean = df_columns

for field in schema.fields:
    c = field.name
    df_clean = df_clean.withColumn(
        c,
        when(
            (col(c) == "-") | (trim(col(c)) == ""),
            None
        ).otherwise(trim(col(c)))
    )

print(f"✅ تم تنظيف القيم")


# In[39]:


# =========================================================
# تحويل الأنواع
# =========================================================

from pyspark.sql.types import IntegerType, DoubleType

int_cols = [
    "sport", "dsport", "sbytes", "dbytes", "sttl", "dttl",
    "sloss", "dloss", "Spkts", "Dpkts", "swin", "dwin",
    "stcpb", "dtcpb", "smeansz", "dmeansz", "trans_depth",
    "res_bdy_len", "Stime", "Ltime", "is_sm_ips_ports",
    "ct_state_ttl", "ct_flw_http_mthd", "is_ftp_login",
    "ct_ftp_cmd", "ct_srv_src", "ct_srv_dst", "ct_dst_ltm",
    "ct_src_ltm", "ct_src_dport_ltm", "ct_dst_sport_ltm",
    "ct_dst_src_ltm", "Label"
]

double_cols = [
    "dur", "Sload", "Dload", "Sjit", "Djit",
    "Sintpkt", "Dintpkt", "tcprtt", "synack", "ackdat"
]

for c in int_cols:
    df_clean = df_clean.withColumn(c, col(c).cast(IntegerType()))

for c in double_cols:
    df_clean = df_clean.withColumn(c, col(c).cast(DoubleType()))

print(f"✅ تم تحويل الأنواع")
df_clean.cache()
print(f"📊 عدد السجلات: {df_clean.count()}")


# In[42]:


# احفظ Parquet في /tmp (داخل الحاوية)
df_clean.coalesce(1).write.mode("overwrite").parquet("file:///tmp/unsw_cleaned.parquet")
print("✅ تم الحفظ في /tmp")


# In[ ]:




