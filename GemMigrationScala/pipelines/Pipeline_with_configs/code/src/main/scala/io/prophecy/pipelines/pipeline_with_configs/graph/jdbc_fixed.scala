package io.prophecy.pipelines.pipeline_with_configs.graph

import io.prophecy.libs._
import io.prophecy.pipelines.pipeline_with_configs.config.Context
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._

object jdbc_fixed {

  def apply(context: Context): DataFrame = {
    val Config = context.config
    var reader = context.spark.read.format("jdbc")
    reader = reader
      .option("url",                s"${Config.JDBC_URL_SECRET_hashicorp}")
      .option("user",               s"${Config.JDBC_USER_SECRET_hashicorp}")
      .option("password",           s"${Config.JDBC_PASSWORD_SECRET_hashicorp}")
      .option("pushDownPredicate",  true)
      .option("driver",             "com.mysql.jdbc.Driver")
    reader = reader.option("query", "select * from test_table")
    var df = reader.load()
    df
  }

}
