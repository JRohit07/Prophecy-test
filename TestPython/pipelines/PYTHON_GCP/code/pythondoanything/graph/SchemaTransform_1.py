from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pythondoanything.config.ConfigStore import *
from pythondoanything.udfs.UDFs import *

def SchemaTransform_1(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0\
        .withColumn("c_int_short", expr(Config.c_expr_schematransform))\
        .drop(Config.c_colnamedrop_schematransform)\
        .withColumnRenamed("c_date-for today", Config.c_colname_schematransform)
