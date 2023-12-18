from src.Graph import Graph
from src.utils import timer


@timer
def pagerank(graph: Graph, damping_factor: float, iteration: int):
    """ Calculate the pagerank of the graph.

    Args:
        graph (Graph): The graph of the data.
        damping_factor (float): The damping factor.
        iteration (int): The number of iterations.
    """

    for _ in range(iteration):
        for node in graph.nodes.values():
            node.update_pagerank(damping_factor=damping_factor,
                                 nodes_number=len(graph.nodes))

        graph.normalize_pagerank()
