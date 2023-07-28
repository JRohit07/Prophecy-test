from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from argparse import Namespace
from prophecy.test import BaseTestCase
from prophecy.test.utils import *
from pythondoanything.graph.Join_1 import *
from pythondoanything.config.ConfigStore import *


class Join_1Test(BaseTestCase):

    def test_unit_test_0(self):
        dfIn0 = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/pythondoanything/graph/Join_1/in0/schema.json',
            'test/resources/data/pythondoanything/graph/Join_1/in0/data/test_unit_test_0.json',
            'in0'
        )
        dfIn1 = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/pythondoanything/graph/Join_1/in1/schema.json',
            'test/resources/data/pythondoanything/graph/Join_1/in1/data/test_unit_test_0.json',
            'in1'
        )
        dfOut = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/pythondoanything/graph/Join_1/out/schema.json',
            'test/resources/data/pythondoanything/graph/Join_1/out/data/test_unit_test_0.json',
            'out'
        )
        dfOutComputed = Join_1(self.spark, dfIn0, dfIn1)
        assertDFEquals(
            dfOut.select(
              "c   short  --",
              "c  float",
              "c--boolean",
              "c- - -double",
              "c___-- string",
              "c_timestamp",
              "c_new_col"
            ),
            dfOutComputed.select(
              "c   short  --",
              "c  float",
              "c--boolean",
              "c- - -double",
              "c___-- string",
              "c_timestamp",
              "c_new_col"
            ),
            self.maxUnequalRowsToShow
        )

    def test_unit_test_1(self):
        dfIn0 = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/pythondoanything/graph/Join_1/in0/schema.json',
            'test/resources/data/pythondoanything/graph/Join_1/in0/data/test_unit_test_1.json',
            'in0'
        )
        dfIn1 = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/pythondoanything/graph/Join_1/in1/schema.json',
            'test/resources/data/pythondoanything/graph/Join_1/in1/data/test_unit_test_1.json',
            'in1'
        )
        dfOut = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/pythondoanything/graph/Join_1/out/schema.json',
            'test/resources/data/pythondoanything/graph/Join_1/out/data/test_unit_test_1.json',
            'out'
        )
        dfOutComputed = Join_1(self.spark, dfIn0, dfIn1)
        assertDFEquals(
            dfOut.select("c   short  --", "c-int-column type", "-- c-long", "c-decimal", "c  float"),
            dfOutComputed.select("c   short  --", "c-int-column type", "-- c-long", "c-decimal", "c  float"),
            self.maxUnequalRowsToShow
        )

    def setUp(self):
        BaseTestCase.setUp(self)
        import os
        fabricName = os.environ['FABRIC_NAME']
        Utils.initializeFromArgs(
            self.spark,
            Namespace(
              file = f"configs/resources/config/{fabricName}.json",
              config = None,
              overrideJson = None,
              defaultConfFile = None
            )
        )
