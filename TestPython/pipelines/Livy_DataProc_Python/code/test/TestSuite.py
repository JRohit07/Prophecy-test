import unittest

from test.livy_python.graph.test_RowDistributor_1 import *
from test.livy_python.graph.pythonLivySG1_1.test_Reformat_4_1 import *
from test.livy_python.graph.pythonLivySG1_1.Subgraph_2_1.Subgraph_3_1.test_Reformat_6_1 import *
from test.livy_python.graph.pythonLivySG1_1.Subgraph_2_1.test_Reformat_5_1 import *
from test.livy_python.graph.pythonLivySG1_1.test_Filter_1_1 import *
from test.livy_python.graph.pythonLivySG1_1.test_OrderBy_1_1 import *
from test.livy_python.graph.Subgraph_4.test_Reformat_4_1 import *
from test.livy_python.graph.Subgraph_4.Subgraph_2_1.Subgraph_3_1.test_Reformat_6_1 import *
from test.livy_python.graph.Subgraph_4.Subgraph_2_1.test_Reformat_5_1 import *
from test.livy_python.graph.Subgraph_4.test_Filter_1_1 import *
from test.livy_python.graph.Subgraph_4.test_OrderBy_1_1 import *
from test.livy_python.graph.test_SetOperation_1 import *

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(unittest.TestSuite())
