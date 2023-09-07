package com.scalaio.main.job1.graph

import io.prophecy.libs._
import com.scalaio.main.job1.udfs.PipelineInitCode._
import com.scalaio.main.job1.udfs.UDFs._
import com.scalaio.main.job1.config.Context
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._

object Reformat_11 {

  def apply(context: Context, in: DataFrame): DataFrame =
    in.select(col("`c-decimal`").as("c-decimal"),
              col("`c  float`").as("c  float"),
              col("`c  float`").as("c .float")
    )

}
