package io.prophecy.pipelines.pipeline_first.graph

import io.prophecy.libs._
import io.prophecy.pipelines.pipeline_first.config.Context
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._

object target_4 {

  def apply(context: Context, in: DataFrame): Unit = {
    val Config = context.config
    var writer = in.write.format("jdbc")
    writer = writer
      .option("url",     "jdbc:mysql://3.101.152.38:3306/" + Config.JDBC_DATABASE)
      .option("dbtable", Config.JDBC_DEST_TABLE)
      .option("user",
              dbutils.secrets.get(scope = "rohit_mysql", key = "username")
      )
      .option("password",
              dbutils.secrets.get(scope = "rohit_mysql", key = "password")
      )
      .option("driver", Config.DRIVER_NAME)
    writer = writer.mode("overwrite")
    writer.save()
  }

}
