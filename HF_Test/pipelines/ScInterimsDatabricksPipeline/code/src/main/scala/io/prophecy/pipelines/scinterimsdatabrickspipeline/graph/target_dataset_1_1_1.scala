package io.prophecy.pipelines.scinterimsdatabrickspipeline.graph

import io.prophecy.libs._
import io.prophecy.pipelines.scinterimsdatabrickspipeline.config.Context
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._

object target_dataset_1_1_1 {

  def apply(context: Context, in: DataFrame): Unit = {
    import org.apache.avro.Schema
    var writer = in.write.format("avro")
    writer = writer
    writer = writer.mode("overwrite")
    writer.save("dbfs:/tmp/dest_db_livy_3")
  }

}
