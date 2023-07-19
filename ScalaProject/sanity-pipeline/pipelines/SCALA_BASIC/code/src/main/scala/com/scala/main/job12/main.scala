package com.scala.main.job12

import io.prophecy.libs._
import com.scala.main.job12.config.Context
import com.scala.main.job12.config._
import com.scala.main.job12.config.ConfigStore.interimOutput
import com.scala.main.job12.udfs.UDFs._
import com.scala.main.job12.udfs._
import com.scala.main.job12.udfs.PipelineInitCode._
import com.scala.main.job12.graph._
import com.scala.main.job12.graph.SubgraphMain
import com.scala.main.job12.graph.Subgraph_1
import com.scala.main.job12.graph.Subgraph_3
import com.scala.main.job12.graph.Subgraph_4
import com.scala.main.job12.graph.SubgraphMain.config.{
  Context => SubgraphMain_Context
}
import com.scala.main.job12.graph.Subgraph_1.config.{
  Context => Subgraph_1_Context
}
import com.scala.main.job12.graph.Subgraph_3.config.{
  Context => Subgraph_3_Context
}
import com.scala.main.job12.graph.Subgraph_4.config.{
  Context => Subgraph_4_Context
}
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._

object Main {

  def graph(context: Context): Unit = {
    if (!(context.config.c_int < -100)) {
      val df_src_parquet_all_type_and_partition_withspacehyphens1_1 =
        src_parquet_all_type_and_partition_withspacehyphens1_1(context).interim(
          "graph",
          "2CsHylb0Si7Iu1BwtU25H$$3c8Yrcik6DteZZzAs7Ogp",
          "40EaQ49eizOI6Q0sgDpV2$$tNarnJReknpOLuhqQoArm"
        )
      Lookup_1(context,
               df_src_parquet_all_type_and_partition_withspacehyphens1_1
      )
    }
    val df_src_parquet_all_type_and_partition_withspacehyphens1 =
      src_parquet_all_type_and_partition_withspacehyphens1(context).interim(
        "graph",
        "o8K-lNobc6Z8Asi3dRegs$$Buw8lxPhFtSUcFZhGxXbx",
        "Yui765QKx0wOKHaOnjtzk$$Q04y-nxgyv0ZfORhocEUn"
      )
    val df_SchemaTransform_1 =
      SchemaTransform_1(context,
                        df_src_parquet_all_type_and_partition_withspacehyphens1
      ).interim("graph",
                "5IEpMUJQMpUIx6Hv3eZVS$$9f4baBrU_1q1LbFl9fY2n",
                "vx64sYjC4vVrmBOSkCOXa$$qpmxU6WcJBG1bBJ5VrLY-"
      )
    val df_SubgraphMain = SubgraphMain.apply(
      SubgraphMain_Context(context.spark, context.config.SubgraphMain),
      df_src_parquet_all_type_and_partition_withspacehyphens1
    )
    val df_Reformat_1 = Reformat_1(context, df_SubgraphMain).interim(
      "graph",
      "9SxukrkbLjB9767nnjjyc$$HKrQPtYnAcfBjk1YLp12B",
      "q2OHFdKSlaApfiB-p2kod$$gjcVI8oVJu6r8jvarb7gm"
    )
    val df_Reformat_11 = Reformat_11(context, df_Reformat_1).interim(
      "graph",
      "Xd3Wt7qKtiH4SPH5A-eGR$$oZwwQphp8b9ewzTGxxg9_",
      "BrNFqH0kpdDq56WRlmzeU$$4SWO5koqKXjR7QpYwUKZ5"
    )
    df_Reformat_11.cache().count()
    df_Reformat_11.unpersist()
    val df_Script_1 =
      if (!(context.config.c_int < -100))
        if (!(context.config.c_int < -100))
          Script_1(context,
                   df_src_parquet_all_type_and_partition_withspacehyphens1
          ).interim("graph",
                     "yyqmKt6lIbvCdCmjxPmht$$g2IqhVcYuJWg9juCxyjBj",
                     "KOUvK4u2zMac-9BLVt8Is$$CspK8C6VwzsmBNgylSibS"
            )
            .cache()
        else df_src_parquet_all_type_and_partition_withspacehyphens1
      else null
    val df_Reformat_4 =
      if (!(context.config.c_int < -100 || context.config.c_int < -100)) {
        val df_Join_1 = Join_1(context, df_Script_1, df_SchemaTransform_1)
          .interim("graph",
                   "zUezgrxzF588txPNf9wMI$$JVWCUQIsrKou8fBiESaqS",
                   "hF6jZ7HJrWnao2RvRyYbB$$xQSJSKZgOIG6LRBb7CP6M"
          )
          .cache()
        Reformat_4(context, df_Join_1).interim(
          "graph",
          "Jsldsl3d5xD4SRjpdKI-Z$$DuCm45gqMbljkiKqBMQjw",
          "sPVo9omm0xwOufqyXCGI8$$F12AVA_FrP1_w296nytQb"
        )
      } else
        null
    val df_DONOT_DELETE =
      DONOT_DELETE(context,
                   df_src_parquet_all_type_and_partition_withspacehyphens1
      ).interim("graph",
                "QVkuAsxoq5NQ0MUxMEpMp$$-059MNIlT6AakSkqptOSR",
                "GDf7WQpZhqZc_HPKUwIc1$$t_F8ZP7gTEFITFhhzi1N1"
      )
    df_DONOT_DELETE.cache().count()
    df_DONOT_DELETE.unpersist()
    val df_Subgraph_1 = Subgraph_1.apply(
      Subgraph_1_Context(context.spark, context.config.Subgraph_1),
      df_src_parquet_all_type_and_partition_withspacehyphens1
    )
    val df_Subgraph_3 = Subgraph_3.apply(
      Subgraph_3_Context(context.spark, context.config.Subgraph_3),
      df_Subgraph_1
    )
    val df_Reformat_7 = Reformat_7(context, df_Subgraph_3).interim(
      "graph",
      "wuThqUc2qpf_FmJCMTj2e$$vhP6lu8CS3r_W42eJUyZ1",
      "H6Z_aAnftBpk4a-USAecW$$DfJIjJOqY8XnYd8OGH-ZP"
    )
    val df_Subgraph_4 = Subgraph_4.apply(
      Subgraph_4_Context(context.spark, context.config.Subgraph_4),
      df_Reformat_7
    )
    val df_Reformat_10 = Reformat_10(context, df_Subgraph_4).interim(
      "graph",
      "cxC3W007DVzCvlwaUSQWg$$ckcxE7qTOTY5b8BHciWQ2",
      "VJzZuiwZgT0rxBlvzkHAY$$80GGHEDnLkXPhO1zGDxko"
    )
    df_Reformat_10.cache().count()
    df_Reformat_10.unpersist()
    if (
      !(context.config.c_int < -100 || context.config.c_int < -100 || context.config.c_int < -100)
    ) {
      withSubgraphName("graph", context.spark) {
        withTargetId("dest_test", context.spark) {
          dest_test(context, df_Reformat_4)
        }
      }
    }
  }

