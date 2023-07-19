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

object Reformat_3 {

  def apply(context: Context, in: DataFrame): DataFrame =
    in.select(col("`c   short  --`").as("c   short  --"),
              col("`c   short  --`").as("c_next")
    )

}
