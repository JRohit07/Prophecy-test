package org.main.scla_dep_mgmt_change.graph

import io.prophecy.libs._
import org.main.scla_dep_mgmt_change.udfs.PipelineInitCode._
import org.main.scla_dep_mgmt_change.udfs.UDFs._
import org.main.scla_dep_mgmt_change.config.Context
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._

object Reformat_3_1 {

  def apply(context: Context, in: DataFrame): DataFrame =
    in.select(udf_matrices_test().as("c_udf_matrices"),
              udf_vectors_test().as("c_udf_vectors"),
              udf_matrix_test(udf_matrices_test()).as("c_udf_matrix")
    )

}
