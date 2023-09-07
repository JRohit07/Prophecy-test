from prophecy.config import ConfigBase


class Config(ConfigBase):

    def __init__(
            self,
            c_boolean: bool=None,
            c_double: float=None,
            c_float: float=None,
            c_int: int=None,
            c_long: int=None,
            c_short: int=None,
            c_db_secret: str=None,
            c_string1: str=None,
            c_expr_schematransform: str=None,
            c_colname_schematransform: str=None,
            c_colnamedrop_schematransform: str=None,
            c_regex_filter: str=None,
            c_regex_filter2: str=None,
            c_string: str=None,
            c_repartition_expr: str=None,
            c_repartition_colname: str=None,
            c_sql_expr: str=None,
            c_sql_pattern: str=None,
            c_agg_expr: str=None,
            c_date_for_today: str=None,
            c_float_name: str=None,
            c_row_number: str=None,
            c_int_name: str=None,
            c_join_condition: str=None,
            c_85: int=None,
            c_rd_expr: str=None,
            c_1: int=None,
            c_0: int=None,
            **kwargs
    ):
        self.spark = None
        self.update(
            c_boolean, 
            c_double, 
            c_float, 
            c_int, 
            c_long, 
            c_short, 
            c_db_secret, 
            c_string1, 
            c_expr_schematransform, 
            c_colname_schematransform, 
            c_colnamedrop_schematransform, 
            c_regex_filter, 
            c_regex_filter2, 
            c_string, 
            c_repartition_expr, 
            c_repartition_colname, 
            c_sql_expr, 
            c_sql_pattern, 
            c_agg_expr, 
            c_date_for_today, 
            c_float_name, 
            c_row_number, 
            c_int_name, 
            c_join_condition, 
            c_85, 
            c_rd_expr, 
            c_1, 
            c_0
        )

    def update(
            self,
            c_boolean: bool=True,
            c_double: float=10101.111,
            c_float: float=123.123,
            c_int: int=22,
            c_long: int=123233354523,
            c_short: int=12,
            c_db_secret: str="qasecrets_mysql:username",
            c_string1: str="hey@#%^&*()-=+/*-+\\'\"/.,@~",
            c_expr_schematransform: str="concat(`c  - int`, `c- short`)",
            c_colname_schematransform: str="`c-date-for-today`",
            c_colnamedrop_schematransform: str="c_double",
            c_regex_filter: str="^[_A-Za-z0-9-]+(\\\\.[_A-Za-z0-9-]+)*@[A-Za-z0-9]+(\\\\.[A-Za-z0-9]+)*(\\\\.[A-Za-z]{2,})",
            c_regex_filter2: str="((?=.*\\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#%]).{6,20})",
            c_string: str="hey@#%^&*()-=+/*-+\\'\"/.,@~",
            c_repartition_expr: str="concat(`c  float`, `c--boolean`)",
            c_repartition_colname: str="`c  float`",
            c_sql_expr: str="in0.`c  - int` > 0 and in0.`c- short` > 1",
            c_sql_pattern: str="%[a-z]*%",
            c_agg_expr: str="first(`c  - int`)",
            c_date_for_today: str="`c_date-for today`",
            c_float_name: str="`c_float-__  `",
            c_row_number: str="row_number()",
            c_int_name: str="`c  - int`",
            c_join_condition: str="in0.`c  date`=in1.`c  date`",
            c_85: int=85,
            c_rd_expr: str="`c  float` < 5 and `c-int-column type` <= 85",
            c_1: int=1,
            c_0: int=0,
            **kwargs
    ):
        prophecy_spark = self.spark
        self.c_boolean = self.get_bool_value(c_boolean)
        self.c_double = self.get_float_value(c_double)
        self.c_float = self.get_float_value(c_float)
        self.c_int = self.get_int_value(c_int)
        self.c_long = self.get_int_value(c_long)
        self.c_short = self.get_int_value(c_short)

        if c_db_secret is not None:
            self.c_db_secret = self.get_dbutils(prophecy_spark).secrets.get(*c_db_secret.split(":"))

        self.c_string1 = c_string1
        self.c_expr_schematransform = c_expr_schematransform
        self.c_colname_schematransform = c_colname_schematransform
        self.c_colnamedrop_schematransform = c_colnamedrop_schematransform
        self.c_regex_filter = c_regex_filter
        self.c_regex_filter2 = c_regex_filter2
        self.c_string = c_string
        self.c_repartition_expr = c_repartition_expr
        self.c_repartition_colname = c_repartition_colname
        self.c_sql_expr = c_sql_expr
        self.c_sql_pattern = c_sql_pattern
        self.c_agg_expr = c_agg_expr
        self.c_date_for_today = c_date_for_today
        self.c_float_name = c_float_name
        self.c_row_number = c_row_number
        self.c_int_name = c_int_name
        self.c_join_condition = c_join_condition
        self.c_85 = self.get_int_value(c_85)
        self.c_rd_expr = c_rd_expr
        self.c_1 = self.get_int_value(c_1)
        self.c_0 = self.get_int_value(c_0)
        pass
