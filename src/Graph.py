from typing import List, Tuple

from src.Node import Node


class Graph():

    def __init__(self):
        """ Initialize the graph.
        """

        self.nodes = {}

    def add_node(self, node: Node):
        """ Add a node to the graph.

        Args:
            node (Node): The node to be added.
        """

        self.nodes[node.name] = node

    def sort_nodes(self):
        """ Sort the nodes by their names.
        """

        self.nodes = dict(
            sorted(self.nodes.items(), key=lambda item: int(item[0])))

    def normalize_authority_and_hub(self):
        """ Normalize the authority and hub of each node.
        """

        total_authority = sum(node.authority for node in self.nodes.values())
        total_hub = sum(node.hub for node in self.nodes.values())

        for node in self.nodes.values():
            node.authority /= total_authority
            node.hub /= total_hub

    def get_authority_and_hub(self) -> Tuple[List[float], List[float]]:
        """ Get the authority and hub of each node.

        Returns:
            Tuple[List[float], List[float]]: The authority and hub of each node.
        """

        authorities = []
        hubs = []

        for node in self.nodes.values():
            authorities.append(round(number=node.authority, ndigits=3))
            hubs.append(round(number=node.hub, ndigits=3))

        return (authorities, hubs)

    def normalize_pagerank(self):
        """ Normalize the pagerank of each node.
        """

        total_pagerank = sum(node.pagerank for node in self.nodes.values())

        for node in self.nodes.values():
            node.pagerank /= total_pagerank

    def get_pagerank(self) -> List[float]:
        """ Get the pagerank of each node.

        Returns:
            List[float]: The pagerank of each node.
        """

        pageranks = []

        for node in self.nodes.values():
            pageranks.append(round(number=node.pagerank, ndigits=3))

        return pageranks
