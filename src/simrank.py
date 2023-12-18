from src.Graph import Graph
from src.Similarity import Similarity
from src.utils import timer


@timer
def simrank(graph: Graph, similarity: Similarity, iteration: int):
    """ Calculate the simrank of the graph.

    Args:
        graph (Graph): The graph of the data.
        similarity (Similarity): The similarity class.
        iteration (int): The number of iterations.
    """

    for _ in range(iteration):
        for node_1 in graph.nodes.values():
            for node_2 in graph.nodes.values():
                simrank = similarity.calculate_simrank(node_1=node_1,
                                                       node_2=node_2)
                similarity.update_similarity(node_1=node_1,
                                             node_2=node_2,
                                             simrank=simrank)
