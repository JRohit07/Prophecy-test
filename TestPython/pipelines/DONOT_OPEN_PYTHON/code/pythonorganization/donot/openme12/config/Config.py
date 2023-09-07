from pythonorganization.donot.openme12.graph.SubGraph_2.config.Config import SubgraphConfig as SubGraph_2_Config
from pythonorganization.donot.openme12.graph.all_type_main_1.config.Config import (
    SubgraphConfig as all_type_main_1_Config
)
from pythonorganization.donot.openme12.graph.SubGraph_7.config.Config import SubgraphConfig as SubGraph_7_Config
from prophecy.config import ConfigBase


class Config(ConfigBase):

    def __init__(
            self,
            JDBC_URL: str=None,
            JDBC_SOURCE_TABLE: str=None,
            CONFIG_STR: str=None,
            CONFIG_BOOLEAN: bool=None,
            CONFIG_DOUBLE: float=None,
            CONFIG_INT: int=None,
            CONFIG_FLOAT: float=None,
            CONFIG_SHORT: int=None,
            CONFIG_DB_SECRETS: str=None,
            SubGraph_2: dict=None,
            all_type_main_1: dict=None,
            SubGraph_7: dict=None,
            **kwargs
    ):
        self.spark = None
        self.update(
            JDBC_URL, 
            JDBC_SOURCE_TABLE, 
            CONFIG_STR, 
            CONFIG_BOOLEAN, 
            CONFIG_DOUBLE, 
            CONFIG_INT, 
            CONFIG_FLOAT, 
            CONFIG_SHORT, 
            CONFIG_DB_SECRETS, 
            SubGraph_2, 
            all_type_main_1, 
            SubGraph_7
        )

    def update(
            self,
            JDBC_URL: str="jdbc:mysql://18.144.156.219:3306/test_database",
            JDBC_SOURCE_TABLE: str="test_table",
            CONFIG_STR: str=None,
            CONFIG_BOOLEAN: bool=True,
            CONFIG_DOUBLE: float=1.00123211232E7,
            CONFIG_INT: int=None,
            CONFIG_FLOAT: float=4567546.5,
            CONFIG_SHORT: int=120,
            CONFIG_DB_SECRETS: str="qasecrets:mysql_user",
            SubGraph_2: dict={},
            all_type_main_1: dict={},
            SubGraph_7: dict={},
            **kwargs
    ):
        prophecy_spark = self.spark
        self.JDBC_URL = JDBC_URL
        self.JDBC_SOURCE_TABLE = JDBC_SOURCE_TABLE
        self.CONFIG_STR = CONFIG_STR
        self.CONFIG_BOOLEAN = self.get_bool_value(CONFIG_BOOLEAN)
        self.CONFIG_DOUBLE = self.get_float_value(CONFIG_DOUBLE)
        self.CONFIG_INT = self.get_int_value(CONFIG_INT)
        self.CONFIG_FLOAT = self.get_float_value(CONFIG_FLOAT)
        self.CONFIG_SHORT = self.get_int_value(CONFIG_SHORT)

        if CONFIG_DB_SECRETS is not None:
            self.CONFIG_DB_SECRETS = self.get_dbutils(prophecy_spark).secrets.get(*CONFIG_DB_SECRETS.split(":"))

        self.SubGraph_2 = self.get_config_object(
            prophecy_spark, 
            SubGraph_2_Config(prophecy_spark = prophecy_spark), 
            SubGraph_2, 
            SubGraph_2_Config
        )
        self.all_type_main_1 = self.get_config_object(
            prophecy_spark, 
            all_type_main_1_Config(prophecy_spark = prophecy_spark), 
            all_type_main_1, 
            all_type_main_1_Config
        )
        self.SubGraph_7 = self.get_config_object(
            prophecy_spark, 
            SubGraph_7_Config(prophecy_spark = prophecy_spark), 
            SubGraph_7, 
            SubGraph_7_Config
        )
        pass
