from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from python_subs_disabled.config.ConfigStore import *
from python_subs_disabled.udfs.UDFs import *

def dummy_dest_delta_merge_scd(spark: SparkSession, in0: DataFrame):
    from delta.tables import DeltaTable, DeltaMergeBuilder

    if DeltaTable.isDeltaTable(spark, "dbfs:/tmp/e2e/random1233/dest_dummy_delta_scd2"):
        updatesDF = in0.withColumn("c_boolean", lit("true")).withColumn("c_boolean", lit("true"))
        existingTable = DeltaTable.forPath(spark, "dbfs:/tmp/e2e/random1233/dest_dummy_delta_scd2")
        existingDF = existingTable.toDF()
        cond = None
        scdHistoricColumns = ["c_long"]

        for scdCol in scdHistoricColumns:
            if cond is None:
                cond = (existingDF[scdCol] != updatesDF[scdCol])
            else:
                cond = (cond | (existingDF[scdCol] != updatesDF[scdCol]))

        updateColumns = updatesDF.columns
        rowsToUpdate = updatesDF\
                           .join(existingDF, ["c_int"])\
                           .where((existingDF["c_boolean"] == lit("true")) & (cond))\
                           .select(*[updatesDF[val] for val in updateColumns])\
                           .withColumn("c_boolean", lit("false"))
        stagedUpdatesDF = rowsToUpdate\
                              .withColumn("mergeKey", lit(None))\
                              .union(updatesDF.withColumn("mergeKey", concat("c_int")))
        updateCond = None

        for scdCol in scdHistoricColumns:
            if updateCond is None:
                updateCond = (existingDF[scdCol] != stagedUpdatesDF[scdCol])
            else:
                updateCond = (updateCond | (existingDF[scdCol] != stagedUpdatesDF[scdCol]))

        existingTable\
            .alias("existingTable")\
            .merge(stagedUpdatesDF.alias("staged_updates"), concat(existingDF["c_int"]) == stagedUpdatesDF["mergeKey"])\
            .whenMatchedUpdate(
              condition = (existingDF["c_boolean"] == lit("true")) & updateCond,
              set = {
"c_boolean" : "false", "c_date" : "staged_updates.c_date"}
            )\
            .whenNotMatchedInsertAll()\
            .execute()
    else:
        in0.write.format("delta").mode("overwrite").save("dbfs:/tmp/e2e/random1233/dest_dummy_delta_scd2")
