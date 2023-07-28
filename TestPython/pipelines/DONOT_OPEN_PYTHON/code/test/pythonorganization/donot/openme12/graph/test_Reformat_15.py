from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from argparse import Namespace
from prophecy.test import BaseTestCase
from prophecy.test.utils import *
from pythonorganization.donot.openme12.graph.Reformat_15 import *
from pythonorganization.donot.openme12.config.ConfigStore import *


class Reformat_15Test(BaseTestCase):

    def test_unit_test_0(self):
        dfIn0 = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/pythonorganization/donot/openme12/graph/Reformat_15/in0/schema.json',
            'test/resources/data/pythonorganization/donot/openme12/graph/Reformat_15/in0/data/test_unit_test_0.json',
            'in0'
        )
        dfOut = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/pythonorganization/donot/openme12/graph/Reformat_15/out/schema.json',
            'test/resources/data/pythonorganization/donot/openme12/graph/Reformat_15/out/data/test_unit_test_0.json',
            'out'
        )
        dfOutComputed = Reformat_15(self.spark, dfIn0)
        assertDFEquals(
            dfOut.select("_c0", "_c1", "_c2", "_c3", "_c4", "_c5", "_c6", "_c7", "_c8", "_c9"),
            dfOutComputed.select("_c0", "_c1", "_c2", "_c3", "_c4", "_c5", "_c6", "_c7", "_c8", "_c9"),
            self.maxUnequalRowsToShow
        )

    def test_unit_test_1(self):
        dfIn0 = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/pythonorganization/donot/openme12/graph/Reformat_15/in0/schema.json',
            'test/resources/data/pythonorganization/donot/openme12/graph/Reformat_15/in0/data/test_unit_test_1.json',
            'in0'
        )
        dfOut = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/pythonorganization/donot/openme12/graph/Reformat_15/out/schema.json',
            'test/resources/data/pythonorganization/donot/openme12/graph/Reformat_15/out/data/test_unit_test_1.json',
            'out'
        )
        dfOutComputed = Reformat_15(self.spark, dfIn0)
        assertDFEquals(
            dfOut.select("_c0", "_c1", "_c2", "_c3", "_c4", "_c5", "_c6", "_c7", "_c8", "_c9"),
            dfOutComputed.select("_c0", "_c1", "_c2", "_c3", "_c4", "_c5", "_c6", "_c7", "_c8", "_c9"),
            self.maxUnequalRowsToShow
        )

    def test_unit_test_2(self):
        dfIn0 = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/pythonorganization/donot/openme12/graph/Reformat_15/in0/schema.json',
            'test/resources/data/pythonorganization/donot/openme12/graph/Reformat_15/in0/data/test_unit_test_2.json',
            'in0'
        )
        dfOut = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/pythonorganization/donot/openme12/graph/Reformat_15/out/schema.json',
            'test/resources/data/pythonorganization/donot/openme12/graph/Reformat_15/out/data/test_unit_test_2.json',
            'out'
        )
        dfOutComputed = Reformat_15(self.spark, dfIn0)
        assertDFEquals(
            dfOut.select("_c0", "_c1", "_c2", "_c3", "_c4", "_c5", "_c6", "_c7", "_c8", "_c9"),
            dfOutComputed.select("_c0", "_c1", "_c2", "_c3", "_c4", "_c5", "_c6", "_c7", "_c8", "_c9"),
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
