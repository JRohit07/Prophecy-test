package io.prophecy.pipelines.perf_unitest_generate.config

import org.apache.spark.sql.SparkSession
case class Context(spark: SparkSession, config: Config)
