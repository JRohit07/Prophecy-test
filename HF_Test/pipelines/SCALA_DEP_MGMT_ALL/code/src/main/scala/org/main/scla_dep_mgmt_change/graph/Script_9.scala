package org.main.scla_dep_mgmt_change.graph

import io.prophecy.libs._
import org.main.scla_dep_mgmt_change.config.Context
import org.main.scla_dep_mgmt_change.udfs.UDFs._
import org.main.scla_dep_mgmt_change.udfs._
import org.main.scla_dep_mgmt_change.udfs.PipelineInitCode._
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._

object Script_9 {
  def apply(context: Context, in0: DataFrame, in1: DataFrame): (DataFrame, DataFrame, DataFrame) = {
    val spark = context.spark
    val Config = context.config
    var out0=in0
    var out1=in1
    var out2=in1
    (out0, out1, out2)
  }

}
