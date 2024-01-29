package io.prophecy.pipelines.firstpipeline.graph

import io.prophecy.libs._
import io.prophecy.pipelines.firstpipeline.config.Context
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._

object target_7 {

  def apply(context: Context, in: DataFrame): Unit = {
    val Config = context.config
    var writer = in.write.format("jdbc")
    writer = writer
      .option("url",      Config.JDBC_URL)
      .option("dbtable",  "test_table_destination")
      .option("user",     sys.env(s"${Config.ENV_JDBC_USERNAME}"))
      .option("password", sys.env("JDBC_PASSWORD"))
      .option("driver",   Config.DRIVER_NAME)
    writer = writer.mode("overwrite")
    writer.save()
  }

}
