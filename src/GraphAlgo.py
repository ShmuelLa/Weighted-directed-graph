import os
from pathlib import Path
from typing import List

from src.GraphAlgoInterface import GraphAlgoInterface
from src.DiGraph import *


class GraphAlgo(GraphAlgoInterface):

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
        @returns True if the loading was successful, False o.w.
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

        Example:
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

        Notes:
        If there is no path between id1 and id2, or one of them dose not exist the function returns (float('inf'),[])
        More info:
        https://en.wikipedia.org/wiki/Dijkstra's_algorithm
        """
        pass

    def connected_component(self, id1: int) -> list:
        """
        Finds the Strongly Connected Component(SCC) that node id1 is a part of.
        @param id1: The node id
        @return: The list of nodes in the SCC

        Notes:
        If the graph is None or id1 is not in the graph, the function should return an empty list []
        """
        pass

    def connected_components(self) -> List[list]:
        """
        Finds all the Strongly Connected Component(SCC) in the graph.
        @return: The list all SCC

        Notes:
        If the graph is None the function should return an empty list []
        """
        pass

    def plot_graph(self) -> None:
        """
        Plots the graph.
        If the nodes have a position, the nodes will be placed there.
        Otherwise, they will be placed in a random but elegant manner.
        @return: None
        """
        pass

"""
    public directed_weighted_graph copy() {
        directed_weighted_graph result = new DWGraph_DS();
        if (this._algo_graph.nodeSize() == 0) return result;
        for (node_data n : this._algo_graph.getV()) {
            result.addNode(n);
        }
        if (this._algo_graph.edgeSize() == 0) return result;
        for (node_data n : this._algo_graph.getV()) {
            for (edge_data e : this._algo_graph.getE(n.getKey())) {
                result.connect(e.getSrc(), e.getDest(), e.getWeight());
            }
        }
        return result;
    }
    
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

    public synchronized double shortestPathDist(int src, int dest) {
        if (this._algo_graph.nodeSize()<=1 || this._algo_graph.getNode(src)==null || this._algo_graph.getNode(dest)==null) return -1;
        if (src == dest) return 0.0;
        PriorityQueue<node_data> pq = new PriorityQueue<>();
        double result;
        node_data current = this._algo_graph.getNode(src);
        pq.add(current);
        current.setTag(0);
        while (!pq.isEmpty()) {
            current = pq.poll();
            if (!Objects.equals(current.getInfo(), "y")) {
                current.setInfo("y");
                if (current.getKey() == dest) break;
                for (edge_data e : this._algo_graph.getE(current.getKey())) {
                    if (this._algo_graph.getNode(e.getDest()).getTag() == -1) {
                        this._algo_graph.getNode(e.getDest()).setTag(Integer.MAX_VALUE);
                    }
                    double tmp_tag = current.getTag()+this._algo_graph.getEdge(current.getKey(),e.getDest()).getWeight();
                    if (tmp_tag < this._algo_graph.getNode(e.getDest()).getTag()) {
                        this._algo_graph.getNode(e.getDest()).setTag((int) tmp_tag);
                        pq.add(this._algo_graph.getNode(e.getDest()));
                    }
                }
            }
        }
        current = this._algo_graph.getNode(dest);
        result = current.getTag();
        if (!Objects.equals(current.getInfo(), "y")) {
            this.reset();
            return -1;
        }
        this.reset();
        return result;
    }

    public synchronized List<node_data> shortestPath(int src, int dest) {
        if (this._algo_graph.nodeSize()<=1 || this._algo_graph.getNode(src)==null || this._algo_graph.getNode(dest)==null) return null;
        if (src == dest) return new ArrayList<>();
        PriorityQueue<node_data> pq = new PriorityQueue<>();
        List<node_data> result = new ArrayList<>();
        HashMap<node_data,node_data> parent = new HashMap<>();
        node_data current = this._algo_graph.getNode(src);
        pq.add(current);
        current.setTag(0);
        while (!pq.isEmpty()) {
            current = pq.poll();
            if (!Objects.equals(current.getInfo(),"y")) {
                current.setInfo("y");
                if (current.getKey() == dest) break;
                for (edge_data e : this._algo_graph.getE(current.getKey())) {
                    if (this._algo_graph.getNode(e.getDest()).getTag() == -1) {
                        this._algo_graph.getNode(e.getDest()).setTag(Integer.MAX_VALUE);
                    }
                    double tmp_tag = current.getTag()+this._algo_graph.getEdge(current.getKey(),e.getDest()).getWeight();
                    if (tmp_tag < this._algo_graph.getNode(e.getDest()).getTag()) {
                        this._algo_graph.getNode(e.getDest()).setTag((int) tmp_tag);
                        parent.put(this._algo_graph.getNode(e.getDest()),current);
                        pq.add(this._algo_graph.getNode(e.getDest()));
                    }
                }
            }
        }
        current = this._algo_graph.getNode(dest);
        if (!Objects.equals(current.getInfo(), "y")) {
            this.reset();
            return null;
        }
        result.add(0,current);
        while (current.getKey() != src) {
            result.add(0,parent.get(current));
            current = parent.get(current);
        }
        this.reset();
        return result;
    }

    public void reset() {
        for (node_data n : this._algo_graph.getV()) {
            if (n.getTag() != 0 || n.getInfo() != null) {
                n.setTag(-1);
                n.setInfo(null);
            }
        }
    }
"""
