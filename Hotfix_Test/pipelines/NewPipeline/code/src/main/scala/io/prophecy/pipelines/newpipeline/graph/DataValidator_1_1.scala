package io.prophecy.pipelines.newpipeline.graph

import io.prophecy.libs._
import io.prophecy.pipelines.newpipeline.udfs.PipelineInitCode._
import io.prophecy.pipelines.newpipeline.udfs.UDFs._
import io.prophecy.pipelines.newpipeline.config.Context
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._

object DataValidator_1_1 {

  def apply(context: Context, in: DataFrame): (DataFrame, DataFrame) = {
    import org.apache.spark.sql.functions._
    (in,
     in.filter(List().reduce(_ || _)).withColumn("rule_broken", lit("None"))
    )
  }

}
