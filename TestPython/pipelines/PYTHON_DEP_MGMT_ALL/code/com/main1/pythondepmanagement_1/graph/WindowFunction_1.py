from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from com.main1.pythondepmanagement_1.config.ConfigStore import *
from com.main1.pythondepmanagement_1.udfs.UDFs import *

def WindowFunction_1(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0\
        .withColumn(
          "c- short",
          expr(Config.c_row_number)\
            .over(Window\
            .partitionBy(col("`c- short`"), col("`c  - int`"), lit(Config.c_long_wf))\
            .orderBy(col("`c_float-__  `").asc(), expr(Config.c_wf_orderby_expr).desc()))
        )\
        .withColumn("c-string", row_number()\
        .over(Window\
        .partitionBy(col("`c- short`"), col("`c  - int`"), lit(Config.c_long_wf))\
        .orderBy(col("`c_float-__  `").asc(), expr(Config.c_wf_orderby_expr).desc())))
