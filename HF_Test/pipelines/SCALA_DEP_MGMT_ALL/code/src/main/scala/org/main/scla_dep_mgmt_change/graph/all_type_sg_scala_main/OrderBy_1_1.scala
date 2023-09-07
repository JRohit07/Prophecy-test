package org.main.scla_dep_mgmt_change.graph.all_type_sg_scala_main

import io.prophecy.libs._
import org.main.scla_dep_mgmt_change.udfs.PipelineInitCode._
import org.main.scla_dep_mgmt_change.udfs.UDFs._
import org.main.scla_dep_mgmt_change.graph.all_type_sg_scala_main.config.Context
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._

object OrderBy_1_1 {

  def apply(context: Context, in: DataFrame): DataFrame =
    in.orderBy(
      expr(context.config.c_sg1_c_orderby).asc,
      col("`- c long`").desc,
      col("`c_decimal  -  `").asc,
      col("`c_float-__  `").asc,
      col("c_double").desc,
      col("`c_date-for today`").asc,
      col("`c_timestamp  __ for--today`").asc,
      col("p_int").asc,
      col("p_long").asc,
      col("p_decimal").asc,
      col("p_float").asc,
      col("p_boolean").asc,
      col("p_double").asc,
      col("p_string").asc,
      col("p_date").asc,
      col("p_timestamp").asc
    )

}
