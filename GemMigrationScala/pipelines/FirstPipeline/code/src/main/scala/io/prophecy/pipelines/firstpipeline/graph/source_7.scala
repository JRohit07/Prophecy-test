package io.prophecy.pipelines.firstpipeline.graph

import io.prophecy.libs._
import io.prophecy.pipelines.firstpipeline.config.Context
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._

object source_7 {

  def apply(context: Context): DataFrame = {
    val Config = context.config
    var reader = context.spark.read.format("jdbc")
    reader = reader
      .option("url",                s"jdbc:mysql://3.101.152.38:3306/${Config.JDBC_DATABASE}")
      .option("user",               s"${sys.env("JDBC_USERNAME")}")
      .option("password",           s"${sys.env("JDBC_PASSWORD")}")
      .option("pushDownPredicate",  true)
      .option("driver",             "com.mysql.jdbc.Driver")
    reader = reader.option("query", s"select * from ${Config.JDBC_TABLE}")
    var df = reader.load()
    df
  }

}
