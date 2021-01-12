import os
from collections import deque
from typing import List
import heapq
from src.GraphAlgoInterface import GraphAlgoInterface
from src.DiGraph import *
from matplotlib import pyplot as plt
import numpy as np


def generate_axis_positions(radius, nodes) -> list:
    """
    Generates a constant distance between the nodes on the graph.
    This method is meant to be used in the the node does not have a position set beforehand

    :param radius: The constant radius of the distance
    :param nodes: The number of nodes on the graph
    :return: a list containing the positions
    """
    if nodes == 0:
        return []
    distance = 2 * np.pi / nodes
    list_of_points = []
    for pos in range(0, nodes):
        list_of_points.append(
            (radius * np.cos(pos * distance), radius * np.sin(pos * distance), 0))
    return list_of_points


class GraphAlgo(GraphAlgoInterface):
    """
    This class implements directed weighted graph algorithms including SCC and plotting
    """
    _positions = []

    def __init__(self, graph: DiGraph):
        """
        The graph algo constructor

        :param graph: The graph to initialize
        """
        self._graph = graph

    def get_graph(self) -> GraphInterface:
        """
        Returns the current graph this class is set on

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
            result = DiGraph()
            with open(file_name) as json_file:
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
            print("Could not find/read file (Check if you inserted full path)")
            return False

    def save_to_json(self, file_name: str) -> bool:
        """
        Saves the graph in JSON format to a file

        @param file_name: The path to the out file
        @return: True if the save was successful, False o.w.
        """
        try:
            with open(file_name, "w") as json_path:
                print(self._graph.to_json(), file=json_path)
            return True
        except FileNotFoundError or FileExistsError or OSError:
            print("Could not create file")
            return False

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        """
        Returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm
        If there is no path between id1 and id2, or one of them dose not exist the function returns (float('inf'),[])
        More info:
        https://en.wikipedia.org/wiki/Dijkstra's_algorithm

        @param id1: The start node id
        @param id2: The end node id
        @return: A list containing (distance: float, path: list)
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

    def bfs(self, node: int) -> list:
        queue = deque()
        tmp_node = node
        first_list = []
        reversed_list = []
        queue.append(tmp_node)
        self._graph.get_node(tmp_node).set_info("y")
        while queue.__len__() > 0:
            tmp_node = queue.pop()
            for ni in self._graph.all_out_edges_of_node(tmp_node).keys():
                if self._graph.get_node(ni).get_info() != "y":
                    self._graph.get_node(ni).set_info("y")
                    queue.append(ni)
        reversed_graph = DiGraph()
        for key, nd in self._graph.get_all_v().items():
            if nd.get_info() == "y":
                first_list.append(nd.get_key())
            reversed_graph.add_node(key)
        for nd in self._graph.get_all_v().keys():
            for k, w in self._graph.all_out_edges_of_node(nd).items():
                reversed_graph.add_edge(k, nd, w)
        queue.clear()
        tmp_node = node
        queue.append(tmp_node)
        reversed_graph.get_node(tmp_node).set_info("y")
        while queue.__len__() > 0:
            tmp_node = queue.pop()
            for ni in reversed_graph.all_out_edges_of_node(tmp_node).keys():
                if reversed_graph.get_node(ni).get_info() != "y":
                    reversed_graph.get_node(ni).set_info("y")
                    queue.append(ni)
        for key, nd in reversed_graph.get_all_v().items():
            if nd.get_info() == "y":
                reversed_list.append(key)
        result = list(set(first_list) & set(reversed_list))
        self.reset_graph()
        return result

    def connected_component(self, id1: int) -> list:
        """
        Finds the Strongly Connected Component(SCC) that node id1 is a part of.
        If the graph is None or id1 is not in the graph, the function should return an empty list []

        @param id1: The node id
        @return: The list of nodes in the SCC
        """
        if not self._graph.get_node(id1) or self._graph.v_size() <= 1 or self._graph is None:
            return []
        stack = deque()
        single_component = {}
        result = []
        self.bfs(id1)
        for value in single_component.values():
            result.append(value)
        self.reset_graph()
        return result

    def connected_components(self) -> List[list]:
        """
        Finds all the Strongly Connected Component(SCC) in the graph.
        If the graph is None the function should return an empty list []

        @return: The list all SCC
        """
        if self._graph is None:
            return []
        self.scc_stack_reset()
        result = []
        for key, node in self._graph.get_all_v().items():
            if not node.on_scc_stack:
                tmp_lst = self.bfs(key)
                result.append(tmp_lst)
                for n in tmp_lst:
                    self._graph.get_node(n).on_scc_stack = True
        self.reset_graph()
        return result

    def plot_graph(self) -> None:
        """
        Plots the graph using Matplotlib
        If the nodes have a position, the nodes will be placed there.
        Otherwise, they will be placed in a random but elegant manner.

        @return: None
        """
        arrow_parameters = {'length_includes_head': True, 'head_width': 0.040, 'head_length': 0.07, 'shape': 'full',
                            'fc': 'k', 'ec': None, 'alpha': 0.7}
        self._positions = generate_axis_positions(1, self._graph.v_size())
        for node in self._graph.get_all_v().values():
            if node.get_position() == ():
                node.set_position(self._positions.pop())
        for node in self._graph.get_all_v().values():
            x = node.get_position()[0]
            y = node.get_position()[1]
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

    def reset_graph(self) -> None:
        """
        resets the state of the graph for algorithmic use
        """
        for node in self._graph.get_all_v().values():
            if node.get_tag() != -1 or node.get_info() != "":
                node.set_tag(-1)
                node.set_info("")
                node.scc_index = -1

    def scc_stack_reset(self):
        for node in self._graph.get_all_v().values():
            node.on_scc_stack = False
