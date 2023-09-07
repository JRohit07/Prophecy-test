from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from pythonorganization.donot.openme12.config.ConfigStore import *
from pythonorganization.donot.openme12.udfs.UDFs import *

def Join_3(spark: SparkSession, in0: DataFrame, in1: DataFrame, ) -> DataFrame:
    return in0\
        .alias("in0")\
        .join(in1.alias("in1"), (col("in0.`c  - int`") != col("in1.c_int")), "inner")\
        .select(col("in0.`c- short`").alias("c- short"), col("in0.`c  - int`").alias("c  - int"), col("in1.c_short").alias("c_short"), col("in1.c_int").alias("c_int"))
