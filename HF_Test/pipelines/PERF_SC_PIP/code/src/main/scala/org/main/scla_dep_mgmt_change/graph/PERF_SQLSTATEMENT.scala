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

object PERF_SQLSTATEMENT {

  def apply(context: Context, in0: DataFrame): DataFrame = {
    in0.createOrReplaceTempView("in0")
    context.spark.sql("select * from in0 where first_name not like '%123%'")
  }

}
