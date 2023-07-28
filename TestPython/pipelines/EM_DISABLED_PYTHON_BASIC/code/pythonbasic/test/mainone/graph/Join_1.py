from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pythonbasic.test.mainone.config.ConfigStore import *
from pythonbasic.test.mainone.udfs.UDFs import *

def Join_1(spark: SparkSession, in0: DataFrame, in1: DataFrame, ) -> DataFrame:
    return in0\
        .alias("in0")\
        .join(in1.alias("in1"), (col("in0.`c-int-column type`") != col("in1.`c   short  --`")), "inner")\
        .select(col("in0.`c   short  --`").alias("c   short  --"), col("in0.`c-int-column type`").alias("c-int-column type"), col("in0.`-- c-long`").alias("-- c-long"), col("in1.`c-decimal`").alias("c-decimal"), col("in0.`c  float`").alias("c  float"), col("in0.`c--boolean`").alias("c--boolean"), col("in0.`c- - -double`").alias("c- - -double"), col("in0.`c___-- string`").alias("c___-- string"), col("in0.`c  date`").alias("c  date"), col("in0.c_timestamp").alias("c_timestamp"))
