import unittest

from test.perf_unitest_generate.graph.Subgraph_1.test_Reformat_2 import *
from test.perf_unitest_generate.graph.test_WindowFunction_1 import *
from test.perf_unitest_generate.graph.test_SchemaTransform_1 import *
from test.perf_unitest_generate.graph.test_Deduplicate_1 import *
from test.perf_unitest_generate.graph.test_FlattenSchema_1 import *
from test.perf_unitest_generate.graph.test_Reformat_1 import *
from test.perf_unitest_generate.graph.test_SetOperation_1 import *
from test.perf_unitest_generate.graph.test_OrderBy_1 import *
from test.perf_unitest_generate.graph.test_Aggregate_1 import *
from test.perf_unitest_generate.graph.test_Filter_1 import *
from test.perf_unitest_generate.graph.test_RowDistributor_1 import *
from test.perf_unitest_generate.graph.test_Limit_1 import *
from test.perf_unitest_generate.graph.test_Repartition_1 import *
from test.perf_unitest_generate.graph.test_Join_1 import *

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(unittest.TestSuite())
