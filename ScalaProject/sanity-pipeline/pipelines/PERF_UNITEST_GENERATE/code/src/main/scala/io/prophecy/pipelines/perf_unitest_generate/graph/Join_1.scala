package io.prophecy.pipelines.perf_unitest_generate.graph

import io.prophecy.libs._
import io.prophecy.pipelines.perf_unitest_generate.udfs.PipelineInitCode._
import io.prophecy.pipelines.perf_unitest_generate.udfs.UDFs._
import io.prophecy.pipelines.perf_unitest_generate.config.Context
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
            col("in0.first_name") === col("in1.first_name"),
            "inner"
      )
      .select(
        col("in0.account_flags").as("account_flags"),
        col("in0.account_open_date").as("account_open_date"),
        col("in0.country_code").as("country_code"),
        col("in1.customer_id").as("customer_id"),
        col("in0.email").as("email"),
        col("in0.first_name").as("first_name"),
        col("in0.last_name").as("last_name"),
        col("in0.phone").as("phone")
      )

}
