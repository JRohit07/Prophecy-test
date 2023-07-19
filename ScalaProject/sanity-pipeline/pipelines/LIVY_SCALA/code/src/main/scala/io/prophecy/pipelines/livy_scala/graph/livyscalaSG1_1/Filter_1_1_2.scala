package io.prophecy.pipelines.livy_scala.graph.livyscalaSG1_1

import io.prophecy.libs._
import io.prophecy.pipelines.livy_scala.udfs.PipelineInitCode._
import io.prophecy.pipelines.livy_scala.udfs.UDFs._
import io.prophecy.pipelines.livy_scala.graph.livyscalaSG1_1.config.Context
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._

object Filter_1_1_2 {

  def apply(context: Context, in: DataFrame): DataFrame =
    in.filter(!col("year").like("%45345%"))

}
