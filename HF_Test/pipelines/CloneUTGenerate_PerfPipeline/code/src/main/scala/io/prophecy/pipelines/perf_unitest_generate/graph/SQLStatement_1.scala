package io.prophecy.pipelines.perf_unitest_generate.graph

import io.prophecy.libs._
import io.prophecy.pipelines.perf_unitest_generate.config.ConfigStore._
import io.prophecy.pipelines.perf_unitest_generate.config.Context
import io.prophecy.pipelines.perf_unitest_generate.udfs.UDFs._
import io.prophecy.pipelines.perf_unitest_generate.udfs._
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._

object SQLStatement_1 {

  def apply(context: Context, in0: DataFrame): DataFrame = {
    in0.createOrReplaceTempView("in0")
    context.spark.sql("select * from in0")
  }

}
