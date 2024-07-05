package io.prophecy.pipelines.firstpipeline.graph

import io.prophecy.libs._
import io.prophecy.pipelines.firstpipeline.config.Context
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._

object JDBC_Gem_source_1 {

  def apply(context: Context): DataFrame = {
    var reader = context.spark.read.format("jdbc")
    reader = reader
      .option("url",                  "jdbc:mysql://3.101.152.38:3306/test_database")
      .option("user",                 "test_user")
      .option("password",             "admin")
      .option("pushDownPredicate",    true)
      .option("driver",               "com.mysql.jdbc.Driver")
    reader = reader.option("dbtable", "test_table")
    reader.load()
  }

}
