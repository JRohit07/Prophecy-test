package org.main.scla_dep_mgmt_change.graph.all_type_sg_scala_main

import io.prophecy.libs._
import org.main.scla_dep_mgmt_change.graph.all_type_sg_scala_main.config.Context
import org.main.scla_dep_mgmt_change.udfs.PipelineInitCode._
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._

object Script_1_1 {
  def apply(context: Context, in0: DataFrame): DataFrame = {
    val spark = context.spark
    val Config = context.config
    var config_int_plus_long=Config.c_sg1_c_int+Config.c_sg1_c_long
    var out0=in0
    out0
  }

}
