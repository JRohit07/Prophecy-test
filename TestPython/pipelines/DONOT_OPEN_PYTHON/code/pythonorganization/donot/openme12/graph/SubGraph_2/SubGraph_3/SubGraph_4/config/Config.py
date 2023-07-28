from pythonorganization.donot.openme12.graph.SubGraph_2.SubGraph_3.SubGraph_4.SubGraph_5.config.Config import (
    SubgraphConfig as SubGraph_5_Config
)
from prophecy.config import ConfigBase


class SubgraphConfig(ConfigBase):

    def __init__(
            self,
            prophecy_spark=None,
            JDBC_URL: str="jdbc:mysql://18.144.156.219:3306/test_database",
            JDBC_SOURCE_TABLE: str="test_table",
            CONFIG_STR: str=None,
            CONFIG_BOOLEAN: bool=True,
            CONFIG_DOUBLE: float=1.00123211232E7,
            CONFIG_INT: int=None,
            CONFIG_FLOAT: float=4567546.5,
            CONFIG_SHORT: int=120,
            CONFIG_DB_SECRETS: str="qasecrets:mysql_user",
            SubGraph_5: dict={},
            **kwargs
    ):
        self.JDBC_URL = JDBC_URL
        self.JDBC_SOURCE_TABLE = JDBC_SOURCE_TABLE
        self.CONFIG_STR = CONFIG_STR
        self.CONFIG_BOOLEAN = CONFIG_BOOLEAN
        self.CONFIG_DOUBLE = CONFIG_DOUBLE
        self.CONFIG_INT = CONFIG_INT
        self.CONFIG_FLOAT = CONFIG_FLOAT
        self.CONFIG_SHORT = CONFIG_SHORT

        if CONFIG_DB_SECRETS is not None:
            self.CONFIG_DB_SECRETS = self.get_dbutils(prophecy_spark).secrets.get(*CONFIG_DB_SECRETS.split(":"))

        self.SubGraph_5 = self.get_config_object(
            prophecy_spark, 
            SubGraph_5_Config(prophecy_spark = prophecy_spark), 
            SubGraph_5, 
            SubGraph_5_Config
        )
        pass

    def update(self, updated_config):
        self.JDBC_URL = updated_config.JDBC_URL
        self.JDBC_SOURCE_TABLE = updated_config.JDBC_SOURCE_TABLE
        self.CONFIG_STR = updated_config.CONFIG_STR
        self.CONFIG_BOOLEAN = updated_config.CONFIG_BOOLEAN
        self.CONFIG_DOUBLE = updated_config.CONFIG_DOUBLE
        self.CONFIG_INT = updated_config.CONFIG_INT
        self.CONFIG_FLOAT = updated_config.CONFIG_FLOAT
        self.CONFIG_SHORT = updated_config.CONFIG_SHORT
        self.CONFIG_DB_SECRETS = updated_config.CONFIG_DB_SECRETS
        self.SubGraph_5 = updated_config.SubGraph_5
        pass

Config = SubgraphConfig()
