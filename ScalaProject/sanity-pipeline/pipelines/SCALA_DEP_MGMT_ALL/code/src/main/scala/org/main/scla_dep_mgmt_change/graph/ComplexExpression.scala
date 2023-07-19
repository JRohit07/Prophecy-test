package org.main.scla_dep_mgmt_change.graph

import io.prophecy.libs._
import org.main.scla_dep_mgmt_change.udfs.PipelineInitCode._
import org.main.scla_dep_mgmt_change.udfs.UDFs._
import org.main.scla_dep_mgmt_change.config.Context
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._

object ComplexExpression {

  def apply(context: Context, in: DataFrame): DataFrame =
    in.select(
      c1(context).as("c1"),
      concat(
        regexp_extract(lit("100-200"), "(d+)-(d+)", 1),
        regexp_replace(lit("100-200"), "(d+)",      "num"),
        repeat(lit("123"),             2),
        reverse(lit("Spark SQL")),
        rpad(lit("hi"), 5, "??"),
        rtrim(lit("  LQSa  ")),
        sha2(lit("Spark"),          256),
        substring(lit("Spark SQL"), 5, 2),
        trim(lit("    SparkSQL   ")),
        decode(encode(lit("abc"), "utf-8"), "utf-8"),
        format_string("Hello World %d %s", lit(100), lit("days")),
        lower(lit("SparkSql")),
        lpad(lit("hi"), 5, "??"),
        ltrim(lit("    SparkSQL   ")),
        hex(lit("Spark SQL")),
        md5(lit("Spark")),
        hash(lit("Spark"), array(lit(1.1d), lit(2.123d), lit(3.123d)), lit(2)),
        base64(col("c_string"))
      ).as("c2"),
      isnan(col("c_short").cast(DoubleType))
        .or(col("c_decimal").isNull)
        .or(col("c_string").like("%9%"))
        .or(
          (datediff(col("c_date"), col("c_timestamp")) + last_day(
            col("c_date")
          ) + dayofyear(col("c_date")) - dayofweek(col("c_date")) < date_sub(
            current_timestamp(),
            2
          )).or(array_contains(array(lit(1), lit(2), lit(3)), lit(2)))
            .or(
              array_contains(array(lit(10), lit(12), lit(13), lit(14), lit(15)),
                             lit(11)
              )
            )
        )
        .and(col("c_int") % lit(2) === lit(0))
        .as("c3"),
      when(col("c_int") % lit(11) === lit(0),
           sort_array(split(col("c_string"), "a"))
      ).when(col("c_int") % lit(9) === lit(0),
              sort_array(split(col("c_string"), "[#%]"))
        )
        .when(col("c_int") % lit(7) === lit(0), split(col("c_string"), "[@4]"))
        .when(col("c_int") % lit(5) === lit(0),
              sort_array(split(col("c_string"), "s"))
        )
        .otherwise(
          sort_array(array(lit("b"), lit("d"), lit("c"), lit("a")), true)
        )
        .as("c4"),
      date_add(from_unixtime(lit("2021-01-01 10:10:10"), "yyyy-MM-dd HH:mm:ss"),
               2
      ).as("c5"),
      when(col("c_int") > lit(10),
           when(!(!col("c_string").like("%1%")),               lit("A"))
             .when(!(trim(trim(col("c_string"))) =!= lit("")), lit("B"))
             .otherwise(lit("X"))
      ).when(col("c_int") <= lit(10),
              when(!(!col("c_string").like("%1%")),       lit("C"))
                .when(!(!(!col("c_string").like("%2%"))), lit("D"))
                .otherwise(lit("Z"))
        )
        .otherwise(lit(null))
        .as("c6"),
      c7(context).as("c7"),
      c8(context).as("c8"),
      udf_multiply(col("c_int")).as("c9_udf1"),
      (udf_string_null_safe(col("c_string")) * col("c_int")).as("c9_udf2"),
      expr(context.config.c_reformat_complex).as("c_10_config"),
      udf_divide_total(col("c_int")).as("c_11_udf_divide_total"),
      row_number()
        .over(Window.partitionBy(col("c_boolean")).orderBy(col("c_int").asc))
        .as("c_partition_expression")
    )

