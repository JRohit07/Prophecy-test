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

object Reformat_5 {

  def apply(context: Context, in: DataFrame): DataFrame =
    in.select(
      col("col1"),
      col("col2"),
      col("c3"),
      col("c8_c1"),
      col("c8_c2"),
      col("c9_udf1_c1"),
      col("c9_udf1_c2"),
      substring(col("c9_udf1_c2"), 1, 2).cast(IntegerType).as("cast_c9_sql"),
      lit(context.config.c_sql_c8c1).as("c_sql_c8c1_sql")
    )

}
