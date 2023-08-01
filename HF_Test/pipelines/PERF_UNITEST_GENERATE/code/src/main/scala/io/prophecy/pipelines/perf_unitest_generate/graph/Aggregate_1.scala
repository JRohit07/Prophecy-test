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

object Aggregate_1 {

  def apply(context: Context, in: DataFrame): DataFrame =
    in.groupBy(col("last_name"))
      .agg(
        first(col("account_flags")).as("account_flags"),
        first(col("account_open_date")).as("account_open_date"),
        first(col("country_code")).as("country_code"),
        first(col("customer_id")).as("customer_id")
      )

}
