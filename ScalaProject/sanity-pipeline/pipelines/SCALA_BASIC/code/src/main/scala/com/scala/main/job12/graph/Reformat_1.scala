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

object Reformat_1 {

  def apply(context: Context, in: DataFrame): DataFrame =
    in.select(
      col("`c   short  --`").as("c   short  --"),
      col("`c-int-column type`").as("c-int-column type"),
      col("`-- c-long`").as("-- c-long"),
      col("`c-decimal`").as("c-decimal"),
      col("`c  float`").as("c  float"),
      col("`c--boolean`").as("c--boolean"),
      col("`c- - -double`").as("c- - -double"),
      col("`c___-- string`").as("c___-- string"),
      col("`c  date`").as("c  date"),
      col("c_timestamp"),
      concat(
        lookup("TestLookup", col("`c   short  --`"), col("`c-int-column type`"))
          .getField("c--boolean"),
        lookup("TestLookup", col("`c   short  --`"), col("`c-int-column type`"))
          .getField("c  float")
      ).as("c_lookup_1"),
      col("`c___-- string`")
        .endsWith(col("`c  float`"))
        .or(col("`c___-- string`").startsWith(col("`c  float`")))
        .or(col("`c___-- string`").contains(col("`c  float`")))
        .as("c_contains_starts_ends")
    )

}
