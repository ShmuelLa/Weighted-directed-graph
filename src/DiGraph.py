from src.GraphInterface import GraphInterface
from src.NodeData import NodeData


class DiGraph(GraphInterface):
    """
    This class represents a Directed Weighted Graph
    """

    def __init__(self):
        """
        The default DiGraph constructor
        """
        self._nodes = {}
        self._edges = {}
        self._mode_count = 0
        self._edge_size = 0

    def v_size(self) -> int:
        """
        Returns the number of vertices in this graph

        @return: The number of vertices in this graph
        """
        return self._nodes.__len__()

    def e_size(self) -> int:
        """
        Returns the number of edges in this graph

        @return: The number of edges in this graph
        """
        return self._edge_size

    def get_all_v(self) -> dict:
        """return a dictionary of all the nodes in the Graph, each node is represented using a pair
         (node_id, node_data)
        """
        return self._nodes

    def all_in_edges_of_node(self, id1: int) -> dict:
        """return a dictionary of all the nodes connected to (into) node_id ,
        each node is represented using a pair (other_node_id, weight)
         """
        return self._nodes.get(id1).get_incoming_neighbors()

    def all_out_edges_of_node(self, id1: int) -> dict:
        """return a dictionary of all the nodes connected from node_id , each node is represented using a pair
        (other_node_id, weight)
        """
        return self._nodes.get(id1).get_outgoing_neighbors()

    def get_mc(self) -> int:
        """
        Returns the current version of this graph,
        on every change in the graph state - the MC should be increased
        @return: The current version of this graph.
        """
        return self._mode_count

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        """
        Adds an edge to the graph.
        @param id1: The start node of the edge
        @param id2: The end node of the edge
        @param weight: The weight of the edge
        @return: True if the edge was added successfully, False o.w.

        Note: If the edge already exists or one of the nodes dose not exists the functions will do nothing
        :rtype: object
        """
        if id1 == id2 or weight < 0 or self._nodes.get(id1).has_neighbor(id2):
            return False
        elif self._nodes.__contains__(id1) and self._nodes.__contains__(id2):
            self._nodes.get(id1).connect_outgoing_edge(id2, weight)
            self._nodes.get(id2).connect_incoming_edge(id1, weight)
            self._edge_size += 1
            self._mode_count += 1
            return True

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        """
        Adds a node to the graph.
        Note: if the node id already exists the node will not be added

        @param node_id: The node ID
        @param pos: The position of the node
        @return: True if the node was added successfully, False o.w.
        """
        if self._nodes.__contains__(node_id):
            return False
        else:
            tmp_node = NodeData(node_id)
            self._nodes[node_id] = tmp_node
            self._mode_count += 1
            if pos is not None:
                self._nodes.get(node_id).set_position(pos)
            return True

    def remove_node(self, node_id: int) -> bool:
        """
        Removes a node from the graph.
        @param node_id: The node ID
        @return: True if the node was removed successfully, False o.w.

        Note: if the node id does not exists the function will do nothing
        """
        if self._nodes.__contains__(node_id):
            for k, v in self.all_in_edges_of_node(node_id).keys():
                self._nodes.get(node_id).remove_incoming_edge(k)
                v.remove_outgoing_edge(k)
                self._mode_count += 1
                self._edge_size -= 1
            self._nodes.pop(node_id)
            return True
        else:
            return False

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        """
        Removes an edge from the graph.
        @param node_id1: The start node of the edge
        @param node_id2: The end node of the edge
        @return: True if the edge was removed successfully, False o.w.

        Note: If such an edge does not exists the function will do nothing
        """
        if node_id1 != node_id2 and self._nodes.__contains__(node_id1) and self._nodes.__contains__(node_id1):
            self._nodes.get(node_id1).remove_outgoing_edge(node_id2)
            self._nodes.get(node_id2).remove_incoming_edge(node_id1)
            self._mode_count += 1
            self._edge_size -= 1
            return True
        else:
            return False
