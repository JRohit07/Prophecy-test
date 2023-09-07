package com.main.sub_graph_src1.graph.all_type_sg_scala_main

import io.prophecy.libs._
import com.main.sub_graph_src1.udfs.PipelineInitCode._
import com.main.sub_graph_src1.udfs.UDFs._
import com.main.sub_graph_src1.graph.all_type_sg_scala_main.config.Context
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._

object Join_1_1 {

  def apply(context: Context, in0: DataFrame, in1: DataFrame): DataFrame =
    in0
      .as("in0")
      .join(in1.as("in1"),
            col("in0.`c  - int`") === col("in1.`c  - int`"),
            "inner"
      )
      .select(
        col("in0.`c- short`").as("c- short"),
        col("in0.`c  - int`").as("c  - int"),
        col("in0.`- c long`").as("- c long"),
        col("in0.`c_decimal  -  `").as("c_decimal  -  "),
        col("in0.`c_float-__  `").as("c_float-__  "),
        col("in0.`c -  boolean _  `").as("c -  boolean _  "),
        col("in0.c_double").as("c_double"),
        col("in0.`c-string`").as("c-string"),
        col("in0.`c_date-for today`").as("c_date-for today"),
        expr(context.config.c_sg1_join_expr_timestamp)
          .as("c_timestamp  __ for--today"),
        col("in0.`c_array-int  _ int`").as("c_array-int  _ int"),
        col("in0.`c_array-string  _ string`").as("c_array-string  _ string"),
        col("in0.`c_array--long`").as("c_array--long"),
        col("in0.`c_array-- boolean `").as("c_array-- boolean "),
        col("in0.`-- c_array_timestamp -- `").as("-- c_array_timestamp -- "),
        col("in0.`c_array -- float`").as("c_array -- float"),
        col("in0.`c_array -- decimal`").as("c_array -- decimal"),
        col("in0.`c_struct -- _  `").as("c_struct -- _  "),
        col("in0.p_short").as("p_short"),
        col("in0.p_int").as("p_int"),
        col("in0.p_long").as("p_long"),
        col("in0.p_decimal").as("p_decimal"),
        col("in0.p_float").as("p_float"),
        col("in0.p_boolean").as("p_boolean"),
        col("in0.p_double").as("p_double"),
        col("in0.p_string").as("p_string"),
        col("in0.p_date").as("p_date"),
        col("in0.p_timestamp").as("p_timestamp")
      )

}
