from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from python_subs_disabled.config.ConfigStore import *
from python_subs_disabled.udfs.UDFs import *

def dummy_catalog_delta(spark: SparkSession, in0: DataFrame):
    if spark.catalog._jcatalog.tableExists(f"qa_database.testination_1"):
        from delta.tables import DeltaTable, DeltaMergeBuilder
        DeltaTable\
            .forName(spark, f"qa_database.testination_1")\
            .alias("target")\
            .merge(in0.alias("source"), (col("source.c_int") == col("target.c_int")))\
            .whenMatchedUpdateAll(condition = (col("source.c_float") > lit(10)))\
            .whenNotMatchedInsertAll()\
            .execute()
    else:
        in0.write.format("delta").mode("overwrite").saveAsTable(f"qa_database.testination_1")
