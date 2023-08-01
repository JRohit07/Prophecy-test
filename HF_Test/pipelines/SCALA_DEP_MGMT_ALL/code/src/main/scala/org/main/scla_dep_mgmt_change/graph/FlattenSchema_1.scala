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

object FlattenSchema_1 {

  def apply(context: Context, in: DataFrame): DataFrame = {
    val flattened = in
      .withColumn("c_array_int",       explode_outer(col("c_array_int")))
      .withColumn("c_array_string",    explode_outer(col("c_array_string")))
      .withColumn("c_array_long",      explode_outer(col("c_array_long")))
      .withColumn("c_array_boolean",   explode_outer(col("c_array_boolean")))
      .withColumn("c_array_date",      explode_outer(col("c_array_date")))
      .withColumn("c_array_timestamp", explode_outer(col("c_array_timestamp")))
      .withColumn("c_array_float",     explode_outer(col("c_array_float")))
      .withColumn("c_array_decimal",   explode_outer(col("c_array_decimal")))
      .withColumn("c_struct-c_array_int",
                  explode_outer(col("c_struct.c_array_int"))
      )
    flattened.select(
      if (flattened.columns.contains("c_array_int")) col("c_array_int")
      else col("c_array_int"),
      if (flattened.columns.contains("c_array_string")) col("c_array_string")
      else col("c_array_string"),
      if (flattened.columns.contains("c_array_long")) col("c_array_long")
      else col("c_array_long"),
      if (flattened.columns.contains("c_array_boolean")) col("c_array_boolean")
      else col("c_array_boolean"),
      if (flattened.columns.contains("c_array_date")) col("c_array_date")
      else col("c_array_date"),
      if (flattened.columns.contains("c_array_timestamp"))
        col("c_array_timestamp")
      else col("c_array_timestamp"),
      if (flattened.columns.contains("c_array_float")) col("c_array_float")
      else col("c_array_float"),
      if (flattened.columns.contains("c_array_decimal")) col("c_array_decimal")
      else col("c_array_decimal"),
      if (flattened.columns.contains("c_struct-c_array_int"))
        col("c_struct-c_array_int")
      else col("c_struct.c_array_int").as("c_struct-c_array_int"),
      if (flattened.columns.contains("c_struct-c_timestamp"))
        col("c_struct-c_timestamp")
      else col("c_struct.c_timestamp").as("c_struct-c_timestamp"),
      if (flattened.columns.contains("c_struct-c_short"))
        col("c_struct-c_short")
      else col("c_struct.c_short").as("c_struct-c_short"),
      if (flattened.columns.contains("c_struct-c_decimal"))
        col("c_struct-c_decimal")
      else col("c_struct.c_decimal").as("c_struct-c_decimal")
    )
  }

}
