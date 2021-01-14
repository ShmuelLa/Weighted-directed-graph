class NodeData:
    """
    This class represents a vertex on a connected weighted graph.
    after initialization this objects hold all the information about any node
    including ingoing and outgoing edges, algorithmic tagging data and more.
    """

    def __init__(self, node_id: int):
        """
        The main node_data constructor. Creates a new node with the received ID

        :param node_id: The ID to be set for the new node
        """
        self._neighbors_out = {}
        self._neighbors_in = {}
        self._position = ()
        self._key = node_id
        self._tag = -1.0
        self._info = ""
        self.on_scc_stack = False

    def has_outgoing_edge(self, node1: int, weight: float) -> bool:
        """
        Checks if the node has an outgoing edge with a specific weight

        :param node1: the node to be checked
        :param weight: the weight of the edge
        :return: True if exists False otherwise
        """
        if self._neighbors_out.__contains__(node1):
            return self._neighbors_out.get(node1) == weight
        else:
            return False

    def has_incoming_edge(self, node1: int, weight: float) -> bool:
        """
        Checks if the node has an incoming edge with a specific weight

        :param node1: the node to be checked
        :param weight: the weight of the edge
        :return: True if exists False otherwise
        """
        if self._neighbors_in.__contains__(node1):
            return self._neighbors_in.get(node1) == weight
        else:
            return False

    def has_neighbor(self, node_id: int) -> bool:
        """
        Checks if the node has a specific neighbor connected out ->

        :param node_id: the node to be checked
        :return: True if the node is connected False otherwise
        """
        return self._neighbors_out.__contains__(node_id)

    def connect_incoming_edge(self, node_id: int, weight: float) -> None:
        """
        Connects an incoming edge to the node

        :param node_id: node to be connected from
        :param weight: edge weight
        """
        self._neighbors_in[node_id] = weight

    def connect_outgoing_edge(self, node_id: int, weight: float) -> None:
        """
        Connects an outgoing edge to the node

        :param node_id: node to be connected to
        :param weight: edge weight
        """
        self._neighbors_out[node_id] = weight

    def remove_incoming_edge(self, node_id: int) -> bool:
        """
        Removes an incoming edge from the node

        :param node_id: node to be removed
        :return: True if successful False otherwise
        """
        if self._neighbors_in.__contains__(node_id):
            self._neighbors_in.pop(node_id)
            return True
        else:
            return False

    def remove_outgoing_edge(self, node_id: int) -> bool:
        """
        Removes and outgoing edge from the node

        :param node_id: the node to remove
        :return: True is successful False otherwise
        """
        if self._neighbors_in.__contains__(node_id):
            self._neighbors_in.pop(node_id)
            return True
        else:
            return False

    def set_position(self, pos: tuple) -> None:
        """
        Sets the current Node's 3D position, will be inserted in a (x, y, z) tuple

        :param pos: tuple of the position in (x, y, z) format
        """
        self._position = pos

    def get_position(self) -> tuple:
        """
        Returns this nodes position value's

        :return: (x,y,x) tuple
        """
        return self._position

    def get_outgoing_neighbors(self) -> dict:
        """
        Returns a dictionary representing all the nodes outgoing from this node,
        each node is represented using a pair (other_node_id, weight)

        :return: dict of neighboring nodes {other_node_id, weight}
        """
        return self._neighbors_out

    def get_incoming_neighbors(self) -> dict:
        """
        Returns a dictionary representing all the nodes incoming from this node,
        each node is represented using a pair (other_node_id, weight)

        :return: dict of neighboring nodes {other_node_id, weight}
        """
        return self._neighbors_in

    def get_key(self) -> int:
        """
        Returns this node's key

        :return: int representing the nodes key
        """
        return self._key

    def set_tag(self, tag: float) -> None:
        """
        Sets the tag (coloring) of this node, this function is used for algorithms

        :param tag: float representing the nodes new tag
        """
        self._tag = tag

    def get_tag(self) -> float:
        """
        Returns the tag (coloring) associated with this node

        :return: float representing this node's tag
        """
        return self._tag

    def set_info(self, info: str) -> None:
        """
        Sets the remark (meta data) associated with this node

        :param info: str representing the new info
        """
        self._info = info

    def get_info(self) -> str:
        """
        Returns the remark (meta data) associated with this node

        :return: Str representing this noe's data
        """
        return self._info

    def __str__(self) -> str:
        """
        turns the note to string in json format:
        example - {"pos":"0.9420675020620758,0.7598820416652761,0.0","id":7}

        :return:
        """
        if self._position == ():
            return "{\"id\":" + str(self._key) + "}"
        else:
            return "{\"pos\":\"" + str(self._position[0]) + "," + str(self._position[1]) + "," \
                   + str(self._position[2]) + "\"," + "\"id\":" + str(self._key) + "}"

    def __lt__(self, other) -> bool:
        """
        comparator implementation used for comparing graph tag, used mainly in Dijkstra's algorithm

        :param other: other node to compare with
        :return: the node with smaller tag
        """
        return self.get_tag() < other.get_tag()

    def __gt__(self, other) -> bool:
        """
        comparator implementation used for comparing graph tag, used mainly in Dijkstra's algorithm

        :param other: other node to compare with
        :return: the node with bigger tag
        """
        return self.get_tag() > other.get_tag()

    def __repr__(self) -> str:
        """
        Returns output, format example: "0: |edges out| 1 |edges in| 1"

        :return: String representation of the node
        """
        return str(self._key) + ": |edges out| " + \
            str(self._neighbors_out.__len__()) + " |edges in| " + str(self._neighbors_in.__len__())
