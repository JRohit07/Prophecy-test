from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pythondoanything.config.ConfigStore import *
from pythondoanything.udfs.UDFs import *

def Join_1(spark: SparkSession, in0: DataFrame, in1: DataFrame, ) -> DataFrame:
    return in0\
        .alias("in0")\
        .join(in1.alias("in1"), expr(Config.c_join_condition), "inner")\
        .where((col("in0.`c  float`") < lit(Config.c_int)))\
        .select(col("in0.`c   short  --`").alias("c   short  --"), col("in0.`c-int-column type`").alias("c-int-column type"), col("in0.`-- c-long`").alias("-- c-long"), col("in0.`c-decimal`").alias("c-decimal"), col("in0.`c  float`").alias("c  float"), col("in0.`c--boolean`").alias("c--boolean"), col("in0.`c- - -double`").alias("c- - -double"), col("in0.`c___-- string`").alias("c___-- string"), col("in0.`c  date`").alias("c  date"), col("in0.c_timestamp").alias("c_timestamp"), concat(
          col("in0.`c  float`"), 
          lit(Config.c_boolean), 
          lit(" :: "), 
          lit(Config.c_double), 
          lit(" :: "), 
          lit(Config.c_float), 
          lit(" :: "), 
          lit(Config.c_int), 
          lit(" :: "), 
          lit(Config.c_long), 
          lit(" :: "), 
          lit(Config.c_short), 
          lit(" :: "), 
          lit(Config.c_string1)
        )\
        .alias("c_new_col"))
