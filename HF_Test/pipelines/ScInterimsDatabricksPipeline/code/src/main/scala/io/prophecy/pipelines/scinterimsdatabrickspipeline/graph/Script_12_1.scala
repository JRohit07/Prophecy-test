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

object Script_12_1 {
  def apply(context: Context): DataFrame = {
    val spark = context.spark
    val Config = context.config
    // import spark.implicits._
    // val out0 = Seq(
    //   (Config.CONFIG_INT, Config.CONFIG_STR, 10.12),
    //   (64, Config.c_record_complex.cr_string, -100),
    //   (-27, Config.c_array_complex(0).car_string, -10.2323)
    // ).toDF("c_number", "c_string", "c_float")
    
    import spark.implicits._
    val jsonStr = s"""[{"id": ${Config.CONFIG_INT},"type":"donut","name":"BlackForest","ppu":0.55,"batters":{"batter":[{"id":"1001","type":"Regular"},{"id":"1002","type":"Chocolate"},{"id":"1003","type":"${Config.CONFIG_STR}"},{"id":"1004","type":"Devil's Food"}]},"topping":[{"id":"5001","type":"None"},{"id":"5002","type":"Glazed"},{"id":"5005","type":"Sugar"},{"id":"5007","type":"Powdered Sugar"},{"id":"5006","type":"Chocolate with Sprinkles"},{"id":"5003","type":"Chocolate"},{"id":"5004","type":"Maple"}]},{"id":2,"type":"donut","name":"Blueberry","ppu":0.59,"batters":{"batter":[{"id":"1001","type":"Regular"},{"id":"1003","type":"Blueberry"},{"id":"1004","type":"Devil's Food"}]},"topping":[{"id":"5001","type":"None"},{"id":"5002","type":"Glazed"},{"id":"5005","type":"Sugar"},{"id":"5007","type":"Powdered Sugar"},{"id":"5006","type":"Chocolate with Sprinkles"},{"id":"5003","type":"Chocolate"},{"id":"5004","type":"Maple"}]}]"""
    val out0 = spark.read.json(Seq(jsonStr).toDS)
    out0
  }

}
