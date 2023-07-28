from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from argparse import Namespace
from prophecy.test import BaseTestCase
from prophecy.test.utils import *
from python_unity_catalog.graph.Subgraph_1.Subgraph_2.Reformat_4 import *
from python_unity_catalog.config.ConfigStore import *


class Reformat_4Test(BaseTestCase):

    def test_unit_test_0(self):
        dfIn0 = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/python_unity_catalog/graph/Subgraph_1/Subgraph_2/Reformat_4/in0/schema.json',
            'test/resources/data/python_unity_catalog/graph/Subgraph_1/Subgraph_2/Reformat_4/in0/data/test_unit_test_0.json',
            'in0'
        )
        dfOut = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/python_unity_catalog/graph/Subgraph_1/Subgraph_2/Reformat_4/out/schema.json',
            'test/resources/data/python_unity_catalog/graph/Subgraph_1/Subgraph_2/Reformat_4/out/data/test_unit_test_0.json',
            'out'
        )
        dfOutComputed = Reformat_4(self.spark, dfIn0)
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
        Utils.initializeFromArgs(
            self.spark,
            Namespace(
              file = f"configs/resources/config/{fabricName}.json",
              config = None,
              overrideJson = None,
              defaultConfFile = None
            )
        )
