class Node():
    """ The node class.
    """

    def __init__(self, name: str):
        """ Initialize the node class.

        Args:
            name (str): The name of the node.
        """

        self.name = name
        self.parents = []
        self.children = []
        self.authority = 1.0
        self.hub = 1.0
        self.pagerank = 1.0

    def add_parent(self, parent: "Node"):
        """ Add a parent node.

        Args:
            parent (Node): The parent node.
        """

        self.parents.append(parent)

    def add_child(self, child: "Node"):
        """ Add a child node.

        Args:
            child (Node): The child node.
        """

        self.children.append(child)

    def update_authority(self):
        """ Update the authority of the node.
        """

        self.authority = sum(node.hub for node in self.parents)

    def update_hub(self):
        """ Update the hub of the node.
        """

        self.hub = sum(node.authority for node in self.children)

    def update_pagerank(self, damping_factor: float, nodes_number: int):
        """ Update the pagerank of the node.

        Args:
            damping_factor (float): The damping factor.
            nodes_number (int): The number of nodes.
        """

        self.pagerank = damping_factor / nodes_number + \
            (1 - damping_factor) * sum(node.pagerank / len(node.children)
                                 for node in self.parents)
