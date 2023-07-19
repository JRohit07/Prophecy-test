package io.prophecy.pipelines.scinterimsdatabrickspipeline.config

import org.apache.spark.sql.SparkSession
case class Context(spark: SparkSession, config: Config)
