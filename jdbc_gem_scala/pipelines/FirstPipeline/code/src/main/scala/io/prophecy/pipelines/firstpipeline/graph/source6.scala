package io.prophecy.pipelines.firstpipeline.graph

import io.prophecy.libs._
import io.prophecy.pipelines.firstpipeline.config.Context
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._

object source6 {

  def apply(context: Context): DataFrame = {
    val Config = context.config
    var reader = context.spark.read.format("jdbc")
    reader = reader
      .option("url",                Config.JDBC_URL)
      .option("user",               sys.env("JDBC_USERNAME"))
      .option("password",           sys.env("JDBC_PASSWORD"))
      .option("pushDownPredicate",  true)
      .option("driver",             "com.mysql.jdbc.Driver")
    reader = reader.option("query", Config.SQL_QUERY)
    var df = reader.load()
    df
  }

}
