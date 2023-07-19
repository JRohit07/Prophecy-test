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

object Reformat_3 {

  def apply(context: Context, in: DataFrame): DataFrame =
    in.select(
      array(col("year"),                 col("value"), col("unit")).as("arr_str1"),
      array(col("industry_code_ANZSIC"), col("industry_name_ANZSIC"))
        .as("arr_str2"),
      array(lit(1), lit(2), col("year").cast(IntegerType)).as("arr_int"),
      struct(array(col("year"),                 col("value"), col("unit")).as("col1"),
             array(col("industry_code_ANZSIC"), col("industry_name_ANZSIC"))
               .as("col2"),
             col("unit")
      ).as("struct_complex"),
      col("year"),
      col("variable")
    )

}
