import os
from collections import deque
import random
from typing import List
import heapq
from cycler import cycler
import matplotlib as mpl
import matplotlib.tri as tri
from src.GraphAlgoInterface import GraphAlgoInterface
from src.DiGraph import *
from matplotlib import pyplot as plt
import numpy as np

class GraphAlgo(GraphAlgoInterface):
    _scc_count = 0

    def __init__(self, graph: DiGraph):
        self._graph = graph

    def get_graph(self) -> GraphInterface:
        """
        :return: the directed graph on which the algorithm works on.
        """
        return self._graph

    def load_from_json(self, file_name: str) -> bool:
        """
        Loads a graph from a json file.
        @param file_name: The path to the json file
        @returns True if the loading was successful, False o.scc_index.
        """
        try:
            directory = os.getcwd()
            full_path = os.path.dirname(directory) + "\\data\\Saved_Graphs\\" + file_name
            result = DiGraph()
            with open(full_path) as json_file:
                data = json.load(json_file)
            edges = data.get("Edges")
            nodes = data.get("Nodes")
            for node in nodes:
                result.add_node(node.get("id"))
            for edge in edges:
                result.add_edge(edge.get("src"), edge.get("dest"), edge.get("w"))
            self._graph = result
            return True
        except FileNotFoundError or FileExistsError or OSError:
            print("Could not find/read file")
            return False

    def save_to_json(self, file_name: str) -> bool:
        """
        Saves the graph in JSON format to a file
        @param file_name: The path to the out file
        @return: True if the save was successful, False o.w.
        """
        try:
            directory = os.getcwd()
            full_path = os.path.dirname(directory) + "\\data\\Saved_Graphs\\" + file_name
            with open(full_path, "w") as json_path:
                print(self._graph.to_json(), file=json_path)
            return True
        except FileNotFoundError or FileExistsError or OSError:
            print("Could not create file")
            return False

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        """
        Returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm
        @param id1: The start node id
        @param id2: The end node id
        @return: The distance of the path, a list of the nodes ids that the path goes through

        Notes:
        If there is no path between id1 and id2, or one of them dose not exist the function returns (float('inf'),[])
        More info:
        https://en.wikipedia.org/wiki/Dijkstra's_algorithm
        """
        if id1 == id2 or self._graph.v_size() <= 1 or not self._graph.has_node(id1) or not self._graph.has_node(id2):
            return float('inf'), []
        pq = []
        result = []
        parent = {}
        current = self._graph.get_node(id1)
        heapq.heappush(pq, current)
        current.set_tag(0)
        while pq.__len__() > 0:
            current = heapq.heappop(pq)
            if not current.get_info() == "y":
                current.set_info("y")
                if current.get_key() == id2:
                    break
                for k, w in self._graph.all_out_edges_of_node(current.get_key()).items():
                    if self._graph.get_node(k).get_tag() == -1:
                        self._graph.get_node(k).set_tag(float('inf'))
                    tmp_tag = current.get_tag() + w
                    if tmp_tag < self._graph.get_node(k).get_tag():
                        self._graph.get_node(k).set_tag(tmp_tag)
                        parent[k] = current
                        heapq.heappush(pq, self._graph.get_node(k))
        current = self._graph.get_node(id2)
        if not current.get_info() == "y":
            self.reset_graph()
            return float('inf'), []
        result_distance = self._graph.get_node(id2).get_tag()
        result.insert(0, current.get_key())
        while current.get_key() != id1:
            result.insert(0, parent.get(current.get_key()).get_key())
            current = parent.get(current.get_key())
        self.reset_graph()
        return result_distance, result

    def connected_component(self, id1: int) -> list:
        """
        Finds the Strongly Connected Component(SCC) that node id1 is a part of.
        @param id1: The node id
        @return: The list of nodes in the SCC

        Notes:
        If the graph is None or id1 is not in the graph, the function should return an empty list []
        """
        if not self._graph.get_node(id1) or self._graph.v_size() <= 1 or self._graph is None:
            return []
        pass

    def connected_components(self) -> List[list]:
        """
        Finds all the Strongly Connected Component(SCC) in the graph.
        @return: The list all SCC

        Notes:
        If the graph is None the function should return an empty list []
        """
        if self._graph is None:
            return []
        stack = deque()
        single_component = {}
        result = []
        for node in self._graph.get_all_v().values():
            if node.scc_index == -1:
                self.dfs(node, stack, single_component)
        for value in single_component.values():
            result.append(value)
        self.reset_graph()
        return result

    def dfs(self, node: NodeData, stack: deque, single_component: {}):
        stack.append(node)
        node.set_info("y")
        node.scc_index = self._scc_count
        node.set_tag(self._scc_count)
        self._scc_count += 1
        for curr_node in self.get_graph().all_out_edges_of_node(node.get_key()).keys():
            tmp_node = self._graph.get_node(curr_node)
            if tmp_node.scc_index == -1:
                self.dfs(tmp_node, stack, single_component)
                node.set_tag(min(node.get_tag(), tmp_node.get_tag()))
            elif tmp_node.get_info() == "y":
                node.set_tag(min(node.get_tag(), tmp_node.scc_index))
        if node.get_tag() == node.scc_index:
            node_index = float("-inf")
            while node_index != node.get_key():
                tmp_node = stack.pop()
                node_index = tmp_node.get_key()
                if node.get_tag() not in single_component:
                    single_component[node.get_tag()] = []
                    single_component[node.get_tag()].append(tmp_node.get_key())
                else:
                    single_component[node.get_tag()].append(tmp_node.get_key())
                tmp_node.set_info("")

    def plot_graph(self) -> None:
        """
        Plots the graph.
        If the nodes have a position, the nodes will be placed there.
        Otherwise, they will be placed in a random but elegant manner.
        @return: None
        """
        arrow_parameters = {'length_includes_head': True, 'head_width': 0.01, 'head_length': 0.03, 'shape': 'left',
                            'fc': 'k', 'ec': None, 'alpha': 0.6}
        for node in self._graph.get_all_v().values():
            if node.get_position() == ():
                node.rand_pos()
        for node in self._graph.get_all_v().values():
            x = node.get_position()[0]
            y = node.get_position()[1]
            print(x, y)
            plt.plot(x, y, '-o')
            plt.annotate(str(node.get_key()), [x, y+0.025])
            for ni in self._graph.all_out_edges_of_node(node.get_key()).keys():
                tmp_node = self._graph.get_node(ni)
                x2 = tmp_node.get_position()[0]
                y2 = tmp_node.get_position()[1]
                plt.arrow(x, y, -(x-x2), -(y-y2), **arrow_parameters)
        plt.xlabel("x label")
        plt.ylabel("y label")
        plt.title("Weighted Directed Graph")
        plt.show()

        """
        # First create the x and y coordinates of the points.
        n_angles = 36
        n_radii = 8
        min_radius = 0.25
        radii = np.linspace(min_radius, 0.95, n_radii)

        angles = np.linspace(0, 2 * np.pi, n_angles, endpoint=False)
        angles = np.repeat(angles[..., np.newaxis], n_radii, axis=1)
        angles[:, 1::2] += np.pi / n_angles

        x = (radii * np.cos(angles)).flatten()
        y = (radii * np.sin(angles)).flatten()


        ###############################################################################
        # You can specify your own triangulation rather than perform a Delaunay
        # triangulation of the points, where each triangle is given by the indices of
        # the three points that make up the triangle, ordered in either a clockwise or
        # anticlockwise manner.

        xy = np.asarray([
            [-0.101, 0.872], [-0.080, 0.883], [-0.069, 0.888], [-0.054, 0.890],
            [-0.045, 0.897], [-0.057, 0.895], [-0.073, 0.900], [-0.087, 0.898],
            [-0.090, 0.904], [-0.069, 0.907], [-0.069, 0.921], [-0.080, 0.919],
            [-0.073, 0.928], [-0.052, 0.930], [-0.048, 0.942], [-0.062, 0.949],
            [-0.054, 0.958], [-0.069, 0.954], [-0.087, 0.952], [-0.087, 0.959],
            [-0.080, 0.966], [-0.085, 0.973], [-0.087, 0.965], [-0.097, 0.965],
            [-0.097, 0.975], [-0.092, 0.984], [-0.101, 0.980], [-0.108, 0.980],
            [-0.104, 0.987], [-0.102, 0.993], [-0.115, 1.001], [-0.099, 0.996],
            [-0.101, 1.007], [-0.090, 1.010], [-0.087, 1.021], [-0.069, 1.021],
            [-0.052, 1.022], [-0.052, 1.017], [-0.069, 1.010], [-0.064, 1.005],
            [-0.048, 1.005], [-0.031, 1.005], [-0.031, 0.996], [-0.040, 0.987],
            [-0.045, 0.980], [-0.052, 0.975], [-0.040, 0.973], [-0.026, 0.968],
            [-0.020, 0.954], [-0.006, 0.947], [0.003, 0.935], [0.006, 0.926],
            [0.005, 0.921], [0.022, 0.923], [0.033, 0.912], [0.029, 0.905],
            [0.017, 0.900], [0.012, 0.895], [0.027, 0.893], [0.019, 0.886],
            [0.001, 0.883], [-0.012, 0.884], [-0.029, 0.883], [-0.038, 0.879],
            [-0.057, 0.881], [-0.062, 0.876], [-0.078, 0.876], [-0.087, 0.872],
            [-0.030, 0.907], [-0.007, 0.905], [-0.057, 0.916], [-0.025, 0.933],
            [-0.077, 0.990], [-0.059, 0.993]])
        x = np.degrees(xy[:, 0])
        y = np.degrees(xy[:, 1])

        triangles = np.asarray([
            [67, 66, 1], [65, 2, 66], [1, 66, 2], [64, 2, 65], [63, 3, 64],
            [60, 59, 57], [2, 64, 3], [3, 63, 4], [0, 67, 1], [62, 4, 63],
            [57, 59, 56], [59, 58, 56], [61, 60, 69], [57, 69, 60], [4, 62, 68],
            [6, 5, 9], [61, 68, 62], [69, 68, 61], [9, 5, 70], [6, 8, 7],
            [4, 70, 5], [8, 6, 9], [56, 69, 57], [69, 56, 52], [70, 10, 9],
            [54, 53, 55], [56, 55, 53], [68, 70, 4], [52, 56, 53], [11, 10, 12],
            [69, 71, 68], [68, 13, 70], [10, 70, 13], [51, 50, 52], [13, 68, 71],
            [52, 71, 69], [12, 10, 13], [71, 52, 50], [71, 14, 13], [50, 49, 71],
            [49, 48, 71], [14, 16, 15], [14, 71, 48], [17, 19, 18], [17, 20, 19],
            [48, 16, 14], [48, 47, 16], [47, 46, 16], [16, 46, 45], [23, 22, 24],
            [21, 24, 22], [17, 16, 45], [20, 17, 45], [21, 25, 24], [27, 26, 28],
            [20, 72, 21], [25, 21, 72], [45, 72, 20], [25, 28, 26], [44, 73, 45],
            [72, 45, 73], [28, 25, 29], [29, 25, 31], [43, 73, 44], [73, 43, 40],
            [72, 73, 39], [72, 31, 25], [42, 40, 43], [31, 30, 29], [39, 73, 40],
            [42, 41, 40], [72, 33, 31], [32, 31, 33], [39, 38, 72], [33, 72, 38],
            [33, 38, 34], [37, 35, 38], [34, 38, 35], [35, 37, 36]])

        ###############################################################################
        # Rather than create a Triangulation object, can simply pass x, y and triangles
        # arrays to triplot directly.  It would be better to use a Triangulation object
        # if the same triangulation was to be used more than once to save duplicated
        # calculations.

        fig2, ax2 = plt.subplots()
        ax2.set_aspect('equal')
        ax2.triplot(x, y, triangles, 'go-', lw=1.0)
        ax2.set_title('triplot of user-specified triangulation')
        ax2.set_xlabel('Longitude (degrees)')
        ax2.set_ylabel('Latitude (degrees)')

        plt.show()
    """

    def reset_graph(self):
        _scc_count = 0
        for node in self._graph.get_all_v().values():
            if node.get_tag() != -1 or node.get_info() != "":
                node.set_tag(-1)
                node.set_info("")
                node.on_scc_stack = False
                node.scc_index = -1


