package org.main.scla_dep_mgmt_change.graph

import io.prophecy.libs._
import org.main.scla_dep_mgmt_change.config.Context
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
      .option("url", "jdbc:mysql://3.101.152.38:3306/test_database")
      .option("user", {
                import com.databricks.dbutils_v1.DBUtilsHolder.dbutils
                dbutils.secrets.get(scope = "qasecrets_mysql", key = "username")
              }
      )
      .option("password", {
                import com.databricks.dbutils_v1.DBUtilsHolder.dbutils
                dbutils.secrets.get(scope = "qasecrets_mysql", key = "password")
              }
      )
      .option("pushDownPredicate",    true)
      .option("driver",               "com.mysql.jdbc.Driver")
    reader = reader.option("dbtable", "test_table")
    reader.load()
  }

}
