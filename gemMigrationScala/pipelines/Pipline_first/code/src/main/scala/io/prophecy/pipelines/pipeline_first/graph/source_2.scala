package io.prophecy.pipelines.pipeline_first.graph

import io.prophecy.libs._
import io.prophecy.pipelines.pipeline_first.config.Context
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._

object source_2 {

  def apply(context: Context): DataFrame = {
    val Config = context.config
    var reader = context.spark.read.format("jdbc")
    reader = reader
      .option("url", Config.JDBC_URL)
      .option("user",
              dbutils.secrets.get(scope = "rohit_mysql", key = "username")
      )
      .option("password",
              dbutils.secrets.get(scope = "rohit_mysql", key = "password")
      )
      .option("pushDownPredicate",    true)
      .option("driver",               Config.DRIVER_NAME)
    reader = reader.option("dbtable", "test_table_automation")
    var df = reader.load()
    df
  }

}
