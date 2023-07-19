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

object Script_6 {
  def apply(context: Context, in0: DataFrame, in1: DataFrame, in2: DataFrame, in3: DataFrame, in4: DataFrame, in5: DataFrame): DataFrame = {
    val spark = context.spark
    val Config = context.config
    var a=Config.c_1*Config.c_0
    assert(a==0)
    a=a+int_value_from_pipeline_init
    var out0=in0.filter(col("customer_id")  > 5)
    var out1=in1.filter(col("customer_id")  > 5)
    var out2=in2.filter(col("first_name") === "%A%" )
    var out3=in3.distinct()
    var out4=in4.filter(col("customer_id")  > 5)
    var out5=in5.filter(col("customer_id")  > 5)
    println(s"Configs are: CONFIG_STR: ${Config.CONFIG_STR} \n CONFIG_DOUBLE: ${Config.CONFIG_DOUBLE} \n CONFIG_BOOLEAN: ${Config.CONFIG_BOOLEAN} \n CONFIG_INT: ${Config.CONFIG_INT} \n CONFIG_FLOAT: ${Config.CONFIG_FLOAT}")
    
    out0=out1.union(out2).union(out3).union(out4).union(out5)
    out0
  }

}
