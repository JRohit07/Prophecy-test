from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from .config import *
from livy_python.udfs.UDFs import *

def OrderBy_1_1(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.orderBy(
        col("year").asc(), 
        col("industry_code_ANZSIC").asc(), 
        col("industry_name_ANZSIC").asc(), 
        col("rme_size_grp").asc(), 
        col("variable").asc(), 
        col("value").asc(), 
        col("unit").asc()
    )
