from prophecy.config import ConfigBase


class Config(ConfigBase):

    def __init__(
            self,
            JDBC_USER_SECRET: str=None,
            JDBC_PASSWORD_SECRET: str=None,
            JDBC_URL: str=None,
            JDBC_TABLE_SOURCE: str=None,
            JDBC_TABLE_DESTINATION: str=None,
            **kwargs
    ):
        self.spark = None
        self.update(JDBC_USER_SECRET, JDBC_PASSWORD_SECRET, JDBC_URL, JDBC_TABLE_SOURCE, JDBC_TABLE_DESTINATION)

    def update(
            self,
            JDBC_USER_SECRET: str="rohit_mysql:username",
            JDBC_PASSWORD_SECRET: str="rohit_mysql:password",
            JDBC_URL: str="jdbc:mysql://3.101.152.38:3306/test_database",
            JDBC_TABLE_SOURCE: str="test_table_automation",
            JDBC_TABLE_DESTINATION: str="test_table_destination",
            **kwargs
    ):
        prophecy_spark = self.spark

        if JDBC_USER_SECRET is not None:
            self.JDBC_USER_SECRET = self.get_dbutils(prophecy_spark).secrets.get(*JDBC_USER_SECRET.split(":"))

        if JDBC_PASSWORD_SECRET is not None:
            self.JDBC_PASSWORD_SECRET = self.get_dbutils(prophecy_spark).secrets.get(*JDBC_PASSWORD_SECRET.split(":"))

        self.JDBC_URL = JDBC_URL
        self.JDBC_TABLE_SOURCE = JDBC_TABLE_SOURCE
        self.JDBC_TABLE_DESTINATION = JDBC_TABLE_DESTINATION
        pass
