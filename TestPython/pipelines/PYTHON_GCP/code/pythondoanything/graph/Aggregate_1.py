from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pythondoanything.config.ConfigStore import *
from pythondoanything.udfs.UDFs import *

def Aggregate_1(spark: SparkSession, in0: DataFrame) -> DataFrame:
    df1 = in0.groupBy(col("`c -  boolean _  `"), lit(Config.c_date_for_today).alias("`c_date-for today`"))
    df2 = df1.pivot("`c- short`", ["`- c long`", "'$c_float_name'"])

    return df2.agg(first(col("`c- short`")).alias("c- short"), expr(Config.c_agg_expr).alias("c  - int"))
