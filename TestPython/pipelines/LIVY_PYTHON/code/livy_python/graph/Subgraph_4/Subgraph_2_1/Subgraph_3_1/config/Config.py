from prophecy.config import ConfigBase


class SubgraphConfig(ConfigBase):

    def __init__(
            self,
            prophecy_spark=None,
            c_st_expr: str="concat(industry_code_ANZSIC, industry_name_ANZSIC)",
            c_expr: str="%11%",
            c_string: str="this is a test string",
            c_int: int=22,
            **kwargs
    ):
        self.c_st_expr = c_st_expr
        self.c_expr = c_expr
        self.c_string = c_string
        self.c_int = c_int
        pass

    def update(self, updated_config):
        self.c_st_expr = updated_config.c_st_expr
        self.c_expr = updated_config.c_expr
        self.c_string = updated_config.c_string
        self.c_int = updated_config.c_int
        pass

Config = SubgraphConfig()
