package io.prophecy.pipelines.firstpipeline.graph

import io.prophecy.libs._
import io.prophecy.pipelines.firstpipeline.config.Context
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._

object target_3 {

  def apply(context: Context, in: DataFrame): Unit = {
    var writer = in.write.format("jdbc")
    writer = writer
      .option("url",      "jdbc:mysql://3.101.152.38:3306/test_database")
      .option("dbtable",  "test_table_destination")
      .option("user",     sys.env("JDBC_USERNAME"))
      .option("password", sys.env("JDBC_PASSWORD"))
      .option("driver",   "com.mysql.jdbc.Driver")
    writer = writer.mode("overwrite")
    writer.save()
  }

}
