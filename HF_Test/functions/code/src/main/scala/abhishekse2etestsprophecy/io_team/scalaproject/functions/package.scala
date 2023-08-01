package abhishekse2etestsprophecy.io_team.scalaproject

import org.apache.spark.sql._
package object functions {
  val udf_string_null_safe = Udf_string_null_safe.udf_string_null_safe
  val udf_multiply         = Udf_multiply.udf_multiply
  val udf_string_length    = Udf_string_length.udf_string_length
  val udf_random_number    = Udf_random_number.udf_random_number
  val udf_add_one          = Udf_add_one.udf_add_one
  val udf_concat           = Udf_concat.udf_concat
  val udf_divide_total     = Udf_divide_total.udf_divide_total
  val udf_string_length5   = Udf_string_length5.udf_string_length5
  val udf_string_length6   = Udf_string_length6.udf_string_length6
  val udf_string_length7   = Udf_string_length7.udf_string_length7
  val udf_string_length8   = Udf_string_length8.udf_string_length8
  val udf_string_length9   = Udf_string_length9.udf_string_length9
  val udf_string_length10  = Udf_string_length10.udf_string_length10
  val udf_complex_window   = Udf_complex_window.udf_complex_window
  val udf1                 = Udf1.udf1

  def registerFunctions(spark: SparkSession) = {
    spark.udf.register("udf_string_null_safe", udf_string_null_safe)
    spark.udf.register("udf_multiply",         udf_multiply)
    spark.udf.register("udf_string_length",    udf_string_length)
    spark.udf.register("udf_random_number",    udf_random_number)
    spark.udf.register("udf_add_one",          udf_add_one)
    spark.udf.register("udf_concat",           udf_concat)
    spark.udf.register("udf_divide_total",     udf_divide_total)
    spark.udf.register("udf_string_length5",   udf_string_length5)
    spark.udf.register("udf_string_length6",   udf_string_length6)
    spark.udf.register("udf_string_length7",   udf_string_length7)
    spark.udf.register("udf_string_length8",   udf_string_length8)
    spark.udf.register("udf_string_length9",   udf_string_length9)
    spark.udf.register("udf_string_length10",  udf_string_length10)
    spark.udf.register("udf_complex_window",   udf_complex_window)
    spark.udf.register("udf1",                 udf1)
  }

}
