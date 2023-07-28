from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from argparse import Namespace
from prophecy.test import BaseTestCase
from prophecy.test.utils import *
from python_unity_catalog.graph.Join_1 import *
import python_unity_catalog.config.ConfigStore as ConfigStore


class Join_1Test(BaseTestCase):

    def test_unit_test_0(self):
        dfIn0 = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/python_unity_catalog/graph/Join_1/in0/schema.json',
            'test/resources/data/python_unity_catalog/graph/Join_1/in0/data/test_unit_test_0.json',
            'in0'
        )
        dfIn1 = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/python_unity_catalog/graph/Join_1/in1/schema.json',
            'test/resources/data/python_unity_catalog/graph/Join_1/in1/data/test_unit_test_0.json',
            'in1'
        )
        dfOut = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/python_unity_catalog/graph/Join_1/out/schema.json',
            'test/resources/data/python_unity_catalog/graph/Join_1/out/data/test_unit_test_0.json',
            'out'
        )
        dfOutComputed = Join_1(self.spark, dfIn0, dfIn1)
        assertDFEquals(
            dfOut.select("c_tinyint", "c_smallint", "c_int", "c_bigint", "c_float", "c_double", "c_string", "c_boolean"),
            dfOutComputed.select(
              "c_tinyint",
              "c_smallint",
              "c_int",
              "c_bigint",
              "c_float",
              "c_double",
              "c_string",
              "c_boolean"
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
