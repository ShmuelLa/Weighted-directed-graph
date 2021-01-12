import math
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


def generate_axis_positions(radius, nodes):
    distance = 2 * np.pi / nodes
    list_of_points = []
    for pos in range(0, nodes):
        list_of_points.append(
            (radius * np.cos(pos * distance), radius * np.sin(pos * distance), 0))
    return list_of_points


class GraphAlgo(GraphAlgoInterface):
    _scc_count = 0
    _positions = []

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

    def reset_graph(self):
        _scc_count = 0
        for node in self._graph.get_all_v().values():
            if node.get_tag() != -1 or node.get_info() != "":
                node.set_tag(-1)
                node.set_info("")
                node.on_scc_stack = False
                node.scc_index = -1
