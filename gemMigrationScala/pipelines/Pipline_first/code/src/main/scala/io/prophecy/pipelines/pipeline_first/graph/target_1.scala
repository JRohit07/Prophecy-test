package io.prophecy.pipelines.pipeline_first.graph

import io.prophecy.libs._
import io.prophecy.pipelines.pipeline_first.config.Context
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._

object target_1 {

  def apply(context: Context, in: DataFrame): Unit = {
    var writer = in.write.format("jdbc")
    writer = writer
      .option("url",     "jdbc:mysql://3.101.152.38:3306/test_database")
      .option("dbtable", "test_table_destination")
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
      .option("driver", "com.mysql.jdbc.Driver")
    writer = writer.mode("overwrite")
    writer.save()
  }

}
