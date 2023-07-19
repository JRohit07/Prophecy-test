package io.prophecy.pipelines.livy_scala.graph.Subgraph_4.Subgraph_2_1_2.Subgraph_3_1_2

import io.prophecy.libs._
import io.prophecy.pipelines.livy_scala.udfs.PipelineInitCode._
import io.prophecy.pipelines.livy_scala.udfs.UDFs._
import io.prophecy.pipelines.livy_scala.graph.Subgraph_4.Subgraph_2_1_2.Subgraph_3_1_2.config.Context
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._

object Reformat_4_1_2 {

  def apply(context: Context, in: DataFrame): DataFrame =
    in.select(col("year"),
              col("industry_code_ANZSIC"),
              col("industry_name_ANZSIC"),
              col("rme_size_grp"),
              col("variable"),
              col("value"),
              col("unit")
    )

}
