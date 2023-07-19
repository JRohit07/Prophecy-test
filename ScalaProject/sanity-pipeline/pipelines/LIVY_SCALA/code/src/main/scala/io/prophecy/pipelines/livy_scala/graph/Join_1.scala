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

object Join_1 {

  def apply(context: Context, in0: DataFrame, in1: DataFrame): DataFrame =
    in0
      .as("in0")
      .join(in1.as("in1"), col("in0.year") === col("in1.year"), "inner")
      .where(col("in0.industry_code_ANZSIC") === lit("A"))
      .select(
        col("in0.year").as("year"),
        col("in0.industry_code_ANZSIC").as("industry_code_ANZSIC"),
        col("in0.industry_name_ANZSIC").as("industry_name_ANZSIC"),
        col("in1.rme_size_grp").as("rme_size_grp"),
        col("in1.variable").as("variable"),
        col("in1.value").as("value"),
        col("in1.unit").as("unit")
      )

}
