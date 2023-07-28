from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from prophecy.transpiler import call_spark_fcn
from prophecy.transpiler.fixed_file_schema import *
from .config import *
from com.main1.pythondepmanagement_1.udfs.UDFs import *

def Join_1(spark: SparkSession, in0: DataFrame, in1: DataFrame, ) -> DataFrame:
    return in0\
        .alias("in0")\
        .join(in1.alias("in1"), (col("in0.cmls_3ds_authntn_mthd") == col("in1.cmls_3ds_authntn_mthd")), "inner")\
        .select(*[concat(col("in0.cmls_3ds_authntn_mthd"), col("in1.c_timestamp")).alias("c_concat_col")], col("in0.*"))
