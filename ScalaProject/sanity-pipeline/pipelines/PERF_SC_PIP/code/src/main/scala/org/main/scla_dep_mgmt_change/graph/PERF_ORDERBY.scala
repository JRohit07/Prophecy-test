package org.main.scla_dep_mgmt_change.graph

import io.prophecy.libs._
import org.main.scla_dep_mgmt_change.udfs.UDFs._
import org.main.scla_dep_mgmt_change.config.Context
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._

object PERF_ORDERBY {

  def apply(context: Context, in: DataFrame): DataFrame =
    in.orderBy(col("c_complex_expression_1").asc,
               col("c_complex_expression_2").desc,
               col("first_name").asc,
               col("c_short").desc
    )

}
