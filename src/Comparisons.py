import matplotlib as plt
import time
import src.NodeData
import src.DiGraph
from src.GraphAlgo import *
from tests.TestDiGraph import main_test_graph


def python_times():
    g1 = main_test_graph()
    ga = GraphAlgo(g1)

    ga.load_from_json("..\data\Graphs_on_circle\G_30000_240000_1.json")
    start_time = time.time()
    ga.connected_components()
    t1 = (time.time() - start_time)
    print("G_30000_240000  -  " + str(t1) + "  - seconds")

    ga.load_from_json("..\data\Graphs_on_circle\G_30000_240000_1.json")
    start_time = time.time()
    ga.connected_components()
    t1 = (time.time() - start_time)
    print("G_30000_240000  -  " + str(t1) + "  - seconds")


if __name__ == '__main__':
    python_times()