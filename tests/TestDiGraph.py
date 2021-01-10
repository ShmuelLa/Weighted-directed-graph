import unittest
from src.DiGraph import DiGraph
from src.NodeData import NodeData


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

    def test_node(self):
        node1 = NodeData(1)
        self.assertEqual(node1.get_key(), 1)
        self.assertEqual(node1.get_tag(), -1)
        node1.set_tag(-22.2)
        self.assertEqual(node1.get_tag(), -22.2)
        self.assertEqual(node1.get_info(), "")
        node1.set_info("z")
        self.assertEqual(node1.get_info(), "z")

    def test_add_node(self):
        g1 = DiGraph()
        g1.add_node(1)
        self.assertEqual(g1.get_all_v().get(1).get_key(), 1)
        self.assertEqual(g1.get_all_v().__len__(), 1)
        g2 = main_test_graph()
        self.assertEqual(g2.v_size(), 5)

    def test_remove_node(self):
        g1 = DiGraph()
        g1.add_node(1)
        g1.remove_node(1)
        self.assertEqual(g1.get_all_v().__len__(), 0)

    def test_add_edge(self):
        g1 = main_test_graph()
        self.assertEqual(g1.e_size(), 5)

    def test_all_v(self):
        g1 = main_test_graph()
        self.assertEqual(g1.get_all_v().__len__(), 5)
        test_index = 1
        for i in g1.get_all_v().keys():
            self.assertEqual(g1.get_all_v().get(i).get_key(), test_index)
            test_index += 1

    def test_in_out_edges(self):
        g1 = main_test_graph()
        self.assertEqual(g1.all_in_edges_of_node(3).__len__(), 2)
        self.assertEqual(g1.all_in_edges_of_node(1).__len__(), 1)
        self.assertEqual(g1.all_out_edges_of_node(1).__len__(), 2)


if __name__ == '__main__':
    unittest.main()

