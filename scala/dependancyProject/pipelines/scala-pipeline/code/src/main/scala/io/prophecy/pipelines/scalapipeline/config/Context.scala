package io.prophecy.pipelines.scalapipeline.config

import org.apache.spark.sql.SparkSession
case class Context(spark: SparkSession, config: Config)
