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

object SQLStatement_1 {

  def apply(
    context: Context,
    input_0: DataFrame
  ): (DataFrame, DataFrame, DataFrame, DataFrame) = {
    input_0.createOrReplaceTempView("input_0")
    (context.spark.sql("select * from input_0 where cast(year as int) >= 2011"),
     context.spark.sql(
       "select * from input_0 where industry_code_ANZSIC like '%A%'"
     ),
     context.spark.sql("select * from input_0 where variable like '%Total%'"),
     context.spark.sql("select * from input_0 where cast(value as int) > 600")
    )
  }

}
