package org.main.scla_dep_mgmt_change.graph

import io.prophecy.libs._
import org.main.scla_dep_mgmt_change.udfs.UDFs._
import org.main.scla_dep_mgmt_change.config.Context
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._

object PERF_JOIN {

  def apply(context: Context, in0: DataFrame, in1: DataFrame): DataFrame =
    in0
      .as("in0")
      .join(in1.as("in1"), col("in0.c_short") === col("in1.c_short"), "inner")
      .where(
        !col("in0.c_string")
          .like("%hello sir this is simple where clause%")
          .and(col("in1.c_int") > lit(-1))
      )
      .select(col("in0.first_name").as("first_name"),
              col("in0.c_short").as("c_short")
      )

}
