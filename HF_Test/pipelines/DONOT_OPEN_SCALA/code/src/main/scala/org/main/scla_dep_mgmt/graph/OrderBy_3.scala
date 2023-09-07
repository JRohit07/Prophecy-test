package org.main.scla_dep_mgmt.graph

import io.prophecy.libs._
import org.main.scla_dep_mgmt.udfs.UDFs._
import org.main.scla_dep_mgmt.config.Context
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._

object OrderBy_3 {

  def apply(context: Context, in: DataFrame): DataFrame =
    in.orderBy(col("c1").asc,
               col("c2").asc,
               col("c3").asc,
               col("c4").asc,
               col("c5").asc,
               col("c6").asc,
               col("c7").asc,
               col("c8").asc,
               col("c9_udf1").asc,
               col("c9_udf2").asc
    )

}
