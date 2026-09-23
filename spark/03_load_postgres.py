#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pyspark.sql import SparkSession
import os
print("✅ Imports OK")


# In[2]:


spark = SparkSession.builder     .appName("UNSW-NB15-PostgreSQL")     .config("spark.jars", "/home/itversity/.ivy2/jars/org.postgresql_postgresql-42.6.0.jar")     .config("spark.driver.memory", "2g")     .getOrCreate()

spark.sparkContext.setLogLevel("WARN")
print(f"✅ Spark version: {spark.version}")


# In[3]:


# =========================================================
# Load Parquet
# =========================================================

PARQUET_PATH = "file:///tmp/unsw_cleaned.parquet"

df = spark.read.parquet(PARQUET_PATH)
df.cache()

print(f"✅ Records: {df.count():,}")
print(f"✅ Columns: {len(df.columns)}")


# In[4]:


# =========================================================
# Test PostgreSQL Connection
# =========================================================

PG_URL = "jdbc:postgresql://dockerfilespark-cluster_util_db-1:5432/postgres"
PG_USER = "postgres"
PG_PASSWORD = "itversity"

print(f"📌 URL: {PG_URL}")

try:
    test_df = spark.read         .format("jdbc")         .option("url", PG_URL)         .option("user", PG_USER)         .option("password", PG_PASSWORD)         .option("driver", "org.postgresql.Driver")         .option("query", "SELECT version()")         .load()
    
    test_df.show(truncate=False)
    print("✅ الاتصال ناجح!")
    
except Exception as e:
    print(f"❌ فشل: {e}")


# In[5]:


# =========================================================
# Load 2.5M records to PostgreSQL
# =========================================================

PG_URL = "jdbc:postgresql://dockerfilespark-cluster_util_db-1:5432/postgres"
PG_USER = "postgres"
PG_PASSWORD = "itversity"
PG_TABLE = "unsw_nb15"

print(f"⏳ جاري تحميل {df.count():,} سطر...")
print(f"⏱️ الوقت المتوقع: 5-15 دقيقة")

df.write     .format("jdbc")     .option("url", PG_URL)     .option("dbtable", PG_TABLE)     .option("user", PG_USER)     .option("password", PG_PASSWORD)     .option("driver", "org.postgresql.Driver")     .option("batchsize", "10000")     .option("truncate", "true")     .mode("append")     .save()

print("✅ تم التحميل!")


# In[ ]:




