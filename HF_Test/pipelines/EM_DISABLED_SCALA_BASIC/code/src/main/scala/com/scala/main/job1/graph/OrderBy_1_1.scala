package com.scala.main.job1.graph

import io.prophecy.libs._
import com.scala.main.job1.udfs.PipelineInitCode._
import com.scala.main.job1.udfs.UDFs._
import com.scala.main.job1.config.Context
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._

object OrderBy_1_1 {

  def apply(context: Context, in: DataFrame): DataFrame =
    in.orderBy(col("`c   short  --`").asc)

}
