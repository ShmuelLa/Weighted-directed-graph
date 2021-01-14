import json
import unittest
from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo
import random


class TestDiGraph(unittest.TestCase):

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

        for i in range(0, 9):
            graph.add_edge(i, i + 1, i + 2)
        self.assertEqual(9, graph.e_size())
        # self.assertEqual(28, graph.get_mc())

        for i in range(6, 10):
            graph.remove_node(i)
        self.assertEqual(6, graph.v_size())
        # self.assertEqual(32, graph.get_mc())

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

        for i in range(9, 5, -1):
            graph.remove_node(i)
        self.assertEqual(5, graph.e_size())

    def test_5(self):
        graph = DiGraph()
        random.seed(8, 1)
        for i in range(0, 10):
            graph.add_node(i)

        for i in range(2, 6):
            graph.add_edge(0, i, i - 1.5)

        for j in graph.all_out_edges_of_node(0):
            self.assertEqual(graph.get_edge(0, j), j - 1.5)

    def test_6(self):
        graph = DiGraph()
        self.assertFalse(graph.add_edge(1, 2, 4))

        graph.add_node(1)
        self.assertFalse(graph.add_edge(0, 1, 41))

        self.assertFalse(graph.add_edge(1, 1, 2))

        graph.add_node(2)
        self.assertTrue(graph.add_edge(1, 2, 4))
        self.assertEqual(4, graph.get_edge(1, 2))

        graph.add_edge(1, 2, 9.2)
        self.assertEqual(9.2, graph.get_edge(1, 2))

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

    def test_8(self):
        G8 = DiGraph()
        pass

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
        galblue = GraphAlgo(blue)
        self.assertEqual(len(galblue.connected_components()), 6)
        self.assertEqual(len(galblue.connected_component(10)), 9)

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

        green = DiGraph()
        for i in range(12):
            green.add_node(i)
        green.add_edge(0, 1, 4)
        green.add_edge(1, 2, 4)
        green.add_edge(2, 3, 4)
        green.add_edge(3, 0, 4)
        green.add_edge(1, 4, 4)
        green.add_edge(4, 5, 4)
        green.add_edge(5, 6, 4)
        green.add_edge(6, 4, 4)
        green.add_edge(6, 7, 4)
        green.add_edge(7, 8, 4)
        green.add_edge(6, 9, 4)
        green.add_edge(10, 4, 4)
        green.add_edge(11, 4, 4)
        green.add_edge(11, 10, 4)

        galgreen = GraphAlgo(green)
        # print(galgreen.connected_components())

        pink = DiGraph()
        for i in range(8):
            pink.add_node(i)
        pink.add_edge(0, 1, 4)
        pink.add_edge(1, 2, 4)
        pink.add_edge(2, 3, 4)
        pink.add_edge(3, 4, 4)
        pink.add_edge(4, 0, 4)
        pink.add_edge(0, 5, 4)
        pink.add_edge(0, 6, 4)
        pink.add_edge(0, 7, 4)
        galpink = GraphAlgo(pink)
        self.assertEqual(galpink.connected_component(0), [0, 4, 3, 2, 1])


if __name__ == '__main__':
    unittest.main()
