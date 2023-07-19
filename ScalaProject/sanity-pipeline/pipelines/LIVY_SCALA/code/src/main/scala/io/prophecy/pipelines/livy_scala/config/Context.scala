package io.prophecy.pipelines.livy_scala.config

import org.apache.spark.sql.SparkSession
case class Context(spark: SparkSession, config: Config)
