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

object SetOperation_1 {

  def apply(context: Context, in0: DataFrame, in1: DataFrame): DataFrame =
    in0.unionAll(in1)

}
