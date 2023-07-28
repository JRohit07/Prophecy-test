from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from python_subs_disabled.config.ConfigStore import *
from python_subs_disabled.udfs.UDFs import *

def dummy_delta_merge(spark: SparkSession, in0: DataFrame):
    from delta.tables import DeltaTable, DeltaMergeBuilder

    if DeltaTable.isDeltaTable(spark, "dbfs:/tmp/e2e/random12345/dest_summy_delta"):
        DeltaTable\
            .forPath(spark, "dbfs:/tmp/e2e/random12345/dest_summy_delta")\
            .alias("target")\
            .merge(in0.alias("source"), (col("source.c_int") == col("target.c_int")))\
            .whenMatchedUpdateAll(condition = (col("source.c_double") > lit(10)))\
            .whenNotMatchedInsertAll()\
            .execute()
    else:
        in0.write.format("delta").mode("overwrite").save("dbfs:/tmp/e2e/random12345/dest_summy_delta")
