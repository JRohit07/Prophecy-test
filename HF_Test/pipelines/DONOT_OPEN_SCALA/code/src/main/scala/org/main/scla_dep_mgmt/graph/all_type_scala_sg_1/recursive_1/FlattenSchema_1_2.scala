package org.main.scla_dep_mgmt.graph.all_type_scala_sg_1.recursive_1

import io.prophecy.libs._
import org.main.scla_dep_mgmt.udfs.UDFs._
import org.main.scla_dep_mgmt.graph.all_type_scala_sg_1.recursive_1.config.Context
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._

object FlattenSchema_1_2 {

  def apply(context: Context, in: DataFrame): DataFrame =
    in.withColumn("c_complex-array", explode_outer(col("c_complex-array")))
      .withColumn("c_complex-array-Diabetes",
                  explode_outer(col("c_complex-array.Diabetes"))
      )
      .withColumn("c_complex-struct-problems",
                  explode_outer(col("c_complex-struct.problems"))
      )
      .withColumn("c_complex-array-Diabetes-medications",
                  explode_outer(col("c_complex-array-Diabetes.medications"))
      )
      .withColumn("c_complex-struct-problems-Diabetes",
                  explode_outer(col("c_complex-struct-problems.Diabetes"))
      )
      .withColumn(
        "c_complex-array-Diabetes-medications-medicationsClasses",
        explode_outer(
          col("c_complex-array-Diabetes-medications.medicationsClasses")
        )
      )
      .withColumn(
        "c_complex-struct-problems-Diabetes-medications",
        explode_outer(col("c_complex-struct-problems-Diabetes.medications"))
      )
      .withColumn(
        "c_complex-array-Diabetes-medications-medicationsClasses-className_1",
        explode_outer(
          col(
            "c_complex-array-Diabetes-medications-medicationsClasses.className_1"
          )
        )
      )
      .withColumn(
        "c_complex-struct-problems-Diabetes-medications-medicationsClasses",
        explode_outer(
          col(
            "c_complex-struct-problems-Diabetes-medications.medicationsClasses"
          )
        )
      )
      .withColumn(
        "c_complex-array-Diabetes-medications-medicationsClasses-className_1-associated-Drug",
        explode_outer(
          col(
            "c_complex-array-Diabetes-medications-medicationsClasses-className_1.associated-Drug"
          )
        )
      )
      .withColumn(
        "c_complex-struct-problems-Diabetes-medications-medicationsClasses-className_1",
        explode_outer(
          col(
            "c_complex-struct-problems-Diabetes-medications-medicationsClasses.className_1"
          )
        )
      )
      .withColumn(
        "c_complex-struct-problems-Diabetes-medications-medicationsClasses-className_1-associated-Drug",
        explode_outer(
          col(
            "c_complex-struct-problems-Diabetes-medications-medicationsClasses-className_1.associated-Drug"
          )
        )
      )
      .select(
        col("c_int").as("c_int.test.value1"),
        col(
          "c_complex-array-Diabetes-medications-medicationsClasses-className_1-associated-Drug.name"
        ).as("c_int.test.value1.complex-array1.diabetes"),
        col("c_complex-struct-problems-Diabetes.medications")
          .as("c_int.test.value1.complex-struct1.diabetes.medication"),
        col(
          "c_complex-struct-problems-Diabetes-medications-medicationsClasses-className_1-associated-Drug.cf-use"
        ).as("c_int.test.value1.complex-struct1.diabetes.medication.cfuse")
      )

}
