package io.prophecy.pipelines.scinterimsdatabrickspipeline.graph

import io.prophecy.libs._
import io.prophecy.pipelines.scinterimsdatabrickspipeline.config.Context
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._

object target_dataset {

  def apply(context: Context, in: DataFrame): Unit = {
    import _root_.io.delta.tables._
    import org.apache.hadoop.fs.{FileSystem, Path}
    in.write.format("delta").mode("overwrite").save("dbfs:/tmp/dest_db_livy_4")
  }

}
