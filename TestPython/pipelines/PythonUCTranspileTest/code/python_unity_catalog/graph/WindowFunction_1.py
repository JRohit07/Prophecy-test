from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from python_unity_catalog.config.ConfigStore import *
from python_unity_catalog.udfs.UDFs import *

def WindowFunction_1(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.withColumn(
        "lastname",
        row_number().over(Window.partitionBy(col("firstname")).orderBy(col("middlename").asc()))
    )
