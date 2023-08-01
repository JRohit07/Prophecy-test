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

object Script_2 {
  def apply(context: Context, in0: DataFrame, in1: DataFrame, in3: DataFrame): DataFrame = {
    val spark = context.spark
    val Config = context.config
    var out1=in0.filter(col("c   short  --")  > 2).select(col("c   short  --"))
    var out2=in1.filter(col("c   short  --")  > 1).select(col("c   short  --"))
    var out4=in3.filter(col("c   short  --") > 3).select(col("c   short  --"))
    var out0=out1.union(out2).union(out4)
    out0
  }

}
