package com.scala.main.job1.graph

import io.prophecy.libs._
import com.scala.main.job1.config.Context
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._

object dest_test {

  def apply(context: Context, in: DataFrame): Unit = {
    var writer = in.write.format("orc").mode("overwrite")
    writer = writer
    writer.save("dbfs:/tmp/dest_temp_io_scala_disableddude")
  }

}
