package io.prophecy.pipelines.pip1.config

import org.apache.spark.sql.SparkSession
case class Context(spark: SparkSession, config: Config)
