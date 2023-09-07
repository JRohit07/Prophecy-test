from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from argparse import Namespace
from prophecy.test import BaseTestCase
from prophecy.test.utils import *
from python_unity_catalog.graph.SQLStatement_1_1 import *
import python_unity_catalog.config.ConfigStore as ConfigStore


class SQLStatement_1_1Test(BaseTestCase):

    def test_unit_test_0(self):
        dfIn0 = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/python_unity_catalog/graph/SQLStatement_1_1/in0/schema.json',
            'test/resources/data/python_unity_catalog/graph/SQLStatement_1_1/in0/data/test_unit_test_0.json',
            'in0'
        )
        dfInput1 = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/python_unity_catalog/graph/SQLStatement_1_1/input1/schema.json',
            'test/resources/data/python_unity_catalog/graph/SQLStatement_1_1/input1/data/test_unit_test_0.json',
            'input1'
        )
        dfOut1 = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/python_unity_catalog/graph/SQLStatement_1_1/out1/schema.json',
            'test/resources/data/python_unity_catalog/graph/SQLStatement_1_1/out1/data/test_unit_test_0.json',
            'out1'
        )
        dfOut = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/python_unity_catalog/graph/SQLStatement_1_1/out/schema.json',
            'test/resources/data/python_unity_catalog/graph/SQLStatement_1_1/out/data/test_unit_test_0.json',
            'out'
        )
        dfOutComputed, dfOut1Computed = SQLStatement_1_1(self.spark, dfIn0, dfInput1)
        assertDFEquals(
            dfOut1.select(
              "firstname",
              "middlename",
              "lastname",
              "id",
              "salary",
              "processed",
              "dob",
              "weight",
              "state",
              "city",
              "gender"
            ),
            dfOut1Computed.select(
              "firstname",
              "middlename",
              "lastname",
              "id",
              "salary",
              "processed",
              "dob",
              "weight",
              "state",
              "city",
              "gender"
            ),
            self.maxUnequalRowsToShow
        )
        assertDFEquals(
            dfOut.select(
              "firstname",
              "middlename",
              "lastname",
              "id",
              "salary",
              "processed",
              "dob",
              "weight",
              "state",
              "city",
              "gender"
            ),
            dfOutComputed.select(
              "firstname",
              "middlename",
              "lastname",
              "id",
              "salary",
              "processed",
              "dob",
              "weight",
              "state",
              "city",
              "gender"
            ),
            self.maxUnequalRowsToShow
        )

    def setUp(self):
        BaseTestCase.setUp(self)
        import os
        fabricName = os.environ['FABRIC_NAME']
        ConfigStore.Utils.initializeFromArgs(
            self.spark,
            Namespace(file = f"configs/resources/config/{fabricName}.json", config = None, overrideJson = None)
        )
