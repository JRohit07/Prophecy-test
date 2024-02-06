package io.prophecy.pipelines.firstpipeline.config

import org.apache.spark.sql.SparkSession
case class Context(spark: SparkSession, config: Config)
