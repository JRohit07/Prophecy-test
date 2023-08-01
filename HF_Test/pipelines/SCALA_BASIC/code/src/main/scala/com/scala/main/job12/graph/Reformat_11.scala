package com.scala.main.job12.graph

import io.prophecy.libs._
import com.scala.main.job12.udfs.PipelineInitCode._
import com.scala.main.job12.udfs.UDFs._
import com.scala.main.job12.config.Context
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._

object Reformat_11 {

  def apply(context: Context, in: DataFrame): DataFrame =
    in.select(col("`c   short  --`").as("c   short  --"),
              col("`c-int-column type`").as("c-int-column type"),
              col("`c--boolean`").as("c--boolean")
    )

}
