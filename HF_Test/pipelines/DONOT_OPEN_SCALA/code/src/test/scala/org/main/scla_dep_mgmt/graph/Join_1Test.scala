package org.main.scla_dep_mgmt.graph

import com.holdenkarau.spark.testing.DataFrameSuiteBase
import org.main.scla_dep_mgmt.config._
import io.prophecy.libs.registerAllUDFs
import io.prophecy.libs.SparkTestingUtils._
import org.apache.spark.sql.types._
import org.apache.spark.sql.{Column, DataFrame}
import org.apache.spark.sql.functions._
import org.junit.runner.RunWith
import org.junit.Assert
import org.scalatest.FunSuite
import java.time.LocalDateTime
import org.scalatest.junit.JUnitRunner
import java.sql.{Date, Timestamp}
import scala.collection.JavaConverters._
import java.nio.file.{Files, Paths}
import java.math.BigDecimal

@RunWith(classOf[JUnitRunner])
class Join_1Test extends FunSuite with DataFrameSuiteBase {
  import sqlContext.implicits._
  var context: Context = null

  test("Unit Test 0") {

    val dfIn0 = createDfFromResourceFiles(
      spark,
      "/data/org/main/scla_dep_mgmt/graph/Join_1/in0/schema.json",
      "/data/org/main/scla_dep_mgmt/graph/Join_1/in0/data/unit_test_0.json",
      "in0"
    )
    val dfIn1 = createDfFromResourceFiles(
      spark,
      "/data/org/main/scla_dep_mgmt/graph/Join_1/in1/schema.json",
      "/data/org/main/scla_dep_mgmt/graph/Join_1/in1/data/unit_test_0.json",
      "in1"
    )
    val dfOut = createDfFromResourceFiles(
      spark,
      "/data/org/main/scla_dep_mgmt/graph/Join_1/out/schema.json",
      "/data/org/main/scla_dep_mgmt/graph/Join_1/out/data/unit_test_0.json",
      "out"
    )

    val dfOutComputed =
      org.main.scla_dep_mgmt.graph.Join_1(context, dfIn0, dfIn1)
    val res = assertDFEquals(
      dfOut.select(
        "c   short  --",
        "c-int-column type",
        "-- c-long",
        "c-decimal",
        "c  float",
        "c--boolean",
        "c- - -double",
        "c___-- string",
        "c  date",
        "c_timestamp",
        "c   short  --",
        "c-int-column type",
        "-- c-long",
        "c-decimal",
        "c  float",
        "c--boolean",
        "c- - -double",
        "c___-- string",
        "c  date",
        "c_timestamp"
      ),
      dfOutComputed.select(
        "c   short  --",
        "c-int-column type",
        "-- c-long",
        "c-decimal",
        "c  float",
        "c--boolean",
        "c- - -double",
        "c___-- string",
        "c  date",
        "c_timestamp",
        "c   short  --",
        "c-int-column type",
        "-- c-long",
        "c-decimal",
        "c  float",
        "c--boolean",
        "c- - -double",
        "c___-- string",
        "c  date",
        "c_timestamp"
      ),
      maxUnequalRowsToShow,
      1.0
    )
    val msg = if (res.isLeft) res.left.get.getMessage else ""
    Assert.assertTrue(msg, res.isRight)
  }

  override def beforeAll() = {
    super.beforeAll()
    spark.conf.set("spark.sql.legacy.allowUntypedScalaUDF", "true")
    registerAllUDFs(spark)

    val fabricName = System.getProperty("fabric")

    val config = ConfigurationFactoryImpl.fromCLI(
      Array("--confFile",
            getClass.getResource(s"/config/${fabricName}.json").getPath
      )
    )

    context = Context(spark, config)

    val dfMain_scla_dep_mgmt_graph_all_type_scala_sg_1_Lookup_1_1 =
      createDfFromResourceFiles(
        spark,
        "/data/org/main/scla_dep_mgmt/graph/all_type_scala_sg_1/Lookup_1_1/schema.json",
        "/data/org/main/scla_dep_mgmt/graph/all_type_scala_sg_1/Lookup_1_1/data.json",
        port = "in"
      )
    org.main.scla_dep_mgmt.graph.all_type_scala_sg_1.Lookup_1_1(
      org.main.scla_dep_mgmt.graph.all_type_scala_sg_1.config
        .Context(context.spark, context.config.all_type_scala_sg_1),
      dfMain_scla_dep_mgmt_graph_all_type_scala_sg_1_Lookup_1_1
    )
  }

}
