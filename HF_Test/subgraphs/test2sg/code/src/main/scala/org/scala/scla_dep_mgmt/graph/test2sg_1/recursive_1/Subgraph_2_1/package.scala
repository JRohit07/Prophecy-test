package org.scala.scla_dep_mgmt.graph.test2sg_1.recursive_1

import io.prophecy.libs._
import org.main.scla_dep_mgmt.graph.test2sg_1.recursive_1.Subgraph_2_1.Subgraph_3_1
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._
package object Subgraph_2_1 {

  def apply(spark: SparkSession, in0: DataFrame): DataFrame = {
    val df_Subgraph_3_1 = Subgraph_3_1.apply(spark, in0)
    val df_Reformat_4_1 = Reformat_4_1(spark,       df_Subgraph_3_1)
    df_Reformat_4_1
  }

}
