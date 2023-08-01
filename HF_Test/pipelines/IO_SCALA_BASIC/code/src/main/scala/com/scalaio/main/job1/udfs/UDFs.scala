package com.scalaio.main.job1.udfs

import _root_.io.prophecy.abinitio.ScalaFunctions._
import _root_.io.prophecy.libs._
import org.apache.spark.sql.types._
import org.apache.spark.sql.functions._
import org.apache.spark.sql._

object UDFs extends Serializable {

  def registerUDFs(spark: SparkSession) = {
    spark.udf.register("udf_string_null_safe", udf_string_null_safe)
    spark.udf.register("udf_multiply",         udf_multiply)
    spark.udf.register("udf_string_length",    udf_string_length)
    spark.udf.register("udf_random_number",    udf_random_number)
    spark.udf.register("udf_add_one",          udf_add_one)
    spark.udf.register("udf_divide_total",     udf_divide_total)
    spark.udf.register("udf_string_length6",   udf_string_length6)
    spark.udf.register("udf_string_length7",   udf_string_length7)
    spark.udf.register("udf_string_length9",   udf_string_length9)
    spark.udf.register("udf_string_length10",  udf_string_length10)
    spark.udf.register("udf_complex_window",   udf_complex_window)
    spark.udf.register("udf1",                 udf1)
    spark.udf.register("udf_matrix_test",      udf_matrix_test)
    spark.udf.register("udf_matrices_test",    udf_matrices_test)
    spark.udf.register("udf_vectors_test",     udf_vectors_test)
    registerAllUDFs(spark)
  }

  def udf_string_null_safe = {
    import org.apache.spark.sql.expressions.Window
    import org.apache.spark.sql.functions._
    var int_value    = 10
    var string_value = "string value"
    val colors =
      Map("red" -> "#FF0000", "azure" -> "#F0FFFF", "peru" -> "#CD853F")
    val nums: Map[Int, Int] = Map()
    val fruit = Set("apples", "oranges", "pears")
    val t     = (4, 3, 2, 1)
    val sum   = t._1 + t._2 + t._3 + t._4
    val ita   = Iterator(20, 40, 2, 50, 69, 90)
    val itb   = Iterator(20, 40, 2, 50, 69, 90)
    udf((s: String) => if (s != null) s.length else string_value.length)
  }

  def udf_multiply = {
    import org.apache.spark.sql.expressions.Window
    import org.apache.spark.sql.functions._
    var int_value    = 10
    var string_value = "string value"
    val colors =
      Map("red" -> "#FF0000", "azure" -> "#F0FFFF", "peru" -> "#CD853F")
    val nums: Map[Int, Int] = Map()
    val fruit = Set("apples", "oranges", "pears")
    val t     = (4, 3, 2, 1)
    val sum   = t._1 + t._2 + t._3 + t._4
    val ita   = Iterator(20, 40, 2, 50, 69, 90)
    val itb   = Iterator(20, 40, 2, 50, 69, 90)
    udf((value: Int) => value * int_value)
  }

  def udf_string_length = {
    import org.apache.spark.sql.expressions.Window
    import org.apache.spark.sql.functions._
    var int_value    = 10
    var string_value = "string value"
    val colors =
      Map("red" -> "#FF0000", "azure" -> "#F0FFFF", "peru" -> "#CD853F")
    val nums: Map[Int, Int] = Map()
    val fruit = Set("apples", "oranges", "pears")
    val t     = (4, 3, 2, 1)
    val sum   = t._1 + t._2 + t._3 + t._4
    val ita   = Iterator(20, 40, 2, 50, 69, 90)
    val itb   = Iterator(20, 40, 2, 50, 69, 90)
    udf((s: String) => s.length)
  }

  def udf_random_number = {
    import org.apache.spark.sql.expressions.Window
    import org.apache.spark.sql.functions._
    var int_value    = 10
    var string_value = "string value"
    val colors =
      Map("red" -> "#FF0000", "azure" -> "#F0FFFF", "peru" -> "#CD853F")
    val nums: Map[Int, Int] = Map()
    val fruit = Set("apples", "oranges", "pears")
    val t     = (4, 3, 2, 1)
    val sum   = t._1 + t._2 + t._3 + t._4
    val ita   = Iterator(20, 40, 2, 50, 69, 90)
    val itb   = Iterator(20, 40, 2, 50, 69, 90)
    udf(() => Math.random())
  }

  def udf_add_one = {
    import org.apache.spark.sql.expressions.Window
    import org.apache.spark.sql.functions._
    var int_value    = 10
    var string_value = "string value"
    val colors =
      Map("red" -> "#FF0000", "azure" -> "#F0FFFF", "peru" -> "#CD853F")
    val nums: Map[Int, Int] = Map()
    val fruit = Set("apples", "oranges", "pears")
    val t     = (4, 3, 2, 1)
    val sum   = t._1 + t._2 + t._3 + t._4
    val ita   = Iterator(20, 40, 2, 50, 69, 90)
    val itb   = Iterator(20, 40, 2, 50, 69, 90)
    udf((x: Int) => x)
  }

