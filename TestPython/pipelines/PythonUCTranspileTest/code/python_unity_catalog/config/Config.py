from prophecy.config import ConfigBase
prophecy_spark_context = None


class C_record(ConfigBase):
    def __init__(self, cr_int: int=12, cr_float: float=123.123):
        self.cr_int = cr_int
        self.cr_float = cr_float
        pass


class C_array(ConfigBase):
    def __init__(self, car_string: str=None, car_boolean: bool=None):
        self.car_string = car_string
        self.car_boolean = car_boolean
        pass


class Config(ConfigBase):

    def __init__(
            self,
            c_string: str=None, 
            c_long: int=None, 
            c_dbsecrets: str=None, 
            c_spark_expression: str=None, 
            c_float: float=None, 
            c_boolean: bool=None, 
            EXPR_COMPLEX_DATES: str=None, 
            c_int_11: int=None, 
            c_record: dict=None, 
            c_array: list=None
    ):
        self.spark = None
        self.update(
            c_string, 
            c_long, 
            c_dbsecrets, 
            c_spark_expression, 
            c_float, 
            c_boolean, 
            EXPR_COMPLEX_DATES, 
            c_int_11, 
            c_record, 
            c_array
        )

    def update(
            self,
            c_string: str="skjdsadsa", 
            c_long: int=4324234, 
            c_dbsecrets: str="qasecrets_mysql:username", 
            c_spark_expression: str="concat('a', c_int)", 
            c_float: float=-12312.123, 
            c_boolean: bool=True, 
            EXPR_COMPLEX_DATES: str="(((((date_add(date_trunc(date_format(date_sub(date_add(current_date(), 2), 2), 'yyyy MMM dd'), 'YEAR'), 1) < date_sub(current_timestamp(), 2)) OR (date_add(from_unixtime(0, 'yyyy-MM-dd HH:mm:ss'), 2) < date_add(from_utc_timestamp(c_timestamp, 'Asia/Seoul'), 2))) OR (next_day('2015-01-14', 'TU') < current_date())) OR  ((to_date('2009-07-30 04:17:52') < to_timestamp(c_date)) OR (add_months(c_timestamp, 1) < add_months(c_date, 2)))) AND ((c_int % 2) = 0)) ", 
            c_int_11: int=11, 
            c_record: dict={}, 
            c_array: list=None
    ):
        global prophecy_spark_context
        prophecy_spark_context = self.spark
        self.c_string = c_string
        self.c_long = self.get_int_value(c_long)

        if c_dbsecrets is not None:
            self.c_dbsecrets = self.get_dbutils(prophecy_spark_context).secrets.get(*c_dbsecrets.split(":"))

        self.c_spark_expression = c_spark_expression
        self.c_float = self.get_float_value(c_float)
        self.c_boolean = self.get_bool_value(c_boolean)
        self.EXPR_COMPLEX_DATES = EXPR_COMPLEX_DATES
        self.c_int_11 = self.get_int_value(c_int_11)
        self.c_record = self.get_object(C_record(), c_record, C_record)
        self.c_array = self.get_object(
            [C_array(car_string = "12321", car_boolean = True), C_array(car_string = "324234", car_boolean = False)], 
            c_array, 
            C_array
        )
        pass
