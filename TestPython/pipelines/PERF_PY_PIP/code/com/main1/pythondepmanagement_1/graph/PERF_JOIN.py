from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from prophecy.transpiler import call_spark_fcn
from prophecy.transpiler.fixed_file_schema import *
from com.main1.pythondepmanagement_1.config.ConfigStore import *
from com.main1.pythondepmanagement_1.udfs.UDFs import *

def PERF_JOIN(spark: SparkSession, in0: DataFrame, in1: DataFrame, ) -> DataFrame:
    return in0\
        .alias("in0")\
        .join(in1.alias("in1"), (col("in0.c_long") == col("in1.c_long")), "inner")\
        .where(
          (
            ((col("in0.c_int") > lit(-10)) & (col("in1.c_decimal") > lit(-100)))
            & ~ col("in0.c_string").like("%asdasdrewasdasd%")
          )
        )\
        .select(col("in0.cmls_3ds_authntn_mthd").alias("first_name"), col("in1.c_short").alias("c_short"), col("in0.c_int").alias("c_int"), col("in0.c_decimal").alias("c_decimal"))
