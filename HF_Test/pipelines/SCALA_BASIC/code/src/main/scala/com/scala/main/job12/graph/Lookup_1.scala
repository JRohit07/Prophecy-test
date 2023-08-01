package com.scala.main.job12.graph

import io.prophecy.libs._
import com.scala.main.job12.config.Context
import com.scala.main.job12.udfs.UDFs._
import com.scala.main.job12.udfs.PipelineInitCode._
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._

object Lookup_1 {

  def apply(context: Context, in0: DataFrame): Unit =
    createLookup("TestLookup",
                 in0,
                 context.spark,
                 List("c   short  --", "c-int-column type"),
                 "c  float",
                 "c--boolean"
    )

}
