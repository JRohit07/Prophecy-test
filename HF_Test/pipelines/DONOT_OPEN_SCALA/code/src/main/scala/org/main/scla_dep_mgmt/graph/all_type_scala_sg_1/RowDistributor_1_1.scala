package org.main.scla_dep_mgmt.graph.all_type_scala_sg_1

import io.prophecy.libs._
import org.main.scla_dep_mgmt.udfs.UDFs._
import org.main.scla_dep_mgmt.graph.all_type_scala_sg_1.config.Context
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._

object RowDistributor_1_1 {

  def apply(context: Context, in: DataFrame): (DataFrame, DataFrame) =
    (in.filter(expr(context.config.c_sg1_c_rowdistributor)),
     in.filter(col("`c  - int`") > lit(-100))
    )

}
