package com.scala.main.job1.graph

import io.prophecy.libs._
import com.scala.main.job1.config.Context
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._

object src_parquet_all_type_and_partition_withspacehyphens1 {

  def apply(context: Context): DataFrame =
    context.spark.read
      .format("csv")
      .option("header", true)
      .option("sep",    ",")
      .schema(
        StructType(
          Array(
            StructField("c   short  --",     StringType,          true),
            StructField("c-int-column type", StringType,          true),
            StructField("-- c-long",         StringType,          true),
            StructField("c-decimal",         StringType,          true),
            StructField("c  float",          StringType,          true),
            StructField("c--boolean",        StringType,          true),
            StructField("c- - -double",      StringType,          true),
            StructField("c___-- string",     StringType,          true),
            StructField("c  date",           StringType,          true),
            StructField("c_timestamp",       StringType,          true),
            StructField("c_decimal",         DecimalType(20, 10), true)
          )
        )
      )
      .load("dbfs:/Prophecy/qa_data/csv/special_char_column_name")

}
