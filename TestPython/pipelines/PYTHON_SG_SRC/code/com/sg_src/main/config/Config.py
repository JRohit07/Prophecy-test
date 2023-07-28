from com.sg_src.main.graph.all_type_main_pythonsg.config.Config import SubgraphConfig as all_type_main_pythonsg_Config
from prophecy.config import ConfigBase


class Config(ConfigBase):

    def __init__(self, c_dbsecrets: str=None, c_string: str=None, all_type_main_pythonsg: dict=None, **kwargs):
        self.spark = None
        self.update(c_dbsecrets, c_string, all_type_main_pythonsg)

    def update(
            self,
            c_dbsecrets: str="qasecrets_mysql:username",
            c_string: str="test",
            all_type_main_pythonsg: dict={},
            **kwargs
    ):
        prophecy_spark = self.spark

        if c_dbsecrets is not None:
            self.c_dbsecrets = self.get_dbutils(prophecy_spark).secrets.get(*c_dbsecrets.split(":"))

        self.c_string = c_string
        self.all_type_main_pythonsg = self.get_config_object(
            prophecy_spark, 
            all_type_main_pythonsg_Config(prophecy_spark = prophecy_spark), 
            all_type_main_pythonsg, 
            all_type_main_pythonsg_Config
        )
        pass
