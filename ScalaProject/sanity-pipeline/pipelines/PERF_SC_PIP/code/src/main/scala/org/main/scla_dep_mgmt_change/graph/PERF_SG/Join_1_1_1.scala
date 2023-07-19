package org.main.scla_dep_mgmt_change.graph.PERF_SG

import io.prophecy.libs._
import org.main.scla_dep_mgmt_change.udfs.UDFs._
import org.main.scla_dep_mgmt_change.graph.PERF_SG.config.Context
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._

object Join_1_1_1 {

  def apply(context: Context, in0: DataFrame, in1: DataFrame): DataFrame =
    in0
      .as("in0")
      .join(
        in1.as("in1"),
        col("in0.cmls_3ds_authntn_mthd") === col("in1.cmls_3ds_authntn_mthd"),
        "inner"
      )
      .select(concat(col("in0.cmls_3ds_authntn_mthd"),
                     col("in1.cmls_3ds_authntn_mthd")
              ).as("c_concat_test"),
              col("in0.*")
      )

}
