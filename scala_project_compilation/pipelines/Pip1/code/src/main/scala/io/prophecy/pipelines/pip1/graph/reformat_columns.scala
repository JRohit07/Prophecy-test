package io.prophecy.pipelines.pip1.graph

import io.prophecy.libs._
import io.prophecy.pipelines.pip1.functions.PipelineInitCode._
import io.prophecy.pipelines.pip1.functions.UDFs._
import io.prophecy.pipelines.pip1.config.Context
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._

object reformat_columns {

  def apply(context: Context, in: DataFrame): DataFrame =
    in.select(col("_c0rdsthestahsrth").as("_c0"),
              col("_c1"),
              col("_c2"),
              col("_c3"),
              col("_c4"),
              col("_c5"),
              col("_c6"),
              col("_c7"),
              col("_c8"),
              col("_c9")
    )

}
