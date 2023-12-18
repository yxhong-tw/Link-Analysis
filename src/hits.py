from src.Graph import Graph
from src.utils import timer


@timer
def hits(graph: Graph, iteration: int):
    """ Calculate the authority and hub of the graph.

    Args:
        graph (Graph): The graph of the data.
        iteration (int): The number of iterations.
    """

    for _ in range(iteration):
        for node in graph.nodes.values():
            node.update_authority()

        for node in graph.nodes.values():
            node.update_hub()

        graph.normalize_authority_and_hub()
