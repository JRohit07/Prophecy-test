package com.scala.main.job1.graph

import io.prophecy.libs._
import com.scala.main.job1.graph.Subgraph_3.config._
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._
package object Subgraph_3 {

  def apply(context: Context, in0: DataFrame): DataFrame = {
    val df_Reformat_6 = Reformat_6(context, in0)
    df_Reformat_6
  }

}
