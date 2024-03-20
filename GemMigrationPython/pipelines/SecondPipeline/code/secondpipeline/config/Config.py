from prophecy.config import ConfigBase


class Config(ConfigBase):

    def __init__(
            self,
            JDBC_URL: str=None,
            JDBC_TABLE: str=None,
            JDBC: str=None,
            JDBC_DATABASE: str=None,
            DRIVER_NAME: str=None,
            JDBC_USER_SECRET: str=None,
            JDBC_PASSWORD_SECRET: str=None,
            JDBC_USER_STRING: str=None,
            JDBC_PASSWORD_STRING: str=None,
            ENV_JDBC_USERNAME: str=None,
            ENV_JDBC_PASSWORD: str=None,
            TEST: str=None,
            ADM: str=None,
            IN: str=None,
            JDBC_DEST_TABLE: str=None,
            USER: str=None,
            **kwargs
    ):
        self.spark = None
        self.update(
            JDBC_URL, 
            JDBC_TABLE, 
            JDBC, 
            JDBC_DATABASE, 
            DRIVER_NAME, 
            JDBC_USER_SECRET, 
            JDBC_PASSWORD_SECRET, 
            JDBC_USER_STRING, 
            JDBC_PASSWORD_STRING, 
            ENV_JDBC_USERNAME, 
            ENV_JDBC_PASSWORD, 
            TEST, 
            ADM, 
            IN, 
            JDBC_DEST_TABLE, 
            USER
        )

    def update(
            self,
            JDBC_URL: str="jdbc:mysql://3.101.152.38:3306/test_database",
            JDBC_TABLE: str="test_table_automation",
            JDBC: str="jdbc:mysql://3.101.152.38:3306/",
            JDBC_DATABASE: str="test_database",
            DRIVER_NAME: str="com.mysql.jdbc.Driver",
            JDBC_USER_SECRET: str="rohit_mysql:username",
            JDBC_PASSWORD_SECRET: str="rohit_mysql:password",
            JDBC_USER_STRING: str="test_user",
            JDBC_PASSWORD_STRING: str="admin",
            ENV_JDBC_USERNAME: str="JDBC_USERNAME",
            ENV_JDBC_PASSWORD: str="JDBC_PASSWORD",
            TEST: str="test",
            ADM: str="adm",
            IN: str="in",
            JDBC_DEST_TABLE: str="test_table_destination",
            USER: str="user",
            **kwargs
    ):
        prophecy_spark = self.spark
        self.JDBC_URL = JDBC_URL
        self.JDBC_TABLE = JDBC_TABLE
        self.JDBC = JDBC
        self.JDBC_DATABASE = JDBC_DATABASE
        self.DRIVER_NAME = DRIVER_NAME

        if JDBC_USER_SECRET is not None:
            self.JDBC_USER_SECRET = self.get_dbutils(prophecy_spark).secrets.get(*JDBC_USER_SECRET.split(":"))

        if JDBC_PASSWORD_SECRET is not None:
            self.JDBC_PASSWORD_SECRET = self.get_dbutils(prophecy_spark).secrets.get(*JDBC_PASSWORD_SECRET.split(":"))

        self.JDBC_USER_STRING = JDBC_USER_STRING
        self.JDBC_PASSWORD_STRING = JDBC_PASSWORD_STRING
        self.ENV_JDBC_USERNAME = ENV_JDBC_USERNAME
        self.ENV_JDBC_PASSWORD = ENV_JDBC_PASSWORD
        self.TEST = TEST
        self.ADM = ADM
        self.IN = IN
        self.JDBC_DEST_TABLE = JDBC_DEST_TABLE
        self.USER = USER
        pass
