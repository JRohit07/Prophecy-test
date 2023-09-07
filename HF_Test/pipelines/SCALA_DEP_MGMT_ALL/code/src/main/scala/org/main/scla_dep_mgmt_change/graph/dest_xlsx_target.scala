package org.main.scla_dep_mgmt_change.graph

import io.prophecy.libs._
import org.main.scla_dep_mgmt_change.config.Context
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._

object dest_xlsx_target {

  def apply(context: Context, in: DataFrame): Unit =
    in.write
      .format("excel")
      .option("header", true)
      .mode("overwrite")
      .mode("overwrite")
      .save("dbfs:/tmp/e2e/xlsx/targetdata")

}
