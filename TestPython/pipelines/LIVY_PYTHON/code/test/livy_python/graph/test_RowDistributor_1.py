from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from argparse import Namespace
from prophecy.test import BaseTestCase
from prophecy.test.utils import *
from livy_python.graph.RowDistributor_1 import *
from livy_python.config.ConfigStore import *


class RowDistributor_1Test(BaseTestCase):

    def test_unit_test_0(self):
        dfIn0 = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/livy_python/graph/RowDistributor_1/in0/schema.json',
            'test/resources/data/livy_python/graph/RowDistributor_1/in0/data/test_unit_test_0.json',
            'in0'
        )
        dfOut1 = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/livy_python/graph/RowDistributor_1/out1/schema.json',
            'test/resources/data/livy_python/graph/RowDistributor_1/out1/data/test_unit_test_0.json',
            'out1'
        )
        dfOut0 = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/livy_python/graph/RowDistributor_1/out0/schema.json',
            'test/resources/data/livy_python/graph/RowDistributor_1/out0/data/test_unit_test_0.json',
            'out0'
        )
        dfOut0Computed, dfOut1Computed = RowDistributor_1(self.spark, dfIn0)
        assertDFEquals(
            dfOut0.select(
              "year",
              "industry_code_ANZSIC",
              "industry_name_ANZSIC",
              "rme_size_grp",
              "variable",
              "value",
              "unit"
            ),
            dfOut0Computed.select(
              "year",
              "industry_code_ANZSIC",
              "industry_name_ANZSIC",
              "rme_size_grp",
              "variable",
              "value",
              "unit"
            ),
            self.maxUnequalRowsToShow
        )

    def test_unit_test_1(self):
        dfIn0 = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/livy_python/graph/RowDistributor_1/in0/schema.json',
            'test/resources/data/livy_python/graph/RowDistributor_1/in0/data/test_unit_test_1.json',
            'in0'
        )
        dfOut1 = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/livy_python/graph/RowDistributor_1/out1/schema.json',
            'test/resources/data/livy_python/graph/RowDistributor_1/out1/data/test_unit_test_1.json',
            'out1'
        )
        dfOut0 = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/livy_python/graph/RowDistributor_1/out0/schema.json',
            'test/resources/data/livy_python/graph/RowDistributor_1/out0/data/test_unit_test_1.json',
            'out0'
        )
        dfOut0Computed, dfOut1Computed = RowDistributor_1(self.spark, dfIn0)
        assertDFEquals(
            dfOut0.select(
              "year",
              "industry_code_ANZSIC",
              "industry_name_ANZSIC",
              "rme_size_grp",
              "variable",
              "value",
              "unit"
            ),
            dfOut0Computed.select(
              "year",
              "industry_code_ANZSIC",
              "industry_name_ANZSIC",
              "rme_size_grp",
              "variable",
              "value",
              "unit"
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
        dfgraph_Lookup_1 = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/livy_python/graph/Lookup_1/schema.json',
            'test/resources/data/livy_python/graph/Lookup_1/data.json',
            "in0"
        )
        from livy_python.graph.Lookup_1 import Lookup_1
        Lookup_1(self.spark, dfgraph_Lookup_1)
