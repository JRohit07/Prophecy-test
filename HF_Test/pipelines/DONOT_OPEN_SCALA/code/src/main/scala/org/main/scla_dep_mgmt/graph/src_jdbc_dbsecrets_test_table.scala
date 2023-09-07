package org.main.scla_dep_mgmt.graph

import io.prophecy.libs._
import org.main.scla_dep_mgmt.config.Context
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._

object src_jdbc_dbsecrets_test_table {

  def apply(context: Context): DataFrame = {
    var reader = context.spark.read.format("jdbc")
    reader = reader
      .option("url",                  "jdbc:mysql://18.144.156.219:3306/test_database")
      .option("user",                 sys.env("ENV_JDBC_USER"))
      .option("password",             sys.env("ENV_JDBC_PASSWORD"))
      .option("pushDownPredicate",    true)
      .option("driver",               "com.mysql.jdbc.Driver")
    reader = reader.option("dbtable", "test_table")
    reader.load()
  }

}
