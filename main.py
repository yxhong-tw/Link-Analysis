from src.Similarity import Similarity
from src.hits import hits
from src.pagerank import pagerank
from src.simrank import simrank
from src.utils import initialize_graph, parse_args, save_results


def main():
    """ Main function
    """

    args = parse_args()

    graph = initialize_graph(data_name=args.data_name)
    graph.sort_nodes()

    # Do PageRank algorithm
    pagerank(graph=graph,
             damping_factor=args.damping_factor,
             iteration=args.iteration)

    # Do HITS algorithm
    hits(graph=graph, iteration=args.iteration)

    # Do SimRank algorithm
    similarity = None
    if args.data_name != "graph_6" and args.data_name != "ibm-5000":
        similarity = Similarity(graph=graph, decay_factor=args.decay_factor)
        simrank(graph=graph, similarity=similarity, iteration=args.iteration)

    save_results(graph=graph, data_name=args.data_name, similarity=similarity)


if __name__ == "__main__":
    main()
