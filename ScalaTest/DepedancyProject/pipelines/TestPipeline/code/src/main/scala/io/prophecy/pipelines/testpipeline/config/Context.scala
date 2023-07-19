package io.prophecy.pipelines.testpipeline.config

import org.apache.spark.sql.SparkSession
case class Context(spark: SparkSession, config: Config)
