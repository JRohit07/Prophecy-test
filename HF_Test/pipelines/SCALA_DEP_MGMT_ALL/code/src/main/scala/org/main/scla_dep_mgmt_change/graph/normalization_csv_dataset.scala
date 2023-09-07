package org.main.scla_dep_mgmt_change.graph

import io.prophecy.libs._
import org.main.scla_dep_mgmt_change.config.Context
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._

object normalization_csv_dataset {

  def apply(context: Context): DataFrame =
    context.spark.read
      .format("csv")
      .option("header", true)
      .option("sep",    ",")
      .schema(
        StructType(
          Array(
            StructField("Y_Value_of_Occupied_Homes",      DoubleType, true),
            StructField("Crime_Rate",                     DoubleType, true),
            StructField("Residential_Land_Zone",          DoubleType, true),
            StructField("Non_retail_Business_acres",      DoubleType, true),
            StructField("Charles_River",                  DoubleType, true),
            StructField("Nitric_Oxide",                   DoubleType, true),
            StructField("Average_Rooms",                  DoubleType, true),
            StructField("Owner_Occupied_Units",           DoubleType, true),
            StructField("Distance_to_Employment_Centers", DoubleType, true),
            StructField("Accessibility_to_Highways",      DoubleType, true),
            StructField("Property_Tax_Rate",              DoubleType, true),
            StructField("Pupil_Teacher_Ratio",            DoubleType, true),
            StructField("Lower_Status",                   DoubleType, true)
          )
        )
      )
      .load("dbfs:/Prophecy/qa_data/csv/normalizationdata/normalization.csv")

}
