from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from python_unity_catalog.config.ConfigStore import *
from python_unity_catalog.udfs.UDFs import *

def SQLStatement_1_1(spark: SparkSession, in0: DataFrame, input1: DataFrame) -> (DataFrame, DataFrame):
    in0.createOrReplaceTempView("in0")
    input1.createOrReplaceTempView("input1")
    df1 = spark.sql("select * from in0")
    df2 = spark.sql("select * from input1")

    return df1, df2
