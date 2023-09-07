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

object UTGenAllType {

  def apply(context: Context, in: DataFrame): DataFrame =
    in.select(
      col("`c- short`").as("c- short"),
      col("`c  - int`").as("c  - int"),
      col("`- c long`").as("- c long"),
      col("`c_decimal  -  `").as("c_decimal  -  "),
      col("`c_float-__  `").as("c_float-__  "),
      col("`c -  boolean _  `").as("c -  boolean _  "),
      col("c_double"),
      col("`c-string`").as("c-string"),
      col("`c_date-for today`").as("c_date-for today"),
      col("`c_timestamp  __ for--today`").as("c_timestamp  __ for--today"),
      col("`c-bytes`").as("c-bytes"),
      col("`c-binary`").as("c-binary"),
      col("p_date")
    )

}
