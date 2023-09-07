package org.main.scla_dep_mgmt_change.graph.RemoveSG

import io.prophecy.libs._
import org.main.scla_dep_mgmt_change.udfs.PipelineInitCode._
import org.main.scla_dep_mgmt_change.udfs.UDFs._
import org.main.scla_dep_mgmt_change.graph.RemoveSG.config.Context
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._

object Limit_2 {
  def apply(context: Context, in: DataFrame): DataFrame = in.limit(10)
}
