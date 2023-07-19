package com.main.sub_graph_src1

import io.prophecy.libs._
import com.main.sub_graph_src1.config.Context
import com.main.sub_graph_src1.config._
import com.main.sub_graph_src1.config.ConfigStore.interimOutput
import com.main.sub_graph_src1.udfs.UDFs._
import com.main.sub_graph_src1.udfs._
import com.main.sub_graph_src1.udfs.PipelineInitCode._
import com.main.sub_graph_src1.graph._
import com.main.sub_graph_src1.graph.all_type_sg_scala_main
import com.main.sub_graph_src1.graph.all_type_sg_scala_main.config.{
  Context => all_type_sg_scala_main_Context
}
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._

object Main {

  def graph(context: Context): Unit = {
    val df_src_parquet_all_type_and_partition_withspacehyphens =
      src_parquet_all_type_and_partition_withspacehyphens(context).interim(
        "graph",
        "8qziesy9-ngcOeLhVFmCK$$oTFH-zftsblU11s6LLMBZ",
        "tZblttEX9pep-3_lCvBEW$$zkLqZI_HCzpfACOL1uLTn"
      )
    val df_Reformat_1 =
      Reformat_1(context,
                 df_src_parquet_all_type_and_partition_withspacehyphens
      ).interim("graph",
                "sguXN3Qzk-rrsIeKc-lwj$$6nXDsqNXOLVMJZNMjkPv0",
                "97nBNPy4v0oHeGU_zRGWw$$luZlhcxAsoGVl412RoaFq"
      )
    df_Reformat_1.cache().count()
    df_Reformat_1.unpersist()
    val df_Reformat_2 =
      Reformat_2(context,
                 df_src_parquet_all_type_and_partition_withspacehyphens
      ).interim("graph",
                "zS5n3k8HQ3HkziA9bYBKF$$PDoyluybxcGiqi79lWkPX",
                "Yg9BtDqf0TxmaRYho1Lh9$$0p_ZBE_H6Fgrzgzdg6M4u"
      )
    df_Reformat_2.cache().count()
    df_Reformat_2.unpersist()
    val (df_all_type_sg_scala_main_out0,
         df_all_type_sg_scala_main_out1,
         df_all_type_sg_scala_main_out2
    ) = {
      val (df_all_type_sg_scala_main_out0_temp,
           df_all_type_sg_scala_main_out1_temp,
           df_all_type_sg_scala_main_out2_temp
      ) = all_type_sg_scala_main.apply(
        all_type_sg_scala_main_Context(context.spark,
                                       context.config.all_type_sg_scala_main
        ),
        df_src_parquet_all_type_and_partition_withspacehyphens,
        df_src_parquet_all_type_and_partition_withspacehyphens,
        df_src_parquet_all_type_and_partition_withspacehyphens
      )
      (df_all_type_sg_scala_main_out0_temp,
       df_all_type_sg_scala_main_out1_temp,
       df_all_type_sg_scala_main_out2_temp
      )
    }
    df_all_type_sg_scala_main_out0.cache().count()
    df_all_type_sg_scala_main_out0.unpersist()
    df_all_type_sg_scala_main_out1.cache().count()
    df_all_type_sg_scala_main_out1.unpersist()
    df_all_type_sg_scala_main_out2.cache().count()
    df_all_type_sg_scala_main_out2.unpersist()
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
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/SCALA_SG_SRC")
    MetricsCollector.start(spark,                    "pipelines/SCALA_SG_SRC")
    graph(context)
    MetricsCollector.end(spark)
  }

}
