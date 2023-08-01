package io.prophecy.pipelines.perf_unitest_generate.graph

import com.holdenkarau.spark.testing.DataFrameSuiteBase
import io.prophecy.pipelines.perf_unitest_generate.config._
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
class FlattenSchema_1Test extends FunSuite with DataFrameSuiteBase {
  import sqlContext.implicits._
  var context: Context = null

  test("Unit Test 0") {

    val dfIn = createDfFromResourceFiles(
      spark,
      "/data/io/prophecy/pipelines/perf_unitest_generate/graph/FlattenSchema_1/in/schema.json",
      "/data/io/prophecy/pipelines/perf_unitest_generate/graph/FlattenSchema_1/in/data/unit_test_0.json",
      "in"
    )
    val dfOut = createDfFromResourceFiles(
      spark,
      "/data/io/prophecy/pipelines/perf_unitest_generate/graph/FlattenSchema_1/out/schema.json",
      "/data/io/prophecy/pipelines/perf_unitest_generate/graph/FlattenSchema_1/out/data/unit_test_0.json",
      "out"
    )

    val dfOutComputed = io.prophecy.pipelines.perf_unitest_generate.graph
      .FlattenSchema_1(context, dfIn)
    val res =
      assertDFEquals(dfOut.select("account_flags",         "account_open_date"),
                     dfOutComputed.select("account_flags", "account_open_date"),
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

    val config = ConfigurationFactoryImpl.getConfig(
      Array("--confFile",
            getClass.getResource(s"/config/${fabricName}.json").getPath
      )
    )

    context = Context(spark, config)

    val dfProphecy_pipelines_perf_unitest_generate_graph_Lookup_1 =
      createDfFromResourceFiles(
        spark,
        "/data/io/prophecy/pipelines/perf_unitest_generate/graph/Lookup_1/schema.json",
        "/data/io/prophecy/pipelines/perf_unitest_generate/graph/Lookup_1/data.json",
        port = "in"
      )
    io.prophecy.pipelines.perf_unitest_generate.graph.Lookup_1(
      context,
      dfProphecy_pipelines_perf_unitest_generate_graph_Lookup_1
    )
  }

}
