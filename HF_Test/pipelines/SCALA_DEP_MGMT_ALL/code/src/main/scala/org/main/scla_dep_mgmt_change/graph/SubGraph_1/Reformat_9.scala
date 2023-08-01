package org.main.scla_dep_mgmt_change.graph.SubGraph_1

import io.prophecy.libs._
import org.main.scla_dep_mgmt_change.udfs.PipelineInitCode._
import org.main.scla_dep_mgmt_change.udfs.UDFs._
import org.main.scla_dep_mgmt_change.graph.SubGraph_1.config.Context
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._

object Reformat_9 {

  def apply(context: Context, in: DataFrame): DataFrame = {
    val Config = context.config
    in.select(
      col("c_array_int"),
      col("c_array_string"),
      col("c_array_long"),
      col("c_array_boolean"),
      col("c_array_date"),
      col("c_array_timestamp"),
      col("c_array_float"),
      col("c_array_decimal"),
      col("`c_struct-c_array_int`").as("c_struct-c_array_int"),
      col("`c_struct-c_timestamp`").as("c_struct-c_timestamp"),
      col("`c_struct-c_short`").as("c_struct-c_short"),
      col("`c_struct-c_decimal`").as("c_struct-c_decimal"),
      concat(lit(Config.c_short),                           lit(Config.c_bool)).as("c_config")
    )
  }

}
