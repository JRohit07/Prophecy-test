from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from com.main1.pythondepmanagement_1.config.ConfigStore import *
from com.main1.pythondepmanagement_1.udfs.UDFs import *

def VeryLargeExpr(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(
        col("account_flags"), 
        col("account_open_date"), 
        col("country_code"), 
        col("customer_id"), 
        col("email"), 
        col("first_name"), 
        col("last_name"), 
        col("phone"), 
        when(
            ~ when(
                coalesce(
                  (
                    (((length(col("first_name").cast(StringType())) == lit(8)) & (length(col("first_name").cast(StringType())) == lit(8))) & ((length(col("first_name").cast(StringType())) == lit(8)) & (length(col("first_name").cast(StringType())) == lit(8))))
                    & (
                      ((~ when((length(trim(col("first_name").cast(StringType()))) == lit(8)), date_format(to_date(trim(col("first_name").cast(StringType())), "yyyyMMdd"), "yyyyMMdd")).isNull() == lit(10)) & (~ when((length(trim(col("first_name").cast(StringType()))) == lit(8)), date_format(to_date(trim(col("first_name").cast(StringType())), "yyyyMMdd"), "yyyyMMdd")).isNull() == lit(10)))
                      & (
                        ~ when((length(trim(col("first_name").cast(StringType()))) == lit(8)), date_format(to_date(trim(col("first_name").cast(StringType())), "yyyyMMdd"), "yyyyMMdd")).isNull()
                        == lit(10)
                      )
                    )
                  ), 
                  lit(0).cast(BooleanType())
                ), 
                lit(1).cast(BooleanType())
              )\
              .when(
                coalesce(
                  (
                    (array_contains(array(lit(6), lit(7)), length(col("first_name").cast(StringType()))) & array_contains(array(lit(6), lit(7)), length(col("first_name").cast(StringType()))))
                    & (
                      ~ when((length(trim((lit(19000000) + col("first_name").cast(DecimalType(9, 0))).cast(StringType()))) == lit(8)), date_format(to_date(trim((lit(19000000) + col("first_name").cast(DecimalType(9, 0))).cast(StringType())), "yyyyMMdd"), "yyyyMMdd")).isNull()
                      == lit(1)
                    )
                  ), 
                  lit(0).cast(BooleanType())
                ), 
                lit(1).cast(BooleanType())
              )\
              .otherwise(lit(0).cast(BooleanType()))\
              .cast(BooleanType()), 
            date_format(to_timestamp(lit(Config.AI_MIN_DATETIME), "yyyy-MM-dd HH:mm:ss"), "yyyyMMdd")
          )\
          .when(
            coalesce(
              (
                (length(col("first_name").cast(StringType())) == lit(8))
                & (
                  ~ when((length(trim(col("first_name").cast(StringType()))) == lit(8)), date_format(to_date(trim(col("first_name").cast(StringType())), "yyyyMMdd"), "yyyyMMdd")).isNull()
                  == lit(1)
                )
              ), 
              lit(0).cast(BooleanType())
            ), 
            col("first_name").cast(StringType())
          )\
          .when(
            coalesce(
              (
                array_contains(array(lit(6), lit(7)), length(col("first_name").cast(StringType())))
                & (
                  ~ when((length(trim((lit(19000000) + col("first_name").cast(DecimalType(9, 0))).cast(StringType()))) == lit(8)), date_format(to_date(trim((lit(19000000) + col("first_name").cast(DecimalType(9, 0))).cast(StringType())), "yyyyMMdd"), "yyyyMMdd")).isNull()
                  == lit(1)
                )
              ), 
              lit(0).cast(BooleanType())
            ), 
            (lit(19000000) + col("first_name").cast(DecimalType(9, 0))).cast(StringType())
          )\
          .otherwise(lit(None))\
          .alias("c_complex_expression")
    )
