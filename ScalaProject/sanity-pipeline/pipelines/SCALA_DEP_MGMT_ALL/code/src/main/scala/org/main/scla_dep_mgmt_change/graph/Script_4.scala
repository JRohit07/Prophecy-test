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

object Script_4 {
  def apply(context: Context, in0: DataFrame): Unit = {
    val spark = context.spark
    val Config = context.config
    var out=in0 //.filter(col("c_short")  > -654566)
    print(out.show())
    println(Config.CONFIG_STR)
    println(Config.CONFIG_BOOLEAN)
    println(Config.CONFIG_DOUBLE)
    println(Config.CONFIG_INT)
    println(Config.CONFIG_FLOAT)
    println(Config.c_agg_expr)
  }

}
