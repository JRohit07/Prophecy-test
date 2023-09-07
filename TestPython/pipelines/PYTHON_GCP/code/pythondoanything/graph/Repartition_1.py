from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pythondoanything.config.ConfigStore import *
from pythondoanything.udfs.UDFs import *

def Repartition_1(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.repartition(
        10,
        expr(Config.c_repartition_expr), 
        concat(lit(Config.c_repartition_colname), col("`c  float`"), col("`c   short  --`"))
    )
