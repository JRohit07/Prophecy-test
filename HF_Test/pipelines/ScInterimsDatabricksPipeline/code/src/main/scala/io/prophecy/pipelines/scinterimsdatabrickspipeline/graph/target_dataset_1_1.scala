package io.prophecy.pipelines.scinterimsdatabrickspipeline.graph

import io.prophecy.libs._
import io.prophecy.pipelines.scinterimsdatabrickspipeline.config.Context
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._

object target_dataset_1_1 {

  def apply(context: Context, in: DataFrame): Unit =
    in.write
      .format("parquet")
      .mode("overwrite")
      .save("dbfs:/tmp/dest_db_livy_2")

}
