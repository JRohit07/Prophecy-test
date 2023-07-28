from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from .config import *
from livy_python.udfs.UDFs import *

def Reformat_5_1(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(
        col("year"), 
        col("industry_code_ANZSIC"), 
        col("industry_name_ANZSIC"), 
        col("rme_size_grp"), 
        col("variable"), 
        col("value"), 
        col("unit"), 
        concat(lit(Config.c_string), lit(Config.c_int)).alias("c_config")
    )
