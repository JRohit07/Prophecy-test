from python_unity_catalog.graph.Subgraph_1.config.Config import SubgraphConfig as Subgraph_1_Config
from prophecy.config import ConfigBase


class Config(ConfigBase):

    def __init__(
            self,
            c_string: str=None,
            c_long: int=None,
            c_dbsecrets: str=None,
            c_spark_expression: str=None,
            c_float: float=None,
            c_boolean: bool=None,
            Subgraph_1: dict=None,
            **kwargs
    ):
        self.spark = None
        self.update(c_string, c_long, c_dbsecrets, c_spark_expression, c_float, c_boolean, Subgraph_1)

    def update(
            self,
            c_string: str="skjdsadsa",
            c_long: int=4324234,
            c_dbsecrets: str="qasecrets_mysql:username",
            c_spark_expression: str="concat('a', first_name)",
            c_float: float=-12312.123,
            c_boolean: bool=True,
            Subgraph_1: dict={},
            **kwargs
    ):
        prophecy_spark = self.spark
        self.c_string = c_string
        self.c_long = self.get_int_value(c_long)

        if c_dbsecrets is not None:
            self.c_dbsecrets = self.get_dbutils(prophecy_spark).secrets.get(*c_dbsecrets.split(":"))

        self.c_spark_expression = c_spark_expression
        self.c_float = self.get_float_value(c_float)
        self.c_boolean = self.get_bool_value(c_boolean)
        self.Subgraph_1 = self.get_config_object(
            prophecy_spark, 
            Subgraph_1_Config(prophecy_spark = prophecy_spark), 
            Subgraph_1, 
            Subgraph_1_Config
        )
        pass