  def main(args: Array[String]): Unit = {
    val config = ConfigurationFactoryImpl.getConfig(args)
    val spark: SparkSession = SparkSession
      .builder()
      .appName("Prophecy Pipeline")
      .config("spark.default.parallelism",             "4")
      .config("spark.sql.legacy.allowUntypedScalaUDF", "true")
      .enableHiveSupport()
      .getOrCreate()
      .newSession()
    val context = Context(spark, config)
    MetricsCollector.initializeMetrics(spark)
    implicit val interimOutputConsole: InterimOutput = InterimOutputHive2("")
    spark.conf.set("prophecy.collect.basic.stats",          "true")
    spark.conf.set("spark.sql.legacy.allowUntypedScalaUDF", "true")
    spark.conf.set("spark.sql.optimizer.excludedRules",
                   "org.apache.spark.sql.catalyst.optimizer.ColumnPruning"
    )
    spark.conf.set("spark_config1",                  "spark_config_value_1")
    spark.conf.set("spark_config2",                  "spark_config_value_2")
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/SCALA_BASIC")
    spark.sparkContext.hadoopConfiguration
      .set("hadoop_config1", "hadoop_config_value1")
    spark.sparkContext.hadoopConfiguration
      .set("hadoop_config2",      "hadoop_config_value2")
    MetricsCollector.start(spark, "pipelines/SCALA_BASIC")
    graph(context)
    MetricsCollector.end(spark)
  }

}
