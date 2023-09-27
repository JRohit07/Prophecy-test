package io.prophecy.pipelines.newpipeline.graph

import io.prophecy.libs._
import io.prophecy.pipelines.newpipeline.config.Context
import io.prophecy.pipelines.newpipeline.udfs.UDFs._
import io.prophecy.pipelines.newpipeline.udfs.PipelineInitCode._
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._

object Lookup_0_2 {

  def apply(context: Context, in0: DataFrame): Unit =
    createLookup("", in0, context.spark, List())

}
