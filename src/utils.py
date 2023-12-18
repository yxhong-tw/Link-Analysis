import argparse
import os
import time

import numpy as np

from src.Graph import Graph
from src.Node import Node
from src.Similarity import Similarity


def timer(func):
    """ Decorator to calculate the time of the function.

    Args:
        func (_type_): The wrapped function.
    """

    def wrapper(*args, **kwargs):
        start = time.time()
        print(f"Running {func.__name__} ...", end='\r')

        result = func(*args, **kwargs)

        end = time.time()
        print(f"{func.__name__} Done in {end - start:.5f} seconds")

        return result

    return wrapper


def parse_args() -> argparse.Namespace:
    """ Parse the arguments.

    Returns:
        argparse.Namespace: The arguments.
    """

    parser = argparse.ArgumentParser()

    parser.add_argument("-dn",
                        "--data_name",
                        type=str,
                        required=True,
                        help="Name of data")
    parser.add_argument("-daf",
                        "--damping_factor",
                        type=float,
                        default=0.1,
                        help="Damping factor")
    parser.add_argument("-def",
                        "--decay_factor",
                        type=float,
                        default=0.7,
                        help="Decay factor")
    parser.add_argument("-i",
                        "--iteration",
                        type=int,
                        default=30,
                        help="Iteration")

    return parser.parse_args()


def initialize_graph(data_name: str) -> Graph:
    """ Initialize the graph.

    Args:
        data_name (str): The name of the data.

    Returns:
        Graph: The graph of the data.
    """

    graph = Graph()

    file_path = (os.path.join("data", data_name) + ".txt")
    with open(file=file_path, mode="r") as f:
        lines = f.readlines()

        for line in lines:

            if "ibm" in data_name:
                items = line.strip().split()
                items = items[1:]
            else:
                items = line.strip().split(",")

            if items[0] not in graph.nodes.keys():
                node = Node(name=items[0])
                graph.add_node(node=node)

            if items[1] not in graph.nodes.keys():
                node = Node(name=items[1])
                node.add_parent(parent=graph.nodes[items[0]])
                graph.add_node(node=node)
            else:
                graph.nodes[items[1]].add_parent(parent=graph.nodes[items[0]])

            graph.nodes[items[0]].add_child(child=graph.nodes[items[1]])

    return graph


def save_results(graph: Graph, similarity: Similarity, data_name: str):
    """ Save the results.

    Args:
        graph (Graph): The graph of the data.
        similarity (Similarity): The similarity class.
        data_name (str): The name of the data.
    """

    if not os.path.exists(path=f"results/{data_name}"):
        os.makedirs(name=f"results/{data_name}", exist_ok=True)

    # Save HITS results
    authorities, hubs = graph.get_authority_and_hub()
    print(f"Authority: {authorities}")
    print(f"Hub: {hubs}")

    file_path = (
        os.path.join("results", data_name, f"{data_name}_HITS_authority") +
        ".txt")
    np.savetxt(fname=file_path, X=authorities, fmt=f"%.3f", newline=" ")

    file_path = (os.path.join("results", data_name, f"{data_name}_HITS_hub") +
                 ".txt")
    np.savetxt(fname=file_path, X=hubs, fmt=f"%.3f", newline=" ")

    # Save PageRank results
    pageranks = graph.get_pagerank()
    print(f"PageRank: {pageranks}")

    file_path = (
        os.path.join("results", data_name, f"{data_name}_PageRank") +
        ".txt")
    np.savetxt(fname=file_path, X=pageranks, fmt=f"%.3f", newline=" ")

    # Save SimRank results
    if similarity != None:
        similarities = similarity.similarity
        print(f"SimRank: {similarities}")

        file_path = (
            os.path.join("results", data_name, f"{data_name}_SimRank") +
            ".txt")
        np.savetxt(fname=file_path, X=similarities, fmt=f"%.3f")
