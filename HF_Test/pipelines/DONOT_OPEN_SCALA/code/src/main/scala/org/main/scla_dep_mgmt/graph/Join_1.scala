package org.main.scla_dep_mgmt.graph

import io.prophecy.libs._
import org.main.scla_dep_mgmt.udfs.UDFs._
import org.main.scla_dep_mgmt.config.Context
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._

object Join_1 {

  def apply(context: Context, in0: DataFrame, in1: DataFrame): DataFrame =
    in0
      .as("in0")
      .join(in1.as("in1"),
            col("in0.`-- c-long`") === col("in1.`-- c-long`"),
            "inner"
      )
      .select(
        col("in0.`c   short  --`").as("c   short  --"),
        col("in0.`c-int-column type`").as("c-int-column type"),
        col("in0.`-- c-long`").as("-- c-long"),
        col("in0.`c-decimal`").as("c-decimal"),
        col("in0.`c  float`").as("c  float"),
        col("in0.`c--boolean`").as("c--boolean"),
        col("in0.`c- - -double`").as("c- - -double"),
        col("in0.`c___-- string`").as("c___-- string"),
        col("in0.`c  date`").as("c  date"),
        col("in0.c_timestamp").as("c_timestamp"),
        col("in1.`c   short  --`").as("c   short  --"),
        col("in1.`c-int-column type`").as("c-int-column type"),
        col("in1.`-- c-long`").as("-- c-long"),
        col("in1.`c-decimal`").as("c-decimal"),
        col("in1.`c  float`").as("c  float"),
        col("in1.`c--boolean`").as("c--boolean"),
        col("in1.`c- - -double`").as("c- - -double"),
        col("in1.`c___-- string`").as("c___-- string"),
        col("in1.`c  date`").as("c  date"),
        col("in1.c_timestamp").as("c_timestamp")
      )

}
