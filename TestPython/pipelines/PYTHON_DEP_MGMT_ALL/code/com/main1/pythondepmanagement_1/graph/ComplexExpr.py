from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from com.main1.pythondepmanagement_1.config.ConfigStore import *
from com.main1.pythondepmanagement_1.udfs.UDFs import *

def ComplexExpr(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(
        expr(Config.EXPR_COMPLEX_DATES).alias("c1"), 
        (
          (
            (
              (
                (
                  (
                    (
                      (
                        (
                          (
                            (
                              (
                                (
                                  (
                                    (
                                      (
                                        (
                                          (
                                            (
                                              (
                                                (
                                                  (
                                                    (
                                                      (
                                                        (
                                                          (
                                                            (
                                                              (
                                                                greatest(col("c_int"), lit(9), lit(2))
                                                                + floor(
                                                                  col("c_decimal")
                                                                )
                                                              )
                                                              + (
                                                                (
                                                                  degrees(lit(3.141592653589793))
                                                                  * exp(
                                                                    lit(2)
                                                                  )
                                                                )
                                                                * expm1(
                                                                  lit(0)
                                                                )
                                                              )
                                                            )
                                                            + factorial(
                                                              lit(5)
                                                            )
                                                          )
                                                          + format_number(
                                                            lit(12332.123456), 
                                                            4
                                                          )
                                                        )
                                                        - instr(
                                                          lit("SparkSQL"), 
                                                          "SQL"
                                                        )
                                                      )
                                                      - length(
                                                        lit("Spark SQL ")
                                                      )
                                                    )
                                                    - levenshtein(
                                                      lit("kitten"), 
                                                      lit("sitting")
                                                    )
                                                  )
                                                  + (
                                                    (
                                                      expr("log(10.0D, 100)")
                                                      * log10(lit(10))
                                                    )
                                                    * log2(lit(2))
                                                  )
                                                )
                                                + locate(
                                                  "bar", 
                                                  lit("foobarbar"), 
                                                  5
                                                )
                                              )
                                              - months_between(
                                                lit("1997-02-28 10:30:00"), 
                                                lit("1996-10-30")
                                              )
                                            )
                                            + nanvl(
                                              lit("NaN").cast(DoubleType()), 
                                              lit(123)
                                            )
                                          )
                                          + rand()
                                        )
                                        + (lit(10) % lit(3))
                                      )
                                      - round(lit("2.5").cast(FloatType()), 0)
                                    )
                                    + (sin(lit(0)) * sinh(lit(0)))
                                  )
                                  + sqrt(lit(4))
                                )
                                + abs(lit(1.23))
                              )
                              + acos(lit(1))
                            )
                            - ascii(lit("2"))
                          )
                          - asin(lit(0))
                        )
                        + bin(lit(13))
                      )
                      + lit("10").cast(IntegerType())
                    )
                    + cbrt(lit("27.0").cast(FloatType()))
                  )
                  + ceil(lit(-2.1))
                )
                - coalesce(lit(None), lit(1), lit(None))
              )
              + conv(lit("100"), 2, 10)
            )
            + year(lit("2016-07-30"))
          )
          + least(col("c_decimal"), col("c_int"), col("c_long"))
        )\
          .alias(
          "c2"
        ), 
        concat(
            regexp_extract(lit("100-200"), "(d+)-(d+)", 1), 
            regexp_replace(lit("100-200"), "(d+)", "num"), 
            repeat(lit("123"), 2), 
            reverse(lit("Spark SQL")), 
            rpad(lit("hi"), 5, "??"), 
            rtrim(lit("LQSa")), 
            sha2(lit("Spark"), 256), 
            substring(lit("Spark SQL"), 5, 2), 
            trim(lit("    SparkSQL   ")), 
            decode(encode(lit("abc"), "utf-8"), "utf-8"), 
            format_string("Hello World %d %s", lit(100), lit("days")), 
            lower(lit("SparkSql")), 
            lpad(lit("hi"), 5, "??"), 
            ltrim(lit("    SparkSQL   ")), 
            hex(lit("Spark SQL")), 
            md5(lit("Spark")), 
            base64(col("c_string"))
          )\
          .alias("c3"), 
        (
          (((isnan(col("c_short").cast(DoubleType())) | col("c_decimal").isNull()) | col("c_string").like("%9%")) | ((((((datediff(col("c_date"), col("c_timestamp")) + last_day(col("c_date"))) + dayofyear(col("c_date"))) - dayofweek(col("c_date"))) < date_sub(current_timestamp(), 2)) | array_contains(array(lit(1), lit(2), lit(3)), lit(2))) | array_contains(array(lit(1), lit(2), lit(3)), lit(11))))
          & ((col("c_int") % lit(2)) == lit(0))
        )\
          .alias(
          "c4"
        ), 
        when(
            ((col("c_int") % lit(Config.c_int_11)) == lit(0)), 
            map_keys(create_map((lit(2) + col("c_int")), lit("a"), (lit(1) + col("c_int")), lit("b")))
          )\
          .when(
            ((col("c_int") % lit(9)) == lit(0)), 
            sort_array(
              split(
                col("c_string"), 
                "[#%]"
              )
            )
          )\
          .when(((col("c_int") % lit(7)) == lit(0)), split(col("c_string"), "[@4]"))\
          .when(((col("c_int") % lit(5)) == lit(0)), map_values(create_map(lit(1), lit("a"), lit(2), lit("b"))))\
          .otherwise(sort_array(array(lit("b"), lit("d"), lit("c"), lit("a")), True))\
          .alias("c5"), 
        when(
            (col("c_int") > lit(10)), 
            when(~ ~ col("c_string").like("%1%"), concat(col("c_string"), lit("A")))\
              .when(~ (trim(trim(col("c_string"))) != lit("")), concat(col("c_string"), lit("B")))\
              .otherwise(concat(col("c_string"), lit("X")))
          )\
          .when(
            (col("c_int") <= lit(10)), 
            when(~ ~ col("c_string").like("%1%"), concat(col("c_string"), lit("C")))\
              .when(~ ~ ~ col("c_string").like("%2%"), concat(col("c_string"), lit("D")))\
              .otherwise(concat(col("c_string"), lit("Z")))
          )\
          .otherwise(lit(None))\
          .alias("c6"), 
        udf_maptype().alias("c_udf_maptype"), 
        udf_arraytype(col("c_int"), lit(5)).alias("c_udf_array_type"), 
        expr(
            "named_struct('a', named_struct('test1', named_struct('test- another', 2)), 'b', named_struct('test1', named_struct('test- another', 2)))"
          )\
          .alias("c_struct.test1.mainstruct"), 
        col("c_short").alias("nested.field.col1"), 
        col("c_int").alias("nested.field.col2"), 
        row_number().over(Window.partitionBy(col("c_boolean")).orderBy(col("c_int").asc())).alias("c_partition_by")
    )
