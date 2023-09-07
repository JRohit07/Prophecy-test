package com.scala.main.job12.graph

import io.prophecy.libs._
import com.scala.main.job12.graph.Subgraph_1.Subgraph_2
import com.scala.main.job12.graph.Subgraph_1.Subgraph_2.config.{
  Context => Subgraph_2_Context
}
import com.scala.main.job12.graph.Subgraph_1.config._
import com.scala.main.job12.graph.Subgraph_1.config.Config.interimOutput
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._
package object Subgraph_1 {

  def apply(context: Context, in0: DataFrame): DataFrame = {
    val df_Subgraph_2 = Subgraph_2.apply(
      Subgraph_2_Context(context.spark, context.config.Subgraph_2),
      in0
    )
    df_Subgraph_2
  }

}