"""
    public boolean isConnected() {
        if (this._algo_graph.nodeSize() <= 1 || this._algo_graph == null) return true;
        Queue<Integer> queue = new LinkedList<>();
        HashSet<Integer> visited = new HashSet<>();
        int tmp_node = this._algo_graph.getV().iterator().next().getKey();
        int test_node = tmp_node;
        queue.add(tmp_node);
        visited.add(tmp_node);
        while (!queue.isEmpty()) {
            tmp_node=queue.poll();
            for (edge_data edge : this._algo_graph.getE(tmp_node)) {
                if (!visited.contains(edge.getDest())) {
                    visited.add(edge.getDest());
                    queue.add(edge.getDest());
                }
            }
        }
        if (visited.size() != this._algo_graph.nodeSize()) return false;
        directed_weighted_graph reversed_graph = new DWGraph_DS();
        for (node_data n : this._algo_graph.getV()) {
            reversed_graph.addNode(n);
        }
        for (node_data n : this._algo_graph.getV()) {
            for (edge_data e : this._algo_graph.getE(n.getKey())) {
                reversed_graph.connect(e.getDest(),e.getSrc(),e.getWeight());
            }
        }
        queue.clear();
        visited.clear();
        tmp_node = test_node;
        queue.add(test_node);
        visited.add(tmp_node);
        while (!queue.isEmpty()) {
            tmp_node=queue.poll();
            for (edge_data edge : reversed_graph.getE(tmp_node)) {
                if (!visited.contains(edge.getDest())) {
                    visited.add(edge.getDest());
                    queue.add(edge.getDest());
                }
            }
        }
        if (visited.size() != reversed_graph.nodeSize()) return false;
        else return true;
    }
"""
