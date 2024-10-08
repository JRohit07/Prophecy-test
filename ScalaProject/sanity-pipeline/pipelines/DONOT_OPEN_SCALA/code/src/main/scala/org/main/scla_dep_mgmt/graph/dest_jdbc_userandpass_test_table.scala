package org.main.scla_dep_mgmt.graph

import io.prophecy.libs._
import org.main.scla_dep_mgmt.config.Context
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._

object dest_jdbc_userandpass_test_table {

  def apply(context: Context, in: DataFrame): Unit = {
    var writer = in.write.format("jdbc")
    writer = writer
      .option("url",      "jdbc:mysql://18.144.156.219:3306/test_database")
      .option("dbtable",  "test_table_destination2_random")
      .option("user",     sys.env("ENV_JDBC_USER"))
      .option("password", sys.env("ENV_JDBC_PASSWORD"))
      .option("driver",   "com.mysql.jdbc.Driver")
    writer = writer.mode("overwrite")
    writer.save()
  }

}
