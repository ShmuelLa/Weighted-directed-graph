import unittest
from src.DiGraph import DiGraph
from src.NodeData import NodeData


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

    def test_remove_node(self):
        g1 = DiGraph()
        g1.add_node(1)
        g1.remove_node(1)
        self.assertEqual(g1.get_all_v().__len__(), 0)


if __name__ == '__main__':
    unittest.main()

node1 = NodeData(1)
ttt = {1: node1, 2: "kssss"}
t2 = {node1.get_key(): node1}
