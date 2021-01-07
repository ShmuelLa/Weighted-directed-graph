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


if __name__ == '__main__':
    unittest.main()
