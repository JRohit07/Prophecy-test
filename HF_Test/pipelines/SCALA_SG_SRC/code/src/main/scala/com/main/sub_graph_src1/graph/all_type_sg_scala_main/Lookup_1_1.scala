package com.main.sub_graph_src1.graph.all_type_sg_scala_main

import io.prophecy.libs._
import com.main.sub_graph_src1.graph.all_type_sg_scala_main.config.Context
import com.main.sub_graph_src1.udfs.UDFs._
import com.main.sub_graph_src1.udfs.PipelineInitCode._
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._

object Lookup_1_1 {

  def apply(context: Context, in0: DataFrame): Unit =
    createLookup("LookupTest",
                 in0,
                 context.spark,
                 List("customer_id", "first_name"),
                 "last_name",
                 "phone"
    )

}
