package io.prophecy.pipelines.pipeline_first.config

import org.apache.spark.sql.SparkSession
case class Context(spark: SparkSession, config: Config)
