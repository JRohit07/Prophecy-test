package org.main.scla_dep_mgmt_change

import io.prophecy.libs._
import org.main.scla_dep_mgmt_change.config.Context
import org.main.scla_dep_mgmt_change.config._
import org.main.scla_dep_mgmt_change.config.ConfigStore.interimOutput
import org.main.scla_dep_mgmt_change.udfs.UDFs._
import org.main.scla_dep_mgmt_change.udfs._
import org.main.scla_dep_mgmt_change.graph._
import org.main.scla_dep_mgmt_change.graph.PERF_SG
import org.main.scla_dep_mgmt_change.graph.PERF_SG.config.{
  Context => PERF_SG_Context
}
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._

object Main {

  def graph(context: Context): Unit = {
    val df_PERF_SRC_2k_COLS = PERF_SRC_2k_COLS(context).interim(
      "graph",
      "ZREi4hOnDRKidTEIiea0k$$DkN8D1VmJxVTBpOOQzjh8",
      "BpAYoGgpEAF2VHUc7l8Ut$$6OX_IvaXh1ps3_JDp5k4U"
    )
    val df_PERF_REFORMAT_CHANGE =
      PERF_REFORMAT_CHANGE(context, df_PERF_SRC_2k_COLS).interim(
        "graph",
        "nh7TjB76YLJCZTL1v8Rll$$QtdsecUCn10t_QPdNhzye",
        "mpAHYFRLlylNJ-nwT2u0V$$mS_kBm3DApkf2wRsjEeIm"
      )
    val df_PERF_LIMIT = PERF_LIMIT(context, df_PERF_REFORMAT_CHANGE).interim(
      "graph",
      "lYtU3vqhxBXX7H8Me7vxg$$BB5ZrAXcocBsmYsDpNiQI",
      "myDSKDk1hpd_1bM9wpnUk$$2k9JndWpQPNHQL49Oyd9G"
    )
    val (df_PERF_ROWDISTRIBUTOR_out0, df_PERF_ROWDISTRIBUTOR_out1) = {
      val (df_PERF_ROWDISTRIBUTOR_out0_temp, df_PERF_ROWDISTRIBUTOR_out1_temp) =
        PERF_ROWDISTRIBUTOR(context, df_PERF_LIMIT)
      (df_PERF_ROWDISTRIBUTOR_out0_temp.interim(
         "graph",
         "uwA9Eo3k1ww6lmHME1nS-$$yYsEPwMrvQVLZGgQuxkeD",
         "6UffG3IRrSdrAX-XK4TFX$$eOJVtVgZiMw3BMjGBKAA0"
       ),
       df_PERF_ROWDISTRIBUTOR_out1_temp.interim(
         "graph",
         "uwA9Eo3k1ww6lmHME1nS-$$yYsEPwMrvQVLZGgQuxkeD",
         "LwGG4eHQTwWQ8EX6OfbLx$$wbKuXZJeToAT5NhZLvgYD"
       )
      )
    }
    val df_PERF_SCRIPT =
      PERF_SCRIPT(context, df_PERF_ROWDISTRIBUTOR_out1).interim(
        "graph",
        "v1TgYKcxiaUW8Hd7hnYE0$$FDOYE2hmrutxNhr1CSxCd",
        "2cS61FN92ICBNLNrvlE_m$$10CKKOH_hdXenGUUM0TNP"
      )
    df_PERF_SCRIPT.cache().count()
    df_PERF_SCRIPT.unpersist()
    val (df_PERF_SG_out0, df_PERF_SG_out1, df_PERF_SG_out2) = {
      val (df_PERF_SG_out0_temp, df_PERF_SG_out1_temp, df_PERF_SG_out2_temp) =
        PERF_SG.apply(PERF_SG_Context(context.spark, context.config.PERF_SG),
                      df_PERF_SRC_2k_COLS,
                      df_PERF_SRC_2k_COLS,
                      df_PERF_SRC_2k_COLS
        )
      (df_PERF_SG_out0_temp, df_PERF_SG_out1_temp, df_PERF_SG_out2_temp)
    }
    val df_PERF_REPARTITION =
      PERF_REPARTITION(context, df_PERF_SG_out0).interim(
        "graph",
        "VGzd4yMZRGRiE9IDjFRlC$$ZDA0R4SR-uRsXyNCIsASK",
        "43QzNs8hPs3TeNXwts7PH$$ev_DDPyODy9u-AUU2x7B6"
      )
    df_PERF_REPARTITION.cache().count()
    df_PERF_REPARTITION.unpersist()
    val df_PERF_REFORMAT =
      PERF_REFORMAT(context, df_PERF_REFORMAT_CHANGE).interim(
        "graph",
        "5eTmnxOlzpTk-SXpQdjbO$$eQvPtE97FaixURKfuJjtX",
        "q4mUv6IZg4lYOimQIeYjl$$M7eNgxCZAjCTJGtAt9_HJ"
      )
    val df_PERF_FILTER = PERF_FILTER(context, df_PERF_REFORMAT).interim(
      "graph",
      "KvfOA7SWKk4-qy6n6iEHZ$$zDwWz7gfDbZl547fyeTeZ",
      "l3C_AJtiKrJdzuSdJyzz3$$6ZshhmwxoyLGt2zeuaby1"
    )
    val df_PERF_JOIN = PERF_JOIN(context, df_PERF_LIMIT, df_PERF_LIMIT).interim(
      "graph",
      "OVXlgFN4YIrucj9hscJtS$$fS2ipqYMUGov4U6NApi6R",
      "p7CW0kgmTid9MySe0fp4I$$hOIIwYx3uLwucnBI0Lhc0"
    )
    df_PERF_JOIN.cache().count()
    df_PERF_JOIN.unpersist()
    val df_PERF_ORDERBY = PERF_ORDERBY(context, df_PERF_FILTER).interim(
      "graph",
      "7LbDGrXKcPP1eLRD59KQ3$$3kIaJ5gntSecfXKno8DW7",
      "kyN4GUr8sF-6k7as3_LHg$$DdFAAjuj_49RL9cbHcot5"
    )
    val df_PERF_FLATTEN = PERF_FLATTEN(context, df_PERF_SRC_2k_COLS).interim(
      "graph",
      "CRWpM7UNcmrjo8Vs0Mg-x$$4Zqn_evL_lvW3rCzOZuv8",
      "7qyrb2bTOCKRK4HUvwa27$$CB8T1N2h0hucB2lNrVw7r"
    )
    df_PERF_FLATTEN.cache().count()
    df_PERF_FLATTEN.unpersist()
    val df_PERF_DEDUPLICATE =
      PERF_DEDUPLICATE(context, df_PERF_SG_out2).interim(
        "graph",
        "VOKGa7oyrIMs-QAoCYs4f$$N_TEQ3II_VAzM4A4CHjrC",
        "pxE8J8xS-lIEn-CeGjRCy$$-ONyC7fWNN-hDmQRViMdo"
      )
    df_PERF_DEDUPLICATE.cache().count()
    df_PERF_DEDUPLICATE.unpersist()
    val df_PERF_WINDOW = PERF_WINDOW(context, df_PERF_SG_out1).interim(
      "graph",
      "WMpejBXBQR2vRhSwbDdlk$$IPdLwS17Px2Rh5DpOSrVa",
      "47q3DWDo96gtGUd_SXUVT$$dzcRBiWmIFVdMosCjajeT"
    )
    df_PERF_WINDOW.cache().count()
    df_PERF_WINDOW.unpersist()
    val df_PERF_AGGREGATE = PERF_AGGREGATE(context, df_PERF_SG_out0).interim(
      "graph",
      "oO_9DIJ0Nc3lZ_P_-Sogh$$Xp51oKKk8JHpHrCrQ5Gm5",
      "j9gS7j6xdChNcjjQ7Th9y$$74j_rCSfLPiQyPRn_ZtoM"
    )
    df_PERF_AGGREGATE.cache().count()
    df_PERF_AGGREGATE.unpersist()
    val df_PERF_SQLSTATEMENT =
      PERF_SQLSTATEMENT(context, df_PERF_ROWDISTRIBUTOR_out0).interim(
        "graph",
        "cY3zoCy7QsbMXXKEkmgjg$$HGG5vEVujFxAhL-phMebE",
        "7mpXnHhhbc7aVNNGZq5TK$$laKIIWD9f_DwmBLBmAMDD"
      )
    df_PERF_SQLSTATEMENT.cache().count()
    df_PERF_SQLSTATEMENT.unpersist()
    val df_PERF_SET =
      PERF_SET(context, df_PERF_ORDERBY, df_PERF_ORDERBY).interim(
        "graph",
        "9Xn8WUJBZMB-i6z6QDdrs$$LWtsTKwZGmUmOSYroh8yv",
        "krmDuadJbpMUR6AIulMnQ$$_m3VVpAKyuD7hxW-N-tMj"
      )
    val df_PERF_SCHEMATRANSFORM =
      PERF_SCHEMATRANSFORM(context, df_PERF_SET).interim(
        "graph",
        "q_S2BgZj5OBdVRBAPciAt$$TqtfUT68t7Gx6QAItBTh-",
        "IQ3fzVerYA9Dmd4-WlJ4G$$YRuIX8VPaetOwVasvqmFA"
      )
    df_PERF_SCHEMATRANSFORM.cache().count()
    df_PERF_SCHEMATRANSFORM.unpersist()
  }

  def main(args: Array[String]): Unit = {
    val config = ConfigurationFactoryImpl.fromCLI(args)
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
    spark.conf.set("spark_config1",                  "spark_config1_value")
    spark.conf.set("spark_config2",                  "spark_config2_value")
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/PERF_SC_PIP")
    spark.sparkContext.hadoopConfiguration
      .set("hadoop_config1", "hadoop_config1_value")
    spark.sparkContext.hadoopConfiguration
      .set("hadoop_config2",      "hadoop_config2_value")
    MetricsCollector.start(spark, "pipelines/PERF_SC_PIP")
    graph(context)
    MetricsCollector.end(spark)
  }

}
