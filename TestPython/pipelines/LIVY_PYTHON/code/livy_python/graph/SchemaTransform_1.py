from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from livy_python.config.ConfigStore import *
from livy_python.udfs.UDFs import *

def SchemaTransform_1(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.withColumn("indus_concat", expr(Config.c_st_expr)).drop("unit").withColumnRenamed("value", "value_new")
