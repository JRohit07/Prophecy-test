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

object Filter_4 {

  def apply(context: Context, in: DataFrame): DataFrame = {
    val Config = context.config
    in.filter(
      !col("c9_udf1_c2")
        .like(Config.c_regex1)
        .and(!col("col2").like(Config.c_regex2))
    )
  }

}
