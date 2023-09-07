from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from com.main1.pythondepmanagement_1.config.ConfigStore import *
from com.main1.pythondepmanagement_1.udfs.UDFs import *

def Deduplicate_1(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0\
        .withColumn(
          "row_number",
          row_number()\
            .over(Window\
            .partitionBy("c___-- string", "c-decimal")\
            .orderBy(concat(lit(Config.c_decimal), col("`c-int-column type`")).desc(), expr(Config.c_expr_deduplicate).desc()))
        )\
        .filter(col("row_number") == lit(1))\
        .drop("row_number")
