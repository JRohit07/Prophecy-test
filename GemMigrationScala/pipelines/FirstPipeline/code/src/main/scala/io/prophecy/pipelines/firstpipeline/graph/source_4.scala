package io.prophecy.pipelines.firstpipeline.graph

import io.prophecy.libs._
import io.prophecy.pipelines.firstpipeline.config.Context
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._

object source_4 {

  def apply(context: Context): DataFrame = {
    val Config = context.config
    var reader = context.spark.read.format("jdbc")
    reader = reader
      .option("url",                  s"${Config.JDBC}${Config.JDBC_DATABASE}")
      .option("user",                 "test_user")
      .option("password",             "admin")
      .option("pushDownPredicate",    true)
      .option("driver",               Config.DRIVER_NAME)
    reader = reader.option("dbtable", Config.JDBC_TABLE)
    var df = reader.load()
    df
  }

}
