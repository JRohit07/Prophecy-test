package com.scala.main.job12.graph

import io.prophecy.libs._
import com.scala.main.job12.graph.Subgraph_3.config._
import com.scala.main.job12.graph.Subgraph_3.config.Config.interimOutput
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._
package object Subgraph_3 {

  def apply(context: Context, in0: DataFrame): DataFrame = {
    val df_Reformat_6 = Reformat_6(context, in0).interim(
      "Subgraph_3",
      "dpM1a3Ympr8yGGohSD0Pe$$RVUG-hDdhFksN995vtlDw",
      "n5apy_ib4bkma0uwVAv6C$$vwmyRZtgYigXf-7KuTK1O"
    )
    df_Reformat_6
  }

}
