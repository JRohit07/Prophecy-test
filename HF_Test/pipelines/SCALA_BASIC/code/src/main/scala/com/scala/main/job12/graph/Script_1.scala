package com.scala.main.job12.graph

import io.prophecy.libs._
import com.scala.main.job12.config.Context
import com.scala.main.job12.udfs.UDFs._
import com.scala.main.job12.udfs._
import com.scala.main.job12.udfs.PipelineInitCode._
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._

object Script_1 {
  def apply(context: Context, in0: DataFrame): DataFrame = {
    val spark = context.spark
    val Config = context.config
    print(s"Config: ${Config.c_test}")
    
    Console.print("out stream")
    Console.err.println("err stream")
    
    System.out.print("out stream")
    System.err.print("err stream")
    
    var out0=in0
    out0
  }

}
