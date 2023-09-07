from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pythondoanything.config.ConfigStore import *
from pythondoanything.udfs.UDFs import *

def OrderBy_2(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.orderBy(col("c_short").asc(), col("c_int").desc(), lit(Config.c_expr_schematransform).asc())
