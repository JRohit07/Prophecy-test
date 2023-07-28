from livy_python.graph.Subgraph_4.config.Config import SubgraphConfig as Subgraph_4_Config
from livy_python.graph.pythonLivySG1_1.config.Config import SubgraphConfig as pythonLivySG1_1_Config
from prophecy.config import ConfigBase


class Config(ConfigBase):

    def __init__(
            self,
            c_st_expr: str=None,
            c_expr: str=None,
            c_string: str=None,
            c_int: int=None,
            pythonLivySG1_1: dict=None,
            Subgraph_4: dict=None,
            **kwargs
    ):
        self.spark = None
        self.update(c_st_expr, c_expr, c_string, c_int, pythonLivySG1_1, Subgraph_4)

    def update(
            self,
            c_st_expr: str="concat(industry_code_ANZSIC, industry_name_ANZSIC)",
            c_expr: str="%11%",
            c_string: str="this is a test string",
            c_int: int=22,
            pythonLivySG1_1: dict={},
            Subgraph_4: dict={},
            **kwargs
    ):
        prophecy_spark = self.spark
        self.c_st_expr = c_st_expr
        self.c_expr = c_expr
        self.c_string = c_string
        self.c_int = self.get_int_value(c_int)
        self.pythonLivySG1_1 = self.get_config_object(
            prophecy_spark, 
            pythonLivySG1_1_Config(prophecy_spark = prophecy_spark), 
            pythonLivySG1_1, 
            pythonLivySG1_1_Config
        )
        self.Subgraph_4 = self.get_config_object(
            prophecy_spark, 
            Subgraph_4_Config(prophecy_spark = prophecy_spark), 
            Subgraph_4, 
            Subgraph_4_Config
        )
        pass
