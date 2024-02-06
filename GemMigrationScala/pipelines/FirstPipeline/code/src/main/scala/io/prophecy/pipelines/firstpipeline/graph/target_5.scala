package io.prophecy.pipelines.firstpipeline.graph

import io.prophecy.libs._
import io.prophecy.pipelines.firstpipeline.config.Context
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._

object target_5 {

  def apply(context: Context, in: DataFrame): Unit = {
    val Config = context.config
    var writer = in.write.format("jdbc")
    writer = writer
      .option("url",      s"${Config.JDBC}${Config.JDBC_DATABASE}")
      .option("dbtable",  s"${Config.TEST}_table_destination")
      .option("user",     s"${Config.TEST}_${Config.USER}")
      .option("password", s"${Config.ADM}${Config.IN}")
      .option("driver",   "com.mysql.jdbc.Driver")
    writer = writer.mode("overwrite")
    writer.save()
  }

}
