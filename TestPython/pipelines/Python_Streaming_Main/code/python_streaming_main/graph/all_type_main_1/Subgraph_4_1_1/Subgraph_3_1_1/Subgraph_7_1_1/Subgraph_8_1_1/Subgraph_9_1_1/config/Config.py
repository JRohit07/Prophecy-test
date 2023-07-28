from prophecy.config import ConfigBase


class SubgraphConfig(ConfigBase):

    def __init__(
            self,
            prophecy_spark=None,
            c_dbsecrets: str="qasecrets_mysql:username",
            c_string: str="test",
            c_boolean_sg9_1_1: bool=False,
            **kwargs
    ):

        if c_dbsecrets is not None:
            self.c_dbsecrets = self.get_dbutils(prophecy_spark).secrets.get(*c_dbsecrets.split(":"))

        self.c_string = c_string
        self.c_boolean_sg9_1_1 = c_boolean_sg9_1_1
        pass

    def update(self, updated_config):
        self.c_dbsecrets = updated_config.c_dbsecrets
        self.c_string = updated_config.c_string
        self.c_boolean_sg9_1_1 = updated_config.c_boolean_sg9_1_1
        pass

Config = SubgraphConfig()
