from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from perf_unitest_generate.config.ConfigStore import *
from perf_unitest_generate.udfs.UDFs import *

def SetOperation_1(spark: SparkSession, in0: DataFrame, in1: DataFrame, ) -> DataFrame:
    return in0.unionAll(in1)
