package io.prophecy.pipelines.firstpipeline.graph

import io.prophecy.libs._
import io.prophecy.pipelines.firstpipeline.config.Context
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._

object source_1 {

  def apply(context: Context): DataFrame = {
    var reader = context.spark.read.format("jdbc")
    reader = reader
      .option("url", "jdbc:mysql://3.101.152.38:3306/test_database")
      .option("user", {
                import com.databricks.dbutils_v1.DBUtilsHolder.dbutils
                dbutils.secrets.get(scope = "rohit_mysql", key = "username")
              }
      )
      .option("password", {
                import com.databricks.dbutils_v1.DBUtilsHolder.dbutils
                dbutils.secrets.get(scope = "rohit_mysql", key = "password")
              }
      )
      .option("pushDownPredicate",  true)
      .option("driver",             "com.mysql.jdbc.Driver")
    reader = reader.option("query", "select * from test_table")
    reader.load()
  }

}
