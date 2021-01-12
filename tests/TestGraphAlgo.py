import unittest
import json
import os.path
from pathlib import Path
import random

from src.NodeData import *
from src.DiGraph import *
import heapq
from src.GraphAlgo import *
from queue import PriorityQueue


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
        g1 = main_test_graph()
        ga1 = GraphAlgo(g1)
        ga1.save_to_json("test1.json")
        g2 = DiGraph()
        ga2 = GraphAlgo(g2)
        self.assertNotEqual(ga1.get_graph(), ga2.get_graph())
        ga2.load_from_json("test1.json")
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
        ga.plot_graph()
        ss = (1,2,3)
        print(ss[1])

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


#      >>> from GraphAlgo import GraphAlgo
#       >>> g_algo = GraphAlgo()
#        >>> g_algo.addNode(0)
#        >>> g_algo.addNode(1)
#        >>> g_algo.addNode(2)
#        >>> g_algo.addEdge(0,1,1)
#        >>> g_algo.addEdge(1,2,4)
#        >>> g_algo.shortestPath(0,1)
#        (1, [0, 1])
#        >>> g_algo.shortestPath(0,2)
#        (5, [0, 1, 2])


if __name__ == '__main__':
    unittest.main()

"""
    @Test
    void isConnected() {
        directed_weighted_graph dg = DWGraph_DSTest.mainTestGraph();
        dw_graph_algorithms dga = new DWGraph_Algo();
        dga.init(dg);
        assertFalse(dga.isConnected());
        dg.connect(3,4,3);
        assertFalse(dga.isConnected());
        dg.connect(2,3,3);
        dga.isConnected();
        assertTrue(dga.isConnected());
    }

    @Test
    void shortestPathDist() {
        directed_weighted_graph dg = DWGraph_DSTest.mainTestGraph();
        dw_graph_algorithms dga = new DWGraph_Algo();
        dga.init(dg);
        assertEquals(3,dga.shortestPathDist(1,3));
        dg.connect(3,4,3);
        assertEquals(6,dga.shortestPathDist(1,4));
        dg.connect(2,3,3);
        assertEquals(3,dga.shortestPathDist(1,3));
        assertEquals(14,dga.shortestPathDist(5,1));
        dg.removeNode(3);
        assertEquals(-1,dga.shortestPathDist(1,5));
        assertEquals(-1,dga.shortestPathDist(5,1));
    }

    @Test
    void shortestPath() {
        directed_weighted_graph dg = DWGraph_DSTest.mainTestGraph();
        dw_graph_algorithms dga = new DWGraph_Algo();
        dga.init(dg);
        ArrayList<Integer> test = new ArrayList<>();
        test.add(1);
        test.add(3);
        test.add(5);
        int index = 0;
        for (node_data n : dga.shortestPath(1,5)) {
            assertEquals(n.getKey(),test.get(index));
            index++;
        }
        ArrayList<Integer> test2 = new ArrayList<>();
        test2.add(3);
        test2.add(4);
        test2.add(1);
        test2.add(2);
        index = 0;
        assertNull(dga.shortestPath(3,2));
        dg.connect(3,4,3);
        dg.connect(2,3,3);
        for (node_data n : dga.shortestPath(3,2)) {
            assertEquals(n.getKey(),test2.get(index));
            index++;
        }
        assertNull(dga.shortestPath(1,55));
        assertNull(dga.shortestPath(-22,0));
    }

    @Test
    void save_load() {
        directed_weighted_graph dg = DWGraph_DSTest.mainTestGraph();
        dw_graph_algorithms dga = new DWGraph_Algo();
        dga.init(dg);
        dga.save("tests/IO/maintestgraph.json");
        directed_weighted_graph dg2 = new DWGraph_DS();
        dw_graph_algorithms dga2 = new DWGraph_Algo();
        dga2.init(dg2);
        dga2.load("tests/IO/maintestgraph.json");
        assertEquals(dga.getGraph(),dga2.getGraph());
        try {
            String a0 = Files.readString(Path.of("data/A0"));
            dga.load("data/A0");
            dga.save("tests/IO/2nd");
            String a2 = Files.readString(Path.of("tests/IO/2nd"));
            assertEquals(a0,a2);
        } catch (IOException e) {
            System.out.println("Wrong Input");
            e.printStackTrace();
        }
    }
}
"""