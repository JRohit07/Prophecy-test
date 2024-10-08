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
    val Config = context.config
    var writer = in.write.format("jdbc")
    writer = writer
      .option("url",      s"jdbc:mysql://3.101.152.38:3306/${Config.JDBC_DATABASE}")
      .option("dbtable",  s"${Config.TEST}_table_destination")
      .option("user",     s"${Config.JDBC_USER_SECRET}")
      .option("password", s"${Config.JDBC_PASSWORD_SECRET}")
      .option("driver",   Config.JDBC_USER_SECRET)
    writer = writer.mode("overwrite")
    writer.save()
  }

}
