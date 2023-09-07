package io.prophecy.pipelines.scinterimsdatabrickspipeline.config

import pureconfig._
import pureconfig.generic.ProductHint
import io.prophecy.libs._

case class Config(CONFIG_INT: Int = 100, CONFIG_STR: String = "test string")
    extends ConfigBase
