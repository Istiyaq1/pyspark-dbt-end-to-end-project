# Databricks notebook source
df = spark.read.format("csv")\
    .option("header", "true")\
    .option("inferSchema", "true")\
    .load("/Volumes/sparkdbt/source/source_data/customers/customers.csv")

# COMMAND ----------

# DBTITLE 1,Load and display customers data from volume


display(df)

# COMMAND ----------

schema_customers = df.schema
schema_customers

# COMMAND ----------

# MAGIC %md
# MAGIC ### **SPARK STREAMINMG**

# COMMAND ----------

entities = ['customers','trips','locations','payments','vehicles','drivers']

# COMMAND ----------

for entity in entities:

        df_batch = spark.read.format("csv")\
        .option("header",True)\
        .option("inferSchema",True)\
        .load(f"/Volumes/sparkdbt/source/source_data/{entity}/")

        schema_entity = df_batch.schema

        df = spark.readStream.format("csv")\
                .option("header",True)\
                .schema(schema_entity)\
                .load(f"/Volumes/sparkdbt/source/source_data/{entity}/")

        df.writeStream.format("delta")\
                .outputMode("append")\
                .option("checkpointLocation",f"/Volumes/sparkdbt/bronze/checkpoint/{entity}/")\
                .trigger(once=True)\
                .toTable(f"sparkdbt.bronze.{entity}")
                