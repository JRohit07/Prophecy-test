from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from python_unity_catalog.config.ConfigStore import *
from python_unity_catalog.udfs.UDFs import *

def ComplexExprReformat(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(
        substring(col("c_string"), 1, 2).alias("c1"), 
        expr(Config.c_spark_expression).alias("c2"), 
        expr("qa_mask_zip_code(c_string)").alias("c3"), 
        expr("named_struct('a', 'test', 'b', 2, 'c', 3)").alias("c4"), 
        expr(Config.EXPR_COMPLEX_DATES).alias("c5"), 
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
          .alias("c7"), 
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
          .alias("c9"), 
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
          .alias("c10"), 
        (
          (((isnan(col("c_short").cast(DoubleType())) | col("c_decimal").isNull()) | col("c_string").like("%9%")) | ((((((datediff(col("c_date"), col("c_timestamp")) + last_day(col("c_date"))) + dayofyear(col("c_date"))) - dayofweek(col("c_date"))) < date_sub(current_timestamp(), 2)) | array_contains(array(lit(1), lit(2), lit(3)), lit(2))) | array_contains(array(lit(1), lit(2), lit(3)), lit(11))))
          & ((col("c_int") % lit(2)) == lit(0))
        )\
          .alias(
          "c11"
        ), 
        concat(
            col("c_tinyint"), 
            lit(Config.c_string), 
            lit(Config.c_boolean), 
            lit(Config.c_array[0].car_string), 
            lit(Config.c_record.cr_int)
          )\
          .alias("c12")
    )