  def udf_divide_total = {
    import org.apache.spark.sql.expressions.Window
    import org.apache.spark.sql.functions._
    var int_value    = 10
    var string_value = "string value"
    val colors =
      Map("red" -> "#FF0000", "azure" -> "#F0FFFF", "peru" -> "#CD853F")
    val nums: Map[Int, Int] = Map()
    val fruit = Set("apples", "oranges", "pears")
    val t     = (4, 3, 2, 1)
    val sum   = t._1 + t._2 + t._3 + t._4
    val ita   = Iterator(20, 40, 2, 50, 69, 90)
    val itb   = Iterator(20, 40, 2, 50, 69, 90)
    udf { (value: Int) =>
      var myList = Array(1.9d, 2.9d, 3.4d, 3.5d)
      var total  = 0.0d
      for (i <- 0 to myList.length - 1)
        total += myList(i)
      total / value
    }
  }

  def udf_string_length6 = {
    import org.apache.spark.sql.expressions.Window
    import org.apache.spark.sql.functions._
    var int_value    = 10
    var string_value = "string value"
    val colors =
      Map("red" -> "#FF0000", "azure" -> "#F0FFFF", "peru" -> "#CD853F")
    val nums: Map[Int, Int] = Map()
    val fruit = Set("apples", "oranges", "pears")
    val t     = (4, 3, 2, 1)
    val sum   = t._1 + t._2 + t._3 + t._4
    val ita   = Iterator(20, 40, 2, 50, 69, 90)
    val itb   = Iterator(20, 40, 2, 50, 69, 90)
    udf((s: String) => s.length)
  }

  def udf_string_length7 = {
    import org.apache.spark.sql.expressions.Window
    import org.apache.spark.sql.functions._
    var int_value    = 10
    var string_value = "string value"
    val colors =
      Map("red" -> "#FF0000", "azure" -> "#F0FFFF", "peru" -> "#CD853F")
    val nums: Map[Int, Int] = Map()
    val fruit = Set("apples", "oranges", "pears")
    val t     = (4, 3, 2, 1)
    val sum   = t._1 + t._2 + t._3 + t._4
    val ita   = Iterator(20, 40, 2, 50, 69, 90)
    val itb   = Iterator(20, 40, 2, 50, 69, 90)
    udf((s: String) => s.length)
  }

  def udf_string_length9 = {
    import org.apache.spark.sql.expressions.Window
    import org.apache.spark.sql.functions._
    var int_value    = 10
    var string_value = "string value"
    val colors =
      Map("red" -> "#FF0000", "azure" -> "#F0FFFF", "peru" -> "#CD853F")
    val nums: Map[Int, Int] = Map()
    val fruit = Set("apples", "oranges", "pears")
    val t     = (4, 3, 2, 1)
    val sum   = t._1 + t._2 + t._3 + t._4
    val ita   = Iterator(20, 40, 2, 50, 69, 90)
    val itb   = Iterator(20, 40, 2, 50, 69, 90)
    udf((s: String) => s.length)
  }

  def udf_string_length10 = {
    import org.apache.spark.sql.expressions.Window
    import org.apache.spark.sql.functions._
    var int_value    = 10
    var string_value = "string value"
    val colors =
      Map("red" -> "#FF0000", "azure" -> "#F0FFFF", "peru" -> "#CD853F")
    val nums: Map[Int, Int] = Map()
    val fruit = Set("apples", "oranges", "pears")
    val t     = (4, 3, 2, 1)
    val sum   = t._1 + t._2 + t._3 + t._4
    val ita   = Iterator(20, 40, 2, 50, 69, 90)
    val itb   = Iterator(20, 40, 2, 50, 69, 90)
    udf((s: String) => s.length)
  }

  def udf_complex_window = {
    import org.apache.spark.sql.expressions.Window
    import org.apache.spark.sql.functions._
    var int_value    = 10
    var string_value = "string value"
    val colors =
      Map("red" -> "#FF0000", "azure" -> "#F0FFFF", "peru" -> "#CD853F")
    val nums: Map[Int, Int] = Map()
    val fruit = Set("apples", "oranges", "pears")
    val t     = (4, 3, 2, 1)
    val sum   = t._1 + t._2 + t._3 + t._4
    val ita   = Iterator(20, 40, 2, 50, 69, 90)
    val itb   = Iterator(20, 40, 2, 50, 69, 90)
    udf((s: String) => s.length)
  }

  def udf1 = {
    var a = 10
    udf((value: Int) => value * a)
  }

  def udf_matrix_test =
    udf((value: Int) => value * value)

  def udf_matrices_test =
    udf(() => 2 * 4)

  def udf_vectors_test =
    udf(() => 2 * 6)

}

object PipelineInitCode extends Serializable
