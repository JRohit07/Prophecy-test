package io.prophecy.pipelines.perf_unitest_generate.graph

import com.holdenkarau.spark.testing.DataFrameSuiteBase
import io.prophecy.pipelines.perf_unitest_generate.config._
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
class RowDistributor_1Test extends FunSuite with DataFrameSuiteBase {
  import sqlContext.implicits._
  var context: Context = null

  test("Unit Test 0") {

    val dfIn = createDfFromResourceFiles(
      spark,
      "/data/io/prophecy/pipelines/perf_unitest_generate/graph/RowDistributor_1/in/schema.json",
      "/data/io/prophecy/pipelines/perf_unitest_generate/graph/RowDistributor_1/in/data/unit_test_0.json",
      "in"
    )
    val dfOut1 = createDfFromResourceFiles(
      spark,
      "/data/io/prophecy/pipelines/perf_unitest_generate/graph/RowDistributor_1/out1/schema.json",
      "/data/io/prophecy/pipelines/perf_unitest_generate/graph/RowDistributor_1/out1/data/unit_test_0.json",
      "out1"
    )
    val dfOut0 = createDfFromResourceFiles(
      spark,
      "/data/io/prophecy/pipelines/perf_unitest_generate/graph/RowDistributor_1/out0/schema.json",
      "/data/io/prophecy/pipelines/perf_unitest_generate/graph/RowDistributor_1/out0/data/unit_test_0.json",
      "out0"
    )

    val (dfOut0Computed, dfOut1Computed) =
      io.prophecy.pipelines.perf_unitest_generate.graph
        .RowDistributor_1(context, dfIn)
    val resOut1 = assertDFEquals(
      dfOut1.select("last_name",
                    "account_flags",
                    "account_open_date",
                    "country_code",
                    "customer_id"
      ),
      dfOut1Computed.select("last_name",
                            "account_flags",
                            "account_open_date",
                            "country_code",
                            "customer_id"
      ),
      maxUnequalRowsToShow,
      1.0
    )
    val msgOut1 = if (resOut1.isLeft) resOut1.left.get.getMessage else ""
    Assert.assertTrue(msgOut1, resOut1.isRight)
    val resOut0 = assertDFEquals(
      dfOut0.select("last_name",
                    "account_flags",
                    "account_open_date",
                    "country_code",
                    "customer_id"
      ),
      dfOut0Computed.select("last_name",
                            "account_flags",
                            "account_open_date",
                            "country_code",
                            "customer_id"
      ),
      maxUnequalRowsToShow,
      1.0
    )
    val msgOut0 = if (resOut0.isLeft) resOut0.left.get.getMessage else ""
    Assert.assertTrue(msgOut0, resOut0.isRight)
  }

  override def beforeAll() = {
    super.beforeAll()
    spark.conf.set("spark.sql.legacy.allowUntypedScalaUDF", "true")

    val fabricName = System.getProperty("fabric")

    val config = ConfigurationFactoryImpl.fromCLI(
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
