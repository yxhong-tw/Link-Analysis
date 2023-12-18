from typing import List

from src.Graph import Graph
from src.Node import Node


class Similarity():
    """ The similarity class.
    """

    def __init__(self, graph: Graph, decay_factor: float):
        """ Initialize the similarity class.

        Args:
            graph (Graph): The graph of the data.
            decay_factor (float): The decay factor.
        """

        self.decay_factor = decay_factor
        self.similarity = self.initialize_similarity(graph)

    def initialize_similarity(self, graph: Graph) -> List[List[float]]:
        """ Initialize the similarity matrix.

        Args:
            graph (Graph): The graph of the data.

        Returns:
            List[List[float]]: The similarity matrix.
        """

        similarity = []

        for node_1 in graph.nodes.values():
            one_row_similarity = []

            for node_2 in graph.nodes.values():
                if node_1 == node_2:
                    one_row_similarity.append(1.0)
                else:
                    one_row_similarity.append(0.0)

            similarity.append(one_row_similarity)

        return similarity

    def calculate_simrank(self, node_1: Node, node_2: Node) -> float:
        """ Calculate the simrank of the two nodes.

        Args:
            node_1 (Node): The first node.
            node_2 (Node): The second node.

        Returns:
            float: The simrank of the two nodes.
        """

        if node_1 == node_2:
            return 1.0

        if len(node_1.parents) == 0 or len(node_2.parents) == 0:
            return 0.0

        total_simrank = 0.0
        for parent_1 in node_1.parents:
            for parent_2 in node_2.parents:
                total_simrank += self.get_similarity(node_1=parent_1,
                                                     node_2=parent_2)

        return self.decay_factor * total_simrank / (len(node_1.parents) *
                                                    len(node_2.parents))

    def get_similarity(self, node_1: Node, node_2: Node) -> float:
        """ Get the similarity of the two nodes.

        Args:
            node_1 (Node): The first node.
            node_2 (Node): The second node.

        Returns:
            float: The similarity of the two nodes.
        """

        return self.similarity[int(node_1.name) - 1][int(node_2.name) - 1]

    def update_similarity(self, node_1: Node, node_2: Node, simrank: float):
        """ Update the similarity of the two nodes.

        Args:
            node_1 (Node): The first node.
            node_2 (Node): The second node.
            simrank (float): The simrank of the two nodes.
        """

        self.similarity[int(node_1.name) - 1][int(node_2.name) - 1] = round(
            number=simrank, ndigits=3)
