from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from argparse import Namespace
from prophecy.test import BaseTestCase
from prophecy.test.utils import *
from livy_python.graph.SchemaTransform_1 import *
from livy_python.config.ConfigStore import *


class SchemaTransform_1Test(BaseTestCase):

    def test_unit_test_0(self):
        dfIn0 = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/livy_python/graph/SchemaTransform_1/in0/schema.json',
            'test/resources/data/livy_python/graph/SchemaTransform_1/in0/data/test_unit_test_0.json',
            'in0'
        )
        dfOut = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/livy_python/graph/SchemaTransform_1/out/schema.json',
            'test/resources/data/livy_python/graph/SchemaTransform_1/out/data/test_unit_test_0.json',
            'out'
        )
        dfOutComputed = SchemaTransform_1(self.spark, dfIn0)
        assertDFEquals(
            dfOut.select(
              "year",
              "industry_code_ANZSIC",
              "industry_name_ANZSIC",
              "rme_size_grp",
              "variable",
              "value_new",
              "indus_concat"
            ),
            dfOutComputed.select(
              "year",
              "industry_code_ANZSIC",
              "industry_name_ANZSIC",
              "rme_size_grp",
              "variable",
              "value_new",
              "indus_concat"
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
