from pyspark.sql import SparkSession
from prophecy.config.utils import *
from .Config import Config as ConfigClass
Config: ConfigClass = ConfigClass()


class Utils:
    @staticmethod
    def initializeFromArgs(spark: SparkSession, args, default_conf="rel_py_pip_dep_mgmt_all.conf"):
        global Config
        Config.updateSpark(spark)
        conf = parse_config(
            args,
            default_conf,
            config_package = "prophecy_config_instances.com.main1.configall.all_the_configs"
        )
        Config.update(**conf)
