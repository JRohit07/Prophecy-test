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

object WindowFunction_1 {

  def apply(context: Context, in: DataFrame): DataFrame = {
    import org.apache.spark.sql.expressions.{Window, WindowSpec}
    in.withColumn(
        "variable",
        row_number().over(
          Window
            .partitionBy(col("year"),                 col("industry_code_ANZSIC"))
            .orderBy(col("industry_name_ANZSIC").asc, col("rme_size_grp").asc)
        )
      )
      .withColumn(
        "value",
        row_number().over(
          Window
            .partitionBy(col("year"),                 col("industry_code_ANZSIC"))
            .orderBy(col("industry_name_ANZSIC").asc, col("rme_size_grp").asc)
        )
      )
      .withColumn(
        "unit",
        row_number().over(
          Window
            .partitionBy(col("year"),                 col("industry_code_ANZSIC"))
            .orderBy(col("industry_name_ANZSIC").asc, col("rme_size_grp").asc)
        )
      )
  }

}
