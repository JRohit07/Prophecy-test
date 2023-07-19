package org.main.scla_dep_mgmt.graph.all_type_scala_sg_1

import io.prophecy.libs._
import org.main.scla_dep_mgmt.udfs.UDFs._
import org.main.scla_dep_mgmt.graph.all_type_scala_sg_1.config.Context
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._

object Aggregate_1_1 {

  def apply(context: Context, in: DataFrame): DataFrame =
    in.groupBy(col("`c_date-for today`"), col("`c_timestamp  __ for--today`"))
      .agg(
        first(col("`c- short`")).as("c- short"),
        first(col("`c  - int`")).as("c  - int"),
        expr(context.config.c_sg1_aggregate).as("- c long"),
        first(col("`c_decimal  -  `")).as("c_decimal  -  "),
        first(col("`c_float-__  `")).as("c_float-__  "),
        first(col("`c -  boolean _  `")).as("c -  boolean _  "),
        first(col("c_double")).as("c_double"),
        first(col("`c-string`")).as("c-string"),
        first(col("`c_date-for today`")).as("c_date-for today"),
        first(col("`c_timestamp  __ for--today`"))
          .as("c_timestamp  __ for--today"),
        first(col("`c_array-int  _ int`")).as("c_array-int  _ int"),
        first(col("`c_array-string  _ string`")).as("c_array-string  _ string"),
        first(col("`c_array--long`")).as("c_array--long"),
        first(col("`c_array-- boolean `")).as("c_array-- boolean "),
        first(col("`-- c_array_timestamp -- `")).as("-- c_array_timestamp -- "),
        first(col("`c_array -- float`")).as("c_array -- float"),
        first(col("`c_array -- decimal`")).as("c_array -- decimal"),
        first(col("`c_struct -- _  `")).as("c_struct -- _  "),
        first(col("p_short")).as("p_short"),
        first(col("p_int")).as("p_int"),
        first(col("p_long")).as("p_long"),
        first(col("p_decimal")).as("p_decimal"),
        first(col("p_float")).as("p_float"),
        first(col("p_boolean")).as("p_boolean"),
        first(col("p_double")).as("p_double"),
        first(col("p_string")).as("p_string"),
        first(col("p_date")).as("p_date"),
        first(col("p_timestamp")).as("p_timestamp")
      )

}
