from python_unity_catalog.graph.Subgraph_1.Subgraph_2.config.Config import SubgraphConfig as Subgraph_2_Config
from prophecy.config import ConfigBase


class SubgraphConfig(ConfigBase):

    def __init__(
            self,
            prophecy_spark=None,
            c_string: str="skjdsadsa",
            c_long: int=4324234,
            c_dbsecrets: str="qasecrets_mysql:username",
            c_spark_expression: str="concat('a', first_name)",
            c_float: float=-12312.123,
            c_boolean: bool=True,
            Subgraph_2: dict={},
            **kwargs
    ):
        self.c_string = c_string
        self.c_long = c_long

        if c_dbsecrets is not None:
            self.c_dbsecrets = self.get_dbutils(prophecy_spark).secrets.get(*c_dbsecrets.split(":"))

        self.c_spark_expression = c_spark_expression
        self.c_float = c_float
        self.c_boolean = c_boolean
        self.Subgraph_2 = self.get_config_object(
            prophecy_spark, 
            Subgraph_2_Config(prophecy_spark = prophecy_spark), 
            Subgraph_2, 
            Subgraph_2_Config
        )
        pass

    def update(self, updated_config):
        self.c_string = updated_config.c_string
        self.c_long = updated_config.c_long
        self.c_dbsecrets = updated_config.c_dbsecrets
        self.c_spark_expression = updated_config.c_spark_expression
        self.c_float = updated_config.c_float
        self.c_boolean = updated_config.c_boolean
        self.Subgraph_2 = updated_config.Subgraph_2
        pass

Config = SubgraphConfig()
