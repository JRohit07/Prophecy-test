package com.scalaio.main.job1.graph.Subgraph_3

import io.prophecy.libs._
import com.scalaio.main.job1.udfs.PipelineInitCode._
import com.scalaio.main.job1.udfs.UDFs._
import com.scalaio.main.job1.graph.Subgraph_3.config.Context
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._
object Reformat_6 { def apply(context: Context, in: DataFrame): DataFrame = in }
