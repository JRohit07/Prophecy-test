package com.scala.main.job12.graph.Subgraph_4

import io.prophecy.libs._
import com.scala.main.job12.graph.Subgraph_4.Subgraph_5.config._
import com.scala.main.job12.graph.Subgraph_4.Subgraph_5.config.Config.interimOutput
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._
package object Subgraph_5 {

  def apply(context: Context, in0: DataFrame): DataFrame = {
    val df_Reformat_9 = Reformat_9(context, in0).interim(
      "Subgraph_5",
      "9iZcTlU3jK0PK6nA6ey38$$9FPV5bstUFv3se8qg-gXt",
      "aB4ngRhUTbczS1X0ANap4$$unaQOXsoNkqzpuhp_yfc9"
    )
    df_Reformat_9
  }

}
