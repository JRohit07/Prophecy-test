package io.prophecy.pipelines.p2.graph

import io.prophecy.libs._
import io.prophecy.pipelines.p2.udfs.PipelineInitCode._
import io.prophecy.pipelines.p2.udfs.UDFs._
import io.prophecy.pipelines.p2.config.Context
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._

object Limit_1 {
  def apply(context: Context, in: DataFrame): DataFrame = in.limit(10)
}
