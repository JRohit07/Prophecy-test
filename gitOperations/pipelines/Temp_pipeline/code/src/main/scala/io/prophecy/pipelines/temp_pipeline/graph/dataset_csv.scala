package io.prophecy.pipelines.temp_pipeline.graph

import io.prophecy.libs._
import io.prophecy.pipelines.temp_pipeline.config.Context
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._

object dataset_csv {

  def apply(context: Context): DataFrame =
    context.spark.read
      .format("csv")
      .option("header", false)
      .option("sep",    ",")
      .schema(
        StructType(
          Array(
            StructField("_c0", StringType, true),
            StructField("_c1", StringType, true),
            StructField("_c2", StringType, true),
            StructField("_c3", StringType, true),
            StructField("_c4", StringType, true),
            StructField("_c5", StringType, true),
            StructField("_c6", StringType, true),
            StructField("_c7", StringType, true),
            StructField("_c8", StringType, true),
            StructField("_c9", StringType, true)
          )
        )
      )
      .load("dbfs:/Prophecy/qa_data/csv/all_type_no_partition")

}
