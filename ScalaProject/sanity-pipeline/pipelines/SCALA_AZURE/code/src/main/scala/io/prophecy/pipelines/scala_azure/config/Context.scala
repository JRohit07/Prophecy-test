package io.prophecy.pipelines.scala_azure.config

import org.apache.spark.sql.SparkSession
case class Context(spark: SparkSession, config: Config)
