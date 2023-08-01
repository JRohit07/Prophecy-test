package org.main.scla_dep_mgmt_change.graph.all_type_sg_scala_main

import io.prophecy.libs._
import org.main.scla_dep_mgmt_change.graph.all_type_sg_scala_main.config.Context
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._

object scala_random_target_subgraph_donotuse {

  def apply(context: Context, in: DataFrame): Unit =
    in.write
      .format("parquet")
      .mode("overwrite")
      .save("dbfs:/tmp/e2e/scala_random_target_subgraph_donotuse")

}