  def c1(context: Context) = {
    val spark  = context.spark
    val Config = context.config
    greatest(col("c_int"), lit(9), lit(2)) + floor(col("c_decimal")) + degrees(
      lit(3.141592653589793d)
    ) * exp(lit(2)) * expm1(lit(0)) + factorial(lit(5)) + format_number(
      lit(12332.123456d),
      4
    ) - instr(lit("SparkSQL"), "SQL") - length(lit("Spark SQL ")) - levenshtein(
      lit("kitten"),
      lit("sitting")
    ) + expr("log(10.0D, 100)") * log10(lit(10)) * log2(lit(2)) + locate(
      "bar",
      lit("foobarbar"),
      5
    ) - months_between(lit("1997-02-28 10:30:00"), lit("1996-10-30")) + nanvl(
      lit("NaN").cast(DoubleType),
      lit(123)
    ) + rand() - round(lit("2.5").cast(FloatType), 0) + sin(lit(0)) * sinh(
      lit(0)
    ) + size(array(lit(1), lit(2), lit(3))) + sqrt(lit(4)) + abs(
      lit(1.23d)
    ) + acos(lit(1)) - ascii(lit("2")) - asin(lit(0)) + bin(lit(13)) + lit("10")
      .cast(IntegerType) + cbrt(lit("27.0").cast(FloatType)) + ceil(
      lit(-2.1d)
    ) - coalesce(lit(null), lit(1), lit(null)) + conv(lit("100"), 2, 10) + year(
      lit("2016-07-30")
    ) + least(col("c_decimal"), col("c_int"), col("c_long"))
  }

  def c8(context: Context) = {
    val spark  = context.spark
    val Config = context.config
    greatest(col("c_int"), lit(9), lit(2)) + floor(col("c_decimal")) + degrees(
      lit(3.141592653589793d)
    ) * exp(lit(2)) * expm1(lit(0)) + factorial(lit(5)) + format_number(
      lit(12332.123456d),
      4
    ) - instr(lit("SparkSQL"), "SQL") - length(lit("Spark SQL ")) - levenshtein(
      lit("kitten"),
      lit("sitting")
    ) + expr("log(10.0D, 100)") * log10(lit(10)) * log2(lit(2)) + locate(
      "bar",
      lit("foobarbar"),
      5
    ) - months_between(lit("1997-02-28 10:30:00"), lit("1996-10-30")) + nanvl(
      lit("NaN").cast(DoubleType),
      lit(123)
    ) + rand() - round(lit("2.5").cast(FloatType), 0) + sin(lit(0)) * sinh(
      lit(0)
    ) + size(array(lit(1), lit(2), lit(3))) + sqrt(lit(4)) + abs(
      lit(1.23d)
    ) + acos(lit(1)) - ascii(lit("2")) - asin(lit(0)) + bin(lit(13)) + lit("10")
      .cast(IntegerType) + cbrt(lit("27.0").cast(FloatType)) + ceil(
      lit(-2.1d)
    ) - coalesce(lit(null), lit(1), lit(null)) + conv(lit("100"), 2, 10) + year(
      lit("2016-07-30")
    ) + least(col("c_decimal"), col("c_int"), col("c_long"))
  }

  def c7(context: Context) = {
    val spark  = context.spark
    val Config = context.config
    greatest(col("c_int"), lit(9), lit(2)) + floor(col("c_decimal")) + degrees(
      lit(3.141592653589793d)
    ) * exp(lit(2)) * expm1(lit(0)) + factorial(lit(5)) + format_number(
      lit(12332.123456d),
      4
    ) - instr(lit("SparkSQL"), "SQL") - length(lit("Spark SQL ")) - levenshtein(
      lit("kitten"),
      lit("sitting")
    ) + expr("log(10.0D, 100)") * log10(lit(10)) * log2(lit(2)) + locate(
      "bar",
      lit("foobarbar"),
      5
    ) - months_between(lit("1997-02-28 10:30:00"), lit("1996-10-30")) + nanvl(
      lit("NaN").cast(DoubleType),
      lit(123)
    ) + rand() - round(lit("2.5").cast(FloatType), 0) + sin(lit(0)) * sinh(
      lit(0)
    ) + size(array(lit(1), lit(2), lit(3))) + sqrt(lit(4)) + abs(
      lit(1.23d)
    ) + acos(lit(1)) - ascii(lit("2")) - asin(lit(0)) + bin(lit(13)) + lit("10")
      .cast(IntegerType) + cbrt(lit("27.0").cast(FloatType)) + ceil(
      lit(-2.1d)
    ) - coalesce(lit(null), lit(1), lit(null)) + conv(lit("100"), 2, 10) + year(
      lit("2016-07-30")
    ) + least(col("c_decimal"), col("c_int"), col("c_long"))
  }

}
