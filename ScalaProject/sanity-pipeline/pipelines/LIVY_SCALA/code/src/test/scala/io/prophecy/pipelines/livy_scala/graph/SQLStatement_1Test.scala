package io.prophecy.pipelines.livy_scala.graph

import com.holdenkarau.spark.testing.DataFrameSuiteBase
import io.prophecy.pipelines.livy_scala.config._
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
class SQLStatement_1Test extends FunSuite with DataFrameSuiteBase {
  import sqlContext.implicits._
  var context: Context = null

  test("Unit Test 0") {

    val dfInput_0 = createDfFromResourceFiles(
      spark,
      "/data/io/prophecy/pipelines/livy_scala/graph/SQLStatement_1/input_0/schema.json",
      "/data/io/prophecy/pipelines/livy_scala/graph/SQLStatement_1/input_0/data/unit_test_0.json",
      "input_0"
    )
    val dfOut2 = createDfFromResourceFiles(
      spark,
      "/data/io/prophecy/pipelines/livy_scala/graph/SQLStatement_1/out2/schema.json",
      "/data/io/prophecy/pipelines/livy_scala/graph/SQLStatement_1/out2/data/unit_test_0.json",
      "out2"
    )
    val dfOut = createDfFromResourceFiles(
      spark,
      "/data/io/prophecy/pipelines/livy_scala/graph/SQLStatement_1/out/schema.json",
      "/data/io/prophecy/pipelines/livy_scala/graph/SQLStatement_1/out/data/unit_test_0.json",
      "out"
    )
    val dfOut3 = createDfFromResourceFiles(
      spark,
      "/data/io/prophecy/pipelines/livy_scala/graph/SQLStatement_1/out3/schema.json",
      "/data/io/prophecy/pipelines/livy_scala/graph/SQLStatement_1/out3/data/unit_test_0.json",
      "out3"
    )
    val dfOut1 = createDfFromResourceFiles(
      spark,
      "/data/io/prophecy/pipelines/livy_scala/graph/SQLStatement_1/out1/schema.json",
      "/data/io/prophecy/pipelines/livy_scala/graph/SQLStatement_1/out1/data/unit_test_0.json",
      "out1"
    )

    val (dfOutComputed, dfOut1Computed, dfOut2Computed, dfOut3Computed) =
      io.prophecy.pipelines.livy_scala.graph.SQLStatement_1(context, dfInput_0)
    val resOut2 = assertDFEquals(
      dfOut2.select("year",
                    "industry_code_ANZSIC",
                    "industry_name_ANZSIC",
                    "rme_size_grp",
                    "variable",
                    "value",
                    "unit"
      ),
      dfOut2Computed.select("year",
                            "industry_code_ANZSIC",
                            "industry_name_ANZSIC",
                            "rme_size_grp",
                            "variable",
                            "value",
                            "unit"
      ),
      maxUnequalRowsToShow,
      1.0
    )
    val msgOut2 = if (resOut2.isLeft) resOut2.left.get.getMessage else ""
    Assert.assertTrue(msgOut2, resOut2.isRight)
    val resOut = assertDFEquals(
      dfOut.select("year",
                   "industry_code_ANZSIC",
                   "industry_name_ANZSIC",
                   "rme_size_grp",
                   "variable",
                   "value",
                   "unit"
      ),
      dfOutComputed.select("year",
                           "industry_code_ANZSIC",
                           "industry_name_ANZSIC",
                           "rme_size_grp",
                           "variable",
                           "value",
                           "unit"
      ),
      maxUnequalRowsToShow,
      1.0
    )
    val msgOut = if (resOut.isLeft) resOut.left.get.getMessage else ""
    Assert.assertTrue(msgOut, resOut.isRight)
    val resOut3 = assertDFEquals(
      dfOut3.select("year",
                    "industry_code_ANZSIC",
                    "industry_name_ANZSIC",
                    "rme_size_grp",
                    "variable",
                    "value",
                    "unit"
      ),
      dfOut3Computed.select("year",
                            "industry_code_ANZSIC",
                            "industry_name_ANZSIC",
                            "rme_size_grp",
                            "variable",
                            "value",
                            "unit"
      ),
      maxUnequalRowsToShow,
      1.0
    )
    val msgOut3 = if (resOut3.isLeft) resOut3.left.get.getMessage else ""
    Assert.assertTrue(msgOut3, resOut3.isRight)
    val resOut1 = assertDFEquals(
      dfOut1.select("year",
                    "industry_code_ANZSIC",
                    "industry_name_ANZSIC",
                    "rme_size_grp",
                    "variable",
                    "value",
                    "unit"
      ),
      dfOut1Computed.select("year",
                            "industry_code_ANZSIC",
                            "industry_name_ANZSIC",
                            "rme_size_grp",
                            "variable",
                            "value",
                            "unit"
      ),
      maxUnequalRowsToShow,
      1.0
    )
    val msgOut1 = if (resOut1.isLeft) resOut1.left.get.getMessage else ""
    Assert.assertTrue(msgOut1, resOut1.isRight)
  }

  override def beforeAll() = {
    super.beforeAll()
    spark.conf.set("spark.sql.legacy.allowUntypedScalaUDF", "true")
    registerAllUDFs(spark)

    val fabricName = System.getProperty("fabric")

    val config = ConfigurationFactoryImpl.getConfig(
      Array("--confFile",
            getClass.getResource(s"/config/${fabricName}.json").getPath
      )
    )

    context = Context(spark, config)

    val dfProphecy_pipelines_livy_scala_graph_Lookup_1 =
      createDfFromResourceFiles(
        spark,
        "/data/io/prophecy/pipelines/livy_scala/graph/Lookup_1/schema.json",
        "/data/io/prophecy/pipelines/livy_scala/graph/Lookup_1/data.json",
        port = "in"
      )
    io.prophecy.pipelines.livy_scala.graph
      .Lookup_1(context, dfProphecy_pipelines_livy_scala_graph_Lookup_1)
  }

}
