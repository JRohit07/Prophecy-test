package org.main.scla_dep_mgmt_change.graph.PERF_SG

import io.prophecy.libs._
import org.main.scla_dep_mgmt_change.udfs.UDFs._
import org.main.scla_dep_mgmt_change.graph.PERF_SG.config.Context
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._

object Aggregate_1_1_1 {

  def apply(context: Context, in: DataFrame): DataFrame =
    in.groupBy(col("cmls_acct_cobrnd_bus_id_drvd"))
      .agg(first(col("cmls_3ds_authntn_mthd")).as("cmls_3ds_authntn_mthd"),
           first(col("cmls_acct_ctry_cd_drvd")).as("cmls_acct_ctry_cd_drvd")
      )

}
