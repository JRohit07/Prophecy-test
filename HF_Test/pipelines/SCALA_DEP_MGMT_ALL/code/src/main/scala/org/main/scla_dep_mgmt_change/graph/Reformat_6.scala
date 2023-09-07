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

object Reformat_6 {

  def apply(context: Context, in: DataFrame): DataFrame =
    in.select(
      concat(col("`c_struct.test1.mainstruct`.a.test1.`test- another`"),
             col("`c_struct.test1.mainstruct`.b.test1.`test- another`")
      ).as("c1"),
      col("`nested.field.customer_id`").as("customer_id"),
      col("`nested.field.first_name`").as("first_name")
    )

}
