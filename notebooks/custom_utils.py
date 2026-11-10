from typing import List 
from pyspark.sql import DataFrame
from pyspark.sql.window import Window

class transformations:
    def dedup(self,df:DataFrame,dedup_cols:List,cdc:str):

        df = df.withColumn("dedupkey",concat(*dedup_cols))
        df = df.withColumn("dedupCounts",row_number().over(Window.partitionBy("dedupkey").orderBy(desc(cdc))))
        df = df.filter(col("dedupcounts")==1)
        df = df.drop("dedupkey","dedupcounts")
        return df
    
    def process_timestamp(self,df):
        df = df.withColumn("process_timestamp",current_timestamp())
        return df
    
    def upsert(self,df,key_cols,table,cdc):
        from pyspark.sql import DataFrame
from pyspark.sql.functions import (
    col, row_number, current_timestamp, desc
)
from pyspark.sql.window import Window
from delta.tables import DeltaTable


class Transformations:

    def dedup(self, df: DataFrame, dedup_cols: list, cdc: str):

        df = df.withColumn("dedupkey", concat(*dedup_cols))

        df = df.withColumn(
            "dedupCounts",
            row_number().over(
                Window.partitionBy("dedupkey").orderBy(desc(cdc))
            )
        )

        df = df.filter(col("dedupCounts") == 1)

        df = df.drop("dedupkey", "dedupCounts")

        return df

    def process_timestamp(self, df):

        df = df.withColumn(
            "process_timestamp",
            current_timestamp()
        )

        return df

    def upsert(self, df, key_cols, table, cdc):

        merge_condition = " AND ".join(
            [f"src.{i} = trg.{i}" for i in key_cols]
        )

        dlt_obj = DeltaTable.forName(
            spark,
            f"pyspark.silver.{table}"
        )

        (
            dlt_obj.alias("trg")
            .merge(df.alias("src"), merge_condition)
            .whenMatchedUpdateAll(
                condition=f"src.{cdc} >= trg.{cdc}"
            )
            .whenNotMatchedInsertAll()
            .execute()
        )

        return True               
