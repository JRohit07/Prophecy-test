package com.scala.main.job12.graph

import io.prophecy.libs._
import com.scala.main.job12.config.Context
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._

object dest_test {

  def apply(context: Context, in: DataFrame): Unit =
    in.write
      .format("parquet")
      .mode("overwrite")
      .save("dbfs:/tmp/out_dest_temp_io_scala_disabledtest")

}
