package org.main.scla_dep_mgmt_change.graph.pm_shared_graph.Subgraph_1

import io.prophecy.libs._
import org.main.scla_dep_mgmt_change.udfs.PipelineInitCode._
import org.main.scla_dep_mgmt_change.udfs.UDFs._
import org.main.scla_dep_mgmt_change.graph.pm_shared_graph.Subgraph_1.config.Context
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._

object Reformat_11 {

  def apply(context: Context, in: DataFrame): DataFrame =
    in.select(udf_add_one(lit(context.config.var2)).as("c_int"))

}
