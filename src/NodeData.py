class NodeData:

    def __init__(self, node_id: int):
        """
        The main node_data constructor. Creates a new node with the received ID

        :param id: The ID to be set for the new node
        """
        self._neighbors_out = {}
        self._neighbors_in = {}
        self._position = ()
        self._key = node_id
        self._tag = -1.0
        self._info = ""
        self.scc_index = -1
        self.on_scc_stack = False

    def has_outgoing_edge(self, node1: int, weight: float) -> bool:
        if self._neighbors_out.__contains__(node1):
            return self._neighbors_out.get(node1) == weight
        else:
            return False

    def has_incoming_edge(self, node1: int, weight: float) -> bool:
        if self._neighbors_in.__contains__(node1):
            return self._neighbors_in.get(node1) == weight
        else:
            return False

    def has_neighbor(self, node_id: int) -> bool:
        return self._neighbors_out.__contains__(node_id)

    def connect_incoming_edge(self, node_id: int, weight: float):
        self._neighbors_in[node_id] = weight

    def connect_outgoing_edge(self, node_id: int, weight: float):
        self._neighbors_out[node_id] = weight

    def remove_incoming_edge(self, node_id: int):
        if self._neighbors_in.__contains__(node_id):
            self._neighbors_in.pop(node_id)
            return True
        else:
            return False

    def remove_outgoing_edge(self, node_id: int):
        if self._neighbors_in.__contains__(node_id):
            self._neighbors_in.pop(node_id)
            return True
        else:
            return False

    def set_position(self, pos: tuple):
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

    def set_tag(self, tag: float):
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

    def set_info(self, info: str):
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

    def __str__(self):
        """
        turns the note to string in json format:
        example - {"pos":"0.9420675020620758,0.7598820416652761,0.0","id":7}

        :return:
        """
        if self._position == ():
            return "{\"id\":" + str(self._key) + "}"
        else:
            return "{\"pos\":\"" + str(self._position[0]) + "," + str(self._position[1]) + ","\
                   + str(self._position[2]) + "\"," + "\"id\":" + str(self._key) + "}"

    def __lt__(self, other):
        return self.get_tag() < other.get_tag()

    def __gt__(self, other):
        return self.get_tag() > other.get_tag()

    def __repr__(self):
        """
        Returns output, format example: "0: |edges out| 1 |edges in| 1"

        :return: String representation of the node
        """
        return str(self._key) + ": |edges out| " + \
               str(self._neighbors_out.__len__()) + " |edges in| " + str(self._neighbors_in.__len__())
