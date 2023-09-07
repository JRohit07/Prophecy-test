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
            **kwargs
    ):
        self.c_string = c_string
        self.c_long = c_long

        if c_dbsecrets is not None:
            self.c_dbsecrets = self.get_dbutils(prophecy_spark).secrets.get(*c_dbsecrets.split(":"))

        self.c_spark_expression = c_spark_expression
        self.c_float = c_float
        self.c_boolean = c_boolean
        pass

    def update(self, updated_config):
        self.c_string = updated_config.c_string
        self.c_long = updated_config.c_long
        self.c_dbsecrets = updated_config.c_dbsecrets
        self.c_spark_expression = updated_config.c_spark_expression
        self.c_float = updated_config.c_float
        self.c_boolean = updated_config.c_boolean
        pass

Config = SubgraphConfig()
