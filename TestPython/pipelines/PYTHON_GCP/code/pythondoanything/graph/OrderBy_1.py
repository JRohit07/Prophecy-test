from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pythondoanything.config.ConfigStore import *
from pythondoanything.udfs.UDFs import *

def OrderBy_1(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.orderBy(
        col("`c- short`").asc(), 
        col("c_double").desc(), 
        concat(lit(Config.c_repartition_colname), col("`c  - int`")).asc()
    )
