from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from com.main1.pythondepmanagement_1.config.ConfigStore import *
from com.main1.pythondepmanagement_1.udfs.UDFs import *

def Aggregate_1_1(spark: SparkSession, in0: DataFrame) -> DataFrame:
    df1 = in0.groupBy(lit(Config.c_aggregate_string).alias("`c___-- string`"), col("`c  date`"))
    df2 = df1.pivot("`-- c-long`", ["c_timestamp", "config_values"])

    return df2.agg(
        expr(Config.c_aggregate_expr).alias("c   short  --"), 
        first(col("`c-int-column type`")).alias("c-int-column type"), 
        first(col("`-- c-long`")).alias("-- c-long"), 
        first(col("`c-decimal renamed`")).alias("c-decimal renamed"), 
        first(col("`c  float`")).alias("c  float")
    )
