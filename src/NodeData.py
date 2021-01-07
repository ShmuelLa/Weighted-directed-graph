class NodeData:

    def __init__(self, id: int):
        """
        The main node_data constructor. Creates a new node with the received ID

        :param id: The ID to be set for the new node
        """
        self._key = id
        self._tag = -1.0
        self._info = ""

    def get_key(self):
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

    def get_tag(self):
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

    def get_info(self):
        """
        Returns the remark (meta data) associated with this node

        :return: Str representing this noe's data
        """
        return self._info
