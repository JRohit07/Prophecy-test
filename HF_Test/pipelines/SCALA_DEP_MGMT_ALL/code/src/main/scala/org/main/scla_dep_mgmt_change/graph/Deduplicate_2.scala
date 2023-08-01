package org.main.scla_dep_mgmt_change.graph

import io.prophecy.libs._
import org.main.scla_dep_mgmt_change.udfs.PipelineInitCode._
import org.main.scla_dep_mgmt_change.udfs.UDFs._
import org.main.scla_dep_mgmt_change.config.Context
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._

object Deduplicate_2 {

  def apply(context: Context, in: DataFrame): DataFrame = {
    val Config = context.config
    import org.apache.spark.sql.expressions.Window
    in.withColumn(
        "row_number",
        row_number().over(
          Window
            .partitionBy("c_array_int", "c_array_string")
            .orderBy(expr(Config.c_dedup_expr).asc,
                     lit(Config.c_dedup_col).desc
            )
        )
      )
      .withColumn(
        "count",
        count("*").over(Window.partitionBy("c_array_int", "c_array_string"))
      )
      .filter(col("row_number") === col("count"))
      .drop("row_number")
      .drop("count")
  }

}
