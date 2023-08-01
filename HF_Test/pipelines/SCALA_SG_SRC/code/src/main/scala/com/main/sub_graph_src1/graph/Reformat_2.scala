package com.main.sub_graph_src1.graph

import io.prophecy.libs._
import com.main.sub_graph_src1.udfs.PipelineInitCode._
import com.main.sub_graph_src1.udfs.UDFs._
import com.main.sub_graph_src1.config.Context
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._

object Reformat_2 {

  def apply(context: Context, in: DataFrame): DataFrame =
    in.select(col("`c- short`").as("c- short"),
              col("`c  - int`").as("c  - int")
    )

}
