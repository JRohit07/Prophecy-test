from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from com.main1.pythondepmanagement_1.config.ConfigStore import *
from com.main1.pythondepmanagement_1.udfs.UDFs import *

def dest_delta_scdmerge_main(spark: SparkSession, in0: DataFrame):
    from delta.tables import DeltaTable, DeltaMergeBuilder

    if (
        DeltaTable.isDeltaTable(spark, "dbfs:/tmp/e2e/234234/dest_delta1_test_scd2")
        and spark._jvm.org.apache.hadoop.fs.FileSystem\
          .get(spark._jsc.hadoopConfiguration())\
          .exists(spark._jvm.org.apache.hadoop.fs.Path("dbfs:/tmp/e2e/234234/dest_delta1_test_scd2"))
    ):
        updatesDF = in0.withColumn("c_boolean", lit("true")).withColumn("c_boolean", lit("true"))
        updateColumns = updatesDF.columns
        existingTable = DeltaTable.forPath(spark, "dbfs:/tmp/e2e/234234/dest_delta1_test_scd2")
        existingDF = existingTable.toDF()
        stagedUpdatesDF = updatesDF\
                              .join(existingDF, ["c_int"])\
                              .where(
                                (
                                  (existingDF["c_boolean"] == lit("true"))
                                  & (~ (existingDF["c_long"]).eqNullSafe(
                                    updatesDF["c_long"]
                                  ))
                                )
                              )\
                              .select(*[updatesDF[val] for val in updateColumns])\
                              .withColumn("c_boolean", lit("false"))\
                              .withColumn("mergeKey", lit(None))\
                              .union(updatesDF.withColumn("mergeKey", concat("c_int")))
        existingTable\
            .alias("existingTable")\
            .merge(stagedUpdatesDF.alias("staged_updates"), concat(existingDF["c_int"]) == stagedUpdatesDF["mergeKey"])\
            .whenMatchedUpdate(
              condition = (
                (existingDF["c_boolean"] == lit("true"))
                & (~ (existingDF["c_long"]).eqNullSafe(stagedUpdatesDF["c_long"]))
              ),
              set = {
"c_boolean" : "false", "c_struct.c_timestamp" : "staged_updates.c_struct.c_date"}
            )\
            .whenNotMatchedInsertAll()\
            .execute()
    else:
        in0.write.format("delta").mode("overwrite").save("dbfs:/tmp/e2e/234234/dest_delta1_test_scd2")
