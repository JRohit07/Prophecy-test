package io.prophecy.pipelines.pipeline_with_configs.graph

import io.prophecy.libs._
import io.prophecy.pipelines.pipeline_with_configs.config.Context
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._

object target_1_2 {

  def apply(context: Context, in: DataFrame): Unit = {
    val Config = context.config
    var writer = in.write.format("jdbc")
    writer = writer
      .option("url",      s"${Config.jdbc_url_databricks}")
      .option("dbtable",  "test_table_destination")
      .option("user",     s"${Config.JDBC_USER_SECRET_databricks}")
      .option("password", s"${Config.JDBC_PASSWORD_SECRET_databricks}")
      .option("driver",   "com.mysql.jdbc.Driver")
    writer = writer.mode("overwrite")
    writer.save()
  }

}
