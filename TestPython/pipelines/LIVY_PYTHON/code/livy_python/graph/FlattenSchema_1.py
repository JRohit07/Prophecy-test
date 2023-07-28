from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from livy_python.config.ConfigStore import *
from livy_python.udfs.UDFs import *

def FlattenSchema_1(spark: SparkSession, in0: DataFrame) -> DataFrame:
    flt_col = in0\
        .withColumn("a2", explode_outer("a2"))\
        .withColumn("a3", explode_outer("a3"))\
        .withColumn("a1", explode_outer("a1"))\
        .withColumn("s1-col2", explode_outer("s1.col2"))\
        .withColumn("s1-col1", explode_outer("s1.col1"))\
        .columns
    selectCols = [col("a1") if "a1" in flt_col else col("a1"),  col("a2") if "a2" in flt_col else col("a2"),                   col("a3") if "a3" in flt_col else col("a3"),                   col("s1-col2") if "s1-col2" in flt_col else col("s1.col2").alias("s1-col2"),                   col("s1-col1") if "s1-col1" in flt_col else col("s1.col1").alias("s1-col1"),                   col("year") if "year" in flt_col else col("year")]

    return in0\
        .withColumn("a2", explode_outer("a2"))\
        .withColumn("a3", explode_outer("a3"))\
        .withColumn("a1", explode_outer("a1"))\
        .withColumn("s1-col2", explode_outer("s1.col2"))\
        .withColumn("s1-col1", explode_outer("s1.col1"))\
        .select(*selectCols)
