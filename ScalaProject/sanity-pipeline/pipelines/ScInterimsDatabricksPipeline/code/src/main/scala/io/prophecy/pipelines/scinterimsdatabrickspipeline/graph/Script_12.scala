package io.prophecy.pipelines.scinterimsdatabrickspipeline.graph

import io.prophecy.libs._
import io.prophecy.pipelines.scinterimsdatabrickspipeline.config.Context
import io.prophecy.pipelines.scinterimsdatabrickspipeline.udfs.UDFs._
import io.prophecy.pipelines.scinterimsdatabrickspipeline.udfs._
import io.prophecy.pipelines.scinterimsdatabrickspipeline.udfs.PipelineInitCode._
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._

object Script_12 {
  def apply(context: Context): DataFrame = {
    val spark = context.spark
    val Config = context.config
    import spark.implicits._
    val out0 = Seq(
      (Config.CONFIG_INT, Config.CONFIG_STR),
      (64, "hello"),
      (-27, "transistor")
    ).toDF("c_number", "c_string")
    out0
  }

}
