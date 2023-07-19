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

object FlattenSchema_1_1 {

  def apply(context: Context, in: DataFrame): DataFrame = {
    val flattened = in
      .withColumn("c_array--long", explode_outer(col("c_array--long")))
      .withColumn("c_array -- decimal",
                  explode_outer(col("c_array -- decimal"))
      )
      .withColumn("c_array-int  _ int",
                  explode_outer(col("c_array-int  _ int"))
      )
      .withColumn(
        "c_struct -- _  -c_array_int - of a struct ",
        explode_outer(col("c_struct -- _  .c_array_int - of a struct "))
      )
    flattened.select(
      if (flattened.columns.contains("c_array--long")) col("c_array--long")
      else col("c_array--long"),
      if (flattened.columns.contains("c_array -- decimal"))
        col("c_array -- decimal")
      else col("c_array -- decimal"),
      if (
        flattened.columns.contains("c_struct -- _  -c_array_int - of a struct ")
      ) col("c_struct -- _  -c_array_int - of a struct ")
      else
        col("c_struct -- _  .c_array_int - of a struct ")
          .as("c_struct -- _  -c_array_int - of a struct "),
      if (
        flattened.columns.contains("c_struct -- _  -c_timestamp - of a struct-")
      ) col("c_struct -- _  -c_timestamp - of a struct-")
      else
        col("c_struct -- _  .c_timestamp - of a struct-")
          .as("c_struct -- _  -c_timestamp - of a struct-"),
      if (
        flattened.columns
          .contains("c_struct -- _  -c_string - of a struct -- _")
      ) col("c_struct -- _  -c_string - of a struct -- _")
      else
        col("c_struct -- _  .c_string - of a struct -- _")
          .as("c_struct -- _  -c_string - of a struct -- _"),
      if (flattened.columns.contains("c_array-int  _ int"))
        col("c_array-int  _ int")
      else col("c_array-int  _ int")
    )
  }

}
