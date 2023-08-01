package org.main.scla_dep_mgmt.graph

import io.prophecy.libs._
import org.main.scla_dep_mgmt.udfs.UDFs._
import org.main.scla_dep_mgmt.config.Context
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._

object Reformat_4 {

  def apply(context: Context, in: DataFrame): DataFrame =
    in.select(
      lookup("Lookup_2", col("p_string"), col("p_long"))
        .getField("c_date-for today")
        .as("col1")
    )

}
