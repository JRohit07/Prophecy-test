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

object Reformat_8 {

  def apply(context: Context, in: DataFrame): DataFrame =
    in.select(
      col("customer_id"),
      col("last_name"),
      col("first_name"),
      col("phone"),
      col("account_open_date"),
      col("email"),
      col("country_code"),
      col("account_flags"),
      lookup("Lookup_1", col("customer_id"), col("first_name"))
        .getField("email")
        .as("lookup1")
    )

}
