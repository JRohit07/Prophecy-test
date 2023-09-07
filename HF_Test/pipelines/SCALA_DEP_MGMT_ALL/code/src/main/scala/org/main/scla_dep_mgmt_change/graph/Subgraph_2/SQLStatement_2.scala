package org.main.scla_dep_mgmt_change.graph.Subgraph_2

import io.prophecy.libs._
import org.main.scla_dep_mgmt_change.udfs.PipelineInitCode._
import org.main.scla_dep_mgmt_change.udfs.UDFs._
import org.main.scla_dep_mgmt_change.graph.Subgraph_2.config.Context
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._

object SQLStatement_2 {

  def apply(
    context: Context,
    in0:     DataFrame,
    in1:     DataFrame,
    in2:     DataFrame,
    in3:     DataFrame,
    in4:     DataFrame,
    in5:     DataFrame,
    in6:     DataFrame,
    in7:     DataFrame
  ): (
    DataFrame,
    DataFrame,
    DataFrame,
    DataFrame,
    DataFrame,
    DataFrame,
    DataFrame,
    DataFrame
  ) = {
    in0.createOrReplaceTempView("in0")
    in1.createOrReplaceTempView("in1")
    in2.createOrReplaceTempView("in2")
    in3.createOrReplaceTempView("in3")
    in4.createOrReplaceTempView("in4")
    in5.createOrReplaceTempView("in5")
    in6.createOrReplaceTempView("in6")
    in7.createOrReplaceTempView("in7")
    (context.spark.sql("select in0.c_array_int as c_int from in0 limit 10"),
     context.spark.sql("select in1.`c  - int` as c_int from in1 limit 10"),
     context.spark.sql("select in2.`c  - int` as c_int from in2 limit 10"),
     context.spark.sql("select cast(in3.c8_c1 as int) from in3 limit 10"),
     context.spark.sql("select cast(in4.c8_c1 as int) from in4 limit 10"),
     context.spark.sql("select in5.`c   short  --` as c_int from in5 limit 10"),
     context.spark.sql("select cast(in6.customer_id as int) from in6 limit 10"),
     context.spark.sql(
       "select cast(in7.`c   short  --` as int) from in7 limit 10"
     )
    )
  }

}
