package io.prophecy.pipelines.livy_scala.graph

import io.prophecy.libs._
import io.prophecy.pipelines.livy_scala.udfs.PipelineInitCode._
import io.prophecy.pipelines.livy_scala.udfs.UDFs._
import io.prophecy.pipelines.livy_scala.config.Context
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._

object Aggregate_1 {

  def apply(context: Context, in: DataFrame): DataFrame =
    in.groupBy(col("year"))
      .agg(
        first(col("industry_code_ANZSIC")).as("industry_code_ANZSIC"),
        first(col("industry_name_ANZSIC")).as("industry_name_ANZSIC"),
        first(col("rme_size_grp")).as("rme_size_grp")
      )

}
