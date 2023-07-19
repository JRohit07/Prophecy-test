package org.main.scla_dep_mgmt_change.graph

import io.prophecy.libs._
import org.main.scla_dep_mgmt_change.config.Context
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._

object src_xlsx_main {

  def apply(context: Context): DataFrame = {
    var reader = context.spark.read
      .format("excel")
      .option("header",      true)
      .option("dataAddress", "'Sheet1'!B1:G20")
    if (
      StructType(
        Array(
          StructField("Region",   StringType, true),
          StructField("Rep",      StringType, true),
          StructField("Item",     StringType, true),
          StructField("Units",    StringType, true),
          StructField("UnitCost", StringType, true),
          StructField("Total",    StringType, true)
        )
      ).fields.nonEmpty
    )
      reader = reader.schema(
        StructType(
          Array(
            StructField("Region",   StringType, true),
            StructField("Rep",      StringType, true),
            StructField("Item",     StringType, true),
            StructField("Units",    StringType, true),
            StructField("UnitCost", StringType, true),
            StructField("Total",    StringType, true)
          )
        )
      )
    reader.load(
      "dbfs:/Prophecy/qa_data/xlsx/office_supply_sales/office_supply_sales.xlsx"
    )
  }

}
