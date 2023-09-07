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

object RowDistributor_1_1_1 {

  def apply(context: Context, in: DataFrame): (DataFrame, DataFrame) =
    (in.filter(!col("cmls_3ds_authntn_mthd").like("%mister transistor%")),
     in.filter(col("cmls_acct_cobrnd_bus_id_drvd") > lit(-100))
    )

}
