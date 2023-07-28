from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from argparse import Namespace
from prophecy.test import BaseTestCase
from prophecy.test.utils import *
from pythonorganization.donot.openme12.graph.Limit_6 import *
from pythonorganization.donot.openme12.config.ConfigStore import *


class Limit_6Test(BaseTestCase):

    def test_unit_test_0(self):
        dfIn0 = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/pythonorganization/donot/openme12/graph/Limit_6/in0/schema.json',
            'test/resources/data/pythonorganization/donot/openme12/graph/Limit_6/in0/data/test_unit_test_0.json',
            'in0'
        )
        dfOut = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/pythonorganization/donot/openme12/graph/Limit_6/out/schema.json',
            'test/resources/data/pythonorganization/donot/openme12/graph/Limit_6/out/data/test_unit_test_0.json',
            'out'
        )
        dfOutComputed = Limit_6(self.spark, dfIn0)
        assertDFEquals(dfOut.select("c_int"), dfOutComputed.select("c_int"), self.maxUnequalRowsToShow)

    def test_unit_test_1(self):
        dfIn0 = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/pythonorganization/donot/openme12/graph/Limit_6/in0/schema.json',
            'test/resources/data/pythonorganization/donot/openme12/graph/Limit_6/in0/data/test_unit_test_1.json',
            'in0'
        )
        dfOut = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/pythonorganization/donot/openme12/graph/Limit_6/out/schema.json',
            'test/resources/data/pythonorganization/donot/openme12/graph/Limit_6/out/data/test_unit_test_1.json',
            'out'
        )
        dfOutComputed = Limit_6(self.spark, dfIn0)
        assertDFEquals(dfOut.select("c_int"), dfOutComputed.select("c_int"), self.maxUnequalRowsToShow)

    def test_unit_test_2(self):
        dfIn0 = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/pythonorganization/donot/openme12/graph/Limit_6/in0/schema.json',
            'test/resources/data/pythonorganization/donot/openme12/graph/Limit_6/in0/data/test_unit_test_2.json',
            'in0'
        )
        dfOut = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/pythonorganization/donot/openme12/graph/Limit_6/out/schema.json',
            'test/resources/data/pythonorganization/donot/openme12/graph/Limit_6/out/data/test_unit_test_2.json',
            'out'
        )
        dfOutComputed = Limit_6(self.spark, dfIn0)
        assertDFEquals(dfOut.select("c_int"), dfOutComputed.select("c_int"), self.maxUnequalRowsToShow)

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
