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

object Aggregate_1 {

  def apply(context: Context, in: DataFrame): DataFrame = {
    val Config = context.config
    in.groupBy(concat(col("c1"), col("c2")).as("col1"),
               expr(Config.c_agg_group).as("col2"),
               lit(Config.c_agg_c3).as("c3")
      )
      .pivot(col("c7"),                      List("c8", "c9_udf1"))
      .agg(expr(Config.c_agg_expr).as("c1"), first(col("c2")).as("c2"))
  }

}
