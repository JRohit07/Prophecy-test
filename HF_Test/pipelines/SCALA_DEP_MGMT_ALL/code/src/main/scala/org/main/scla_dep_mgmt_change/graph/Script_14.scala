package org.main.scla_dep_mgmt_change.graph

import io.prophecy.libs._
import org.main.scla_dep_mgmt_change.config.Context
import org.main.scla_dep_mgmt_change.udfs.UDFs._
import org.main.scla_dep_mgmt_change.udfs._
import org.main.scla_dep_mgmt_change.udfs.PipelineInitCode._
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._

object Script_14 {
  def apply(context: Context, in0: DataFrame): DataFrame = {
    val spark = context.spark
    val Config = context.config
    import org.apache.spark.rdd.RDD
    import org.apache.spark.mllib.linalg.{Vector, Vectors}
    import org.apache.spark.mllib.linalg.distributed.RowMatrix
    import org.apache.spark.mllib.linalg.distributed.{BlockMatrix, CoordinateMatrix, MatrixEntry}
    import spark.implicits._
    
    // val rows: RDD[Vector] = sc.parallelize(Array(Vectors.dense(12.0, -51.0, 4.0), Vectors.dense(6.0, 167.0, -68.0), Vectors.dense(-4.0, 24.0, -41.0))) // an RDD of local vectors
    // val matRow: RowMatrix = new RowMatrix(rows)
    // val m = matRow.numRows()
    // val n = matRow.numCols()
    // // QR decomposition 
    // val qrResult = matRow.tallSkinnyQR(true)
    
    // val entries: RDD[MatrixEntry] = sc.parallelize(Array(MatrixEntry(0, 0, 1.2), MatrixEntry(1, 0, 2.1), MatrixEntry(6, 1, 3.7))) // an RDD of matrix entries
    // val matCoordinated: CoordinateMatrix = new CoordinateMatrix(entries)
    
    // val entriesBlock: RDD[MatrixEntry] = sc.parallelize(Array(MatrixEntry(0, 0, 1.2), MatrixEntry(1, 0, 2.1), MatrixEntry(6, 1, 3.7))) // an RDD of matrix entries
    // val coordMat: CoordinateMatrix = new CoordinateMatrix(entriesBlock)
    // val matBlock: BlockMatrix = coordMat.toBlockMatrix()
    
    val out0=in0
    out0
  }

}
