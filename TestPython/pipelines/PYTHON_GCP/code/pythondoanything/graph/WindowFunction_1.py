from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pythondoanything.config.ConfigStore import *
from pythondoanything.udfs.UDFs import *

def WindowFunction_1(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0\
        .withColumn(
          "c -  boolean _  ",
          expr(Config.c_row_number)\
            .over(Window\
            .partitionBy(col("`c- short`"), lit(Config.c_int_name))\
            .orderBy(col("`- c long`").asc(), col("`c_decimal  -  `").asc(), lit(Config.c_repartition_expr).desc())\
            .rowsBetween(Window.unboundedPreceding, Window.currentRow))
        )\
        .withColumn(
          "c_date-for today",
          row_number()\
            .over(Window\
            .partitionBy(col("`c- short`"), lit(Config.c_int_name))\
            .orderBy(col("`- c long`").asc(), col("`c_decimal  -  `").asc(), lit(Config.c_repartition_expr).desc())\
            .rowsBetween(Window.unboundedPreceding, Window.currentRow))
        )\
        .withColumn("c_timestamp  __ for--today", expr(Config.c_row_number)\
        .over(Window\
        .partitionBy(col("`c- short`"), lit(Config.c_int_name))\
        .orderBy(col("`- c long`").asc(), col("`c_decimal  -  `").asc(), lit(Config.c_repartition_expr).desc())\
        .rowsBetween(Window.unboundedPreceding, Window.currentRow)))
