from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from argparse import Namespace
from prophecy.test import BaseTestCase
from prophecy.test.utils import *
from pythonbasic.test.mainone.graph.Script_4 import *
from pythonbasic.test.mainone.config.ConfigStore import *


class Script_4Test(BaseTestCase):

    def test_unit_test_0(self):
        dfIn0 = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/pythonbasic/test/mainone/graph/Script_4/in0/schema.json',
            'test/resources/data/pythonbasic/test/mainone/graph/Script_4/in0/data/test_unit_test_0.json',
            'in0'
        )
        dfOut0 = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/pythonbasic/test/mainone/graph/Script_4/out0/schema.json',
            'test/resources/data/pythonbasic/test/mainone/graph/Script_4/out0/data/test_unit_test_0.json',
            'out0'
        )
        dfOut0Computed = Script_4(self.spark, dfIn0)

    def test_unit_test_1(self):
        dfIn0 = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/pythonbasic/test/mainone/graph/Script_4/in0/schema.json',
            'test/resources/data/pythonbasic/test/mainone/graph/Script_4/in0/data/test_unit_test_1.json',
            'in0'
        )
        dfOut0 = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/pythonbasic/test/mainone/graph/Script_4/out0/schema.json',
            'test/resources/data/pythonbasic/test/mainone/graph/Script_4/out0/data/test_unit_test_1.json',
            'out0'
        )
        dfOut0Computed = Script_4(self.spark, dfIn0)

    def test_unit_test_2(self):
        dfIn0 = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/pythonbasic/test/mainone/graph/Script_4/in0/schema.json',
            'test/resources/data/pythonbasic/test/mainone/graph/Script_4/in0/data/test_unit_test_2.json',
            'in0'
        )
        dfOut0 = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/pythonbasic/test/mainone/graph/Script_4/out0/schema.json',
            'test/resources/data/pythonbasic/test/mainone/graph/Script_4/out0/data/test_unit_test_2.json',
            'out0'
        )
        dfOut0Computed = Script_4(self.spark, dfIn0)

    def test_unit_test_3(self):
        dfIn0 = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/pythonbasic/test/mainone/graph/Script_4/in0/schema.json',
            'test/resources/data/pythonbasic/test/mainone/graph/Script_4/in0/data/test_unit_test_3.json',
            'in0'
        )
        dfOut0 = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/pythonbasic/test/mainone/graph/Script_4/out0/schema.json',
            'test/resources/data/pythonbasic/test/mainone/graph/Script_4/out0/data/test_unit_test_3.json',
            'out0'
        )
        dfOut0Computed = Script_4(self.spark, dfIn0)

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
