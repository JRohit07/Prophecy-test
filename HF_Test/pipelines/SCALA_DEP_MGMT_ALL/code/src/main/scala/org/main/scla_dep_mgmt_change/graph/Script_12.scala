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

object Script_12 {
  def apply(context: Context): DataFrame = {
    val spark = context.spark
    val Config = context.config
    import spark.implicits._
    val out0 = Seq(
      (Config.CONFIG_INT, Config.CONFIG_STR),
      (64, Config.c_record_complex.cr_string),
      (-27, Config.c_array_complex(0).car_string)
    ).toDF("c_number", "c_string")
    out0
  }

}
