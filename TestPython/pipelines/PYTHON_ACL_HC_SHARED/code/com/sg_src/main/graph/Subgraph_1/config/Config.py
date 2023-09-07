from com.sg_src.main.graph.Subgraph_1.Subgraph_1.config.Config import SubgraphConfig as Subgraph_1_Config
from com.sg_src.main.graph.Subgraph_1.Subgraph_2.config.Config import SubgraphConfig as Subgraph_2_Config
from com.sg_src.main.graph.Subgraph_1.Subgraph_4_1_1.config.Config import SubgraphConfig as Subgraph_4_1_1_Config
from prophecy.config import ConfigBase


class C_sg1_record(ConfigBase):
    def __init__(
            self,
            prophecy_spark=None,
            c_sg1_record_c_string: str="hello sir $$ yes this is me $$$$",
            c_sg1_record_c_boolean: bool=False,
            c_sg1_record_c_float: float=12.12,
            c_sg1_record_c_int: int=12,
            **kwargs
    ):
        self.c_sg1_record_c_string = c_sg1_record_c_string
        self.c_sg1_record_c_boolean = c_sg1_record_c_boolean
        self.c_sg1_record_c_float = c_sg1_record_c_float
        self.c_sg1_record_c_int = c_sg1_record_c_int
        pass


class SubgraphConfig(ConfigBase):

    def __init__(
            self,
            prophecy_spark=None,
            c_dbsecrets: str="qasecrets_mysql:username",
            c_string: str="test",
            Subgraph_4_1_1: dict={},
            c_sg1_array_string: list=["this is first $$", "this is second $$"],
            c_sg1_record: dict={},
            c_sg1_spark_expressions: str="concat('a', 'b')",
            Subgraph_1: dict={},
            Subgraph_2: dict={},
            **kwargs
    ):

        if c_dbsecrets is not None:
            self.c_dbsecrets = self.get_dbutils(prophecy_spark).secrets.get(*c_dbsecrets.split(":"))

        self.c_string = c_string
        self.Subgraph_4_1_1 = self.get_config_object(
            prophecy_spark, 
            Subgraph_4_1_1_Config(prophecy_spark = prophecy_spark), 
            Subgraph_4_1_1, 
            Subgraph_4_1_1_Config
        )
        self.c_sg1_array_string = c_sg1_array_string
        self.c_sg1_record = self.get_config_object(
            prophecy_spark, 
            C_sg1_record(prophecy_spark = prophecy_spark), 
            c_sg1_record, 
            C_sg1_record
        )
        self.c_sg1_spark_expressions = c_sg1_spark_expressions
        self.Subgraph_1 = self.get_config_object(
            prophecy_spark, 
            Subgraph_1_Config(prophecy_spark = prophecy_spark), 
            Subgraph_1, 
            Subgraph_1_Config
        )
        self.Subgraph_2 = self.get_config_object(
            prophecy_spark, 
            Subgraph_2_Config(prophecy_spark = prophecy_spark), 
            Subgraph_2, 
            Subgraph_2_Config
        )
        pass

    def update(self, updated_config):
        self.c_dbsecrets = updated_config.c_dbsecrets
        self.c_string = updated_config.c_string
        self.Subgraph_4_1_1 = updated_config.Subgraph_4_1_1
        self.c_sg1_array_string = updated_config.c_sg1_array_string
        self.c_sg1_record = updated_config.c_sg1_record
        self.c_sg1_spark_expressions = updated_config.c_sg1_spark_expressions
        self.Subgraph_1 = updated_config.Subgraph_1
        self.Subgraph_2 = updated_config.Subgraph_2
        pass

Config = SubgraphConfig()
