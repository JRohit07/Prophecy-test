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

object PassMeBuddy {

  def apply(context: Context, in: DataFrame): DataFrame =
    in.select(
      col("`c- short`").as("c- short"),
      col("`c  - int`").as("c  - int"),
      col("`- c long`").as("- c long"),
      col("`c_decimal  -  `").as("c_decimal  -  "),
      col("`c_float-__  `").as("c_float-__  "),
      col("`c -  boolean _  `").as("c -  boolean _  "),
      col("c_double"),
      col("`c-string`").as("c-string"),
      col("`c_date-for today`").as("c_date-for today"),
      col("`c_timestamp  __ for--today`").as("c_timestamp  __ for--today"),
      col("`c_array-int  _ int`").as("c_array-int  _ int"),
      col("`c_array-string  _ string`").as("c_array-string  _ string"),
      col("`c_array--long`").as("c_array--long"),
      col("`c_array-- boolean `").as("c_array-- boolean "),
      col("`-- c_array_timestamp -- `").as("-- c_array_timestamp -- "),
      col("`c_array -- float`").as("c_array -- float"),
      col("`c_array -- decimal`").as("c_array -- decimal"),
      col("`c_struct -- _  `").as("c_struct -- _  "),
      col("p_short"),
      col("p_int"),
      col("p_long"),
      col("p_decimal"),
      col("p_float"),
      col("p_boolean"),
      col("p_double"),
      col("p_string"),
      col("p_date"),
      col("p_timestamp"),
      col("c_config_use"),
      col("c_config_spark_expr"),
      col("c_udf"),
      expr("qa_mask_zip_code(`c-string`)").as("c_call_func")
    )

}
