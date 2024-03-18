package io.prophecy.pipelines.pipeline_with_configs.config

import org.apache.spark.sql.SparkSession
case class Context(spark: SparkSession, config: Config)
