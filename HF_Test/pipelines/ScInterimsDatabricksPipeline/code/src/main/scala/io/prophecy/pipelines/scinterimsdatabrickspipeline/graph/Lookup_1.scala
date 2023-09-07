package io.prophecy.pipelines.scinterimsdatabrickspipeline.graph

import io.prophecy.libs._
import io.prophecy.pipelines.scinterimsdatabrickspipeline.config.Context
import io.prophecy.pipelines.scinterimsdatabrickspipeline.udfs.UDFs._
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._

object Lookup_1 {

  def apply(context: Context, in0: DataFrame): Unit =
    createLookup("Lookup_2",
                 in0,
                 context.spark,
                 List("year", "industry_name_ANZSIC"),
                 "industry_code_ANZSIC"
    )

}
