from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from python_unity_catalog.config.ConfigStore import *
from python_unity_catalog.udfs.UDFs import *

def WithUDFConfig(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(
        col("c_tinyint"), 
        col("c_smallint"), 
        col("c_int"), 
        col("c_bigint"), 
        col("c_float"), 
        col("c_double"), 
        col("c_string"), 
        col("c_boolean"), 
        col("c_array"), 
        col("c_struct"), 
        lit("2020-10-10").cast(DateType()).alias("c_date"), 
        lit("2020-10-10T10:10:10.10").cast(TimestampType()).alias("c_timestamp"), 
        concat(lit(Config.c_string), lit(Config.c_float)).alias("c_config")
    )
