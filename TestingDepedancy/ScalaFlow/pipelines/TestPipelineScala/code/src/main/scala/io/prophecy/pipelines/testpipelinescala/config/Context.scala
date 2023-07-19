package io.prophecy.pipelines.testpipelinescala.config

import org.apache.spark.sql.SparkSession
case class Context(spark: SparkSession, config: Config)
