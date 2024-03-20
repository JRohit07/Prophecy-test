from prophecy.config import ConfigBase


class Config(ConfigBase):

    def __init__(
            self,
            JDBC_TABLE: str=None,
            JDBC_URL: str=None,
            SQL_QUERY: str=None,
            SQL_CONFIG_QUERY: str=None,
            DRIVER_NAME: str=None,
            JDBC_USER_SECRET: str=None,
            JDBC_PASSWORD_SECRET: str=None,
            JDBC_USER_STRING: str=None,
            JDBC_PASSWORD_STRING: str=None,
            ENV_JDBC_USERNAME: str=None,
            ENV_JDBC_PASSWORD: str=None,
            ENV_JDBC_URL: str=None,
            JDBC_DEST_TABLE: str=None,
            TEST: str=None,
            USER: str=None,
            ADM: str=None,
            IN: str=None,
            JDBC: str=None,
            SCOPE: str=None,
            ROHIT: str=None,
            MYSQL: str=None,
            USERNAME: str=None,
            PASSWORD: str=None,
            JDBC_NAME: str=None,
            JDBC_DATABASE: str=None,
            **kwargs
    ):
        self.spark = None
        self.update(
            JDBC_TABLE, 
            JDBC_URL, 
            SQL_QUERY, 
            SQL_CONFIG_QUERY, 
            DRIVER_NAME, 
            JDBC_USER_SECRET, 
            JDBC_PASSWORD_SECRET, 
            JDBC_USER_STRING, 
            JDBC_PASSWORD_STRING, 
            ENV_JDBC_USERNAME, 
            ENV_JDBC_PASSWORD, 
            ENV_JDBC_URL, 
            JDBC_DEST_TABLE, 
            TEST, 
            USER, 
            ADM, 
            IN, 
            JDBC, 
            SCOPE, 
            ROHIT, 
            MYSQL, 
            USERNAME, 
            PASSWORD, 
            JDBC_NAME, 
            JDBC_DATABASE
        )

    def update(
            self,
            JDBC_TABLE: str="test_table_automation",
            JDBC_URL: str="jdbc:mysql://3.101.152.38:3306/test_database",
            SQL_QUERY: str="select * from test_table",
            SQL_CONFIG_QUERY: str="select * from ${SQL_QUERY}",
            DRIVER_NAME: str="com.mysql.jdbc.Driver",
            JDBC_USER_SECRET: str="rohit_mysql:username",
            JDBC_PASSWORD_SECRET: str="rohit_mysql:password",
            JDBC_USER_STRING: str="test_user",
            JDBC_PASSWORD_STRING: str="admin",
            ENV_JDBC_USERNAME: str="JDBC_USERNAME",
            ENV_JDBC_PASSWORD: str="JDBC_PASSWORD",
            ENV_JDBC_URL: str="JDBC_URL",
            JDBC_DEST_TABLE: str="test_table_destination",
            TEST: str="test",
            USER: str="user",
            ADM: str="adm",
            IN: str="in",
            JDBC: str="jdbc:mysql://3.101.152.38:3306",
            SCOPE: str="rohit_mysql",
            ROHIT: str="rohit",
            MYSQL: str="mysql",
            USERNAME: str="USERNAME",
            PASSWORD: str="PASSWORD",
            JDBC_NAME: str="JDBC",
            JDBC_DATABASE: str="test_database",
            **kwargs
    ):
        prophecy_spark = self.spark
        self.JDBC_TABLE = JDBC_TABLE
        self.JDBC_URL = JDBC_URL
        self.SQL_QUERY = SQL_QUERY
        self.SQL_CONFIG_QUERY = SQL_CONFIG_QUERY
        self.DRIVER_NAME = DRIVER_NAME

        if JDBC_USER_SECRET is not None:
            self.JDBC_USER_SECRET = self.get_dbutils(prophecy_spark).secrets.get(*JDBC_USER_SECRET.split(":"))

        if JDBC_PASSWORD_SECRET is not None:
            self.JDBC_PASSWORD_SECRET = self.get_dbutils(prophecy_spark).secrets.get(*JDBC_PASSWORD_SECRET.split(":"))

        self.JDBC_USER_STRING = JDBC_USER_STRING
        self.JDBC_PASSWORD_STRING = JDBC_PASSWORD_STRING
        self.ENV_JDBC_USERNAME = ENV_JDBC_USERNAME
        self.ENV_JDBC_PASSWORD = ENV_JDBC_PASSWORD
        self.ENV_JDBC_URL = ENV_JDBC_URL
        self.JDBC_DEST_TABLE = JDBC_DEST_TABLE
        self.TEST = TEST
        self.USER = USER
        self.ADM = ADM
        self.IN = IN
        self.JDBC = JDBC
        self.SCOPE = SCOPE
        self.ROHIT = ROHIT
        self.MYSQL = MYSQL
        self.USERNAME = USERNAME
        self.PASSWORD = PASSWORD
        self.JDBC_NAME = JDBC_NAME
        self.JDBC_DATABASE = JDBC_DATABASE
        pass
