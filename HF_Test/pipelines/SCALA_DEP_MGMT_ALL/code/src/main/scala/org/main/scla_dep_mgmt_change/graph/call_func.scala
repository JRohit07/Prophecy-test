package org.main.scla_dep_mgmt_change.graph

import io.prophecy.libs._
import org.main.scla_dep_mgmt_change.udfs.PipelineInitCode._
import org.main.scla_dep_mgmt_change.udfs.UDFs._
import org.main.scla_dep_mgmt_change.config.Context
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._

object call_func {

  def apply(context: Context, in: DataFrame): DataFrame =
    in.select(
      expr("named_struct('a', 'test', 'b', 2, 'c', 3)").as("c1"),
      expr(
        context.config.c_record_complex.cr_array_record(0).crar_spark_expression
      ).as("c2"),
      expr("qa_mask_zip_code(country_code)").as("c3")
    )

}
