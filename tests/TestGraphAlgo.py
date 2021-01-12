import unittest
import os.path
from src.GraphAlgo import *


def main_test_graph():
    dwg = DiGraph()
    for key in range(1, 6):
        dwg.add_node(key)
    dwg.add_edge(1, 2, 3)
    dwg.add_edge(1, 3, 3)
    dwg.add_edge(4, 1, 7)
    dwg.add_edge(3, 5, 7)
    dwg.add_edge(5, 3, 4)
    return dwg


class TestDiGraph(unittest.TestCase):

    def test_save_load(self):
        directory = os.getcwd()
        full_path = os.path.dirname(directory) + "\\data\\Saved_Graphs\\test1.json"
        g1 = main_test_graph()
        ga1 = GraphAlgo(g1)
        ga1.save_to_json(full_path)
        g2 = DiGraph()
        ga2 = GraphAlgo(g2)
        self.assertNotEqual(ga1.get_graph(), ga2.get_graph())
        ga2.load_from_json(full_path)
        self.assertEqual(ga1.get_graph(), ga2.get_graph())
        self.assertEqual(main_test_graph(), ga2.get_graph())

    def test_heapq_lt_gt(self):
        n1 = NodeData(1)
        n2 = NodeData(2)
        n3 = NodeData(3)
        n4 = NodeData(4)
        n5 = NodeData(5)
        priority = []
        n1.set_tag(-14.3)
        n2.set_tag(0)
        n3.set_tag(1)
        n4.set_tag(4)
        n5.set_tag(-100.1)
        heapq.heappush(priority, n5)
        heapq.heappush(priority, n3)
        heapq.heappush(priority, n4)
        heapq.heappush(priority, n2)
        heapq.heappush(priority, n1)

    def test_shortest_path(self):
        g1 = main_test_graph()
        ga1 = GraphAlgo(g1)
        self.assertEqual(ga1.shortest_path(4, 5), (17, [4, 1, 3, 5]))
        self.assertEqual(ga1.shortest_path(1, 5), (10, [1, 3, 5]))
        self.assertEqual(ga1.shortest_path(1, 1), (float('inf'), []))
        self.assertEqual(ga1.shortest_path(1, -11), (float('inf'), []))
        self.assertEqual(ga1.shortest_path(80, -11), (float('inf'), []))

    def test_scc(self):
        g1 = main_test_graph()
        ga = GraphAlgo(g1)
        print(ga.connected_components())

    def test_gidi(self):
        red = DiGraph()
        for i in range(6):
            red.add_node(i)
        red.add_edge(0, 1, 4)
        red.add_edge(2, 0, 1)
        red.add_edge(1, 2, 5)
        red.add_edge(2, 3, 6)
        red.add_edge(3, 4, 8)
        red.add_edge(2, 5, 2)
        red.add_edge(0, 2, 5)
        galred = GraphAlgo(red)
        print(galred.connected_components())

    def test_single_scc(self):
        g1 = main_test_graph()
        ga = GraphAlgo(g1)

    def test_big_scc(self):
        g1 = main_test_graph()
        ga = GraphAlgo(g1)
        ga.load_from_json("..\data\Graphs_on_circle\G_30000_240000_1.json")
        ga.connected_components()


if __name__ == '__main__':
    unittest.main()
