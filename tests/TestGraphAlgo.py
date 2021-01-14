import unittest
import os.path
import random
from src.GraphAlgo import *
import time


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

    def test_g(self):
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
        gal_red = GraphAlgo(red)
        print(gal_red.connected_components())

    def test_single_scc(self):
        g1 = main_test_graph()
        ga = GraphAlgo(g1)
        self.assertEqual(ga.connected_component(1), [1])
        self.assertEqual(ga.connected_component(3), [3, 5] or [5, 3])

    def test_big_scc(self):
        g1 = main_test_graph()
        ga = GraphAlgo(g1)
        ga.load_from_json("..\data\Graphs_on_circle\G_30000_240000_1.json")
        time1 = int(round(time.time() * 1000))
        ga.connected_components()
        time2 = int(round(time.time() * 1000))
        self.assertTrue((time2 - time1) / 1000 < 10)

    def test_1(self):
        graph = DiGraph()
        self.assertEqual(0, graph.e_size())
        self.assertEqual(0, graph.v_size())
        for i in range(0, 5):
            self.assertEqual(i, graph.v_size())
            graph.add_node(i, None)
        graph.remove_node(2)
        self.assertEqual(4, graph.v_size())
        graph.remove_node(2)
        self.assertEqual(4, graph.v_size())
        self.assertTrue(graph.add_edge(0, 1, 2))
        self.assertEqual(1, graph.e_size())
        self.assertTrue(graph.remove_node(0))
        self.assertEqual(0, len(graph.all_out_edges_of_node(0)))
        self.assertEqual(0, graph.e_size())

    def test_3(self):
        graph = DiGraph()
        for i in range(0, 20):
            graph.add_node(i)
        self.assertEqual(20, graph.v_size())
        for i in range(5, 10):
            graph.remove_node(i)
        self.assertEqual(15, graph.v_size())
        for i in range(10, 12):
            graph.remove_node(i)
        self.assertEqual(13, graph.v_size())
    
    def test_2(self):
        graph = DiGraph()
        for i in range(0, 10):
            graph.add_node(i)
        self.assertEqual(10, graph.v_size())
        self.assertEqual(10, graph.get_mc())
        for i in range(0, 9):
            graph.add_edge(i, i + 1, i + 1)
        self.assertEqual(9, graph.e_size())
        self.assertEqual(19, graph.get_mc())
        for i in range(6, 10):
            graph.remove_node(i)
        self.assertEqual(6, graph.v_size())

    def test_9(self):
        blue = DiGraph()
        for i in range(10, 24):
            blue.add_node(i)
        for i in range(10, 18):
            blue.add_edge(i, i + 1, i + 1)
        blue.add_edge(18, 10, 1)
        blue.add_edge(19, 18, 1)
        blue.add_edge(19, 20, 1)
        blue.add_edge(20, 17, 1)
        blue.add_edge(15, 21, 1)
        blue.add_edge(22, 21, 1)
        blue.add_edge(14, 22, 1)
        blue.add_edge(23, 22, 1)
        gal_blue = GraphAlgo(blue)
        self.assertEqual(len(gal_blue.connected_components()), 6)
        self.assertEqual(len(gal_blue.connected_component(10)), 9)

    def test_4(self):
        graph = DiGraph()
        random.seed(1, 1)
        for i in range(0, 10):
            graph.add_node(i)
        for i in range(0, 10):
            w = float("{:.2f}".format(i * random.random()))
            graph.add_edge(i, i + 1, w)
        self.assertEqual(10, graph.v_size())
        self.assertEqual(9, graph.e_size())
        graph.remove_node(0)
        self.assertEqual(8, graph.e_size())

    def test_7(self):
        graph = DiGraph()
        with open("../data/A0", "r") as f:
            data = json.load(f)
        nodes = data["Nodes"]
        for i in range(0, len(nodes)):
            node_data = nodes[i]
            graph.add_node(node_data["id"], node_data["pos"])
        edges = data["Edges"]
        for i in range(0, len(edges)):
            edge_data = edges[i]
            graph.add_edge(edge_data["src"], edge_data["dest"], edge_data["w"])

    def test_10(self):
        red = DiGraph()
        for i in range(6):
            red.add_node(i)
        red.add_edge(0, 1, 4)
        red.add_edge(2, 0, 5)
        red.add_edge(1, 2, 1)
        red.add_edge(2, 3, 2)
        red.add_edge(3, 4, 3)
        red.add_edge(2, 5, 4)
        red.add_edge(0, 2, 7)
        galred = GraphAlgo(red)
        self.assertEqual(galred.shortest_path(0, 4)[0], 10)
        self.assertEqual(galred.shortest_path(0, 2)[0], 5)
        self.assertEqual(len(galred.connected_components()), 4)


if __name__ == '__main__':
    unittest.main()
