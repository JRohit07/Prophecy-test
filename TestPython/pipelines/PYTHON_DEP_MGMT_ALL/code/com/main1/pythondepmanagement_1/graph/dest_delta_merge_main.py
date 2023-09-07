from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from com.main1.pythondepmanagement_1.config.ConfigStore import *
from com.main1.pythondepmanagement_1.udfs.UDFs import *

def dest_delta_merge_main(spark: SparkSession, in0: DataFrame):
    from delta.tables import DeltaTable, DeltaMergeBuilder

    if (
        DeltaTable.isDeltaTable(spark, "dbfs:/tmp/e2e/234324/dest_delta_1mergemain123")
        and spark._jvm.org.apache.hadoop.fs.FileSystem\
          .get(spark._jsc.hadoopConfiguration())\
          .exists(spark._jvm.org.apache.hadoop.fs.Path("dbfs:/tmp/e2e/234324/dest_delta_1mergemain123"))
    ):
        matched_expr = {}
        matched_expr["c_string"] = concat(col("source.c_string"), col("source.c_int"))
        DeltaTable\
            .forPath(spark, "dbfs:/tmp/e2e/234324/dest_delta_1mergemain123")\
            .alias("target")\
            .merge(in0.alias("source"), (col("source.c_increasing") == col("target.c_increasing")))\
            .whenMatchedUpdate(condition = (col("source.c_int") == lit(35)), set = matched_expr)\
            .whenNotMatchedInsertAll()\
            .execute()
    else:
        in0.write.format("delta").mode("overwrite").save("dbfs:/tmp/e2e/234324/dest_delta_1mergemain123")
