from src.Graph import Graph
from src.TestGraph import TestGraph

if __name__ == "__main__":
    # We initialize the graph.
    graph = Graph(True)

    # Add nodes to the graph.
    for i in ['a', 'b', 'c', 'd', 'e', 'f', 'g']:
        graph.add_node(i)

    # Add edges to the graph.
    graph.add_edge('f', 'g', 1)
    graph.add_edge('e', 'f', 1)
    graph.add_edge('d', 'e', 1)
    graph.add_edge('c', 'd', 1)
    graph.add_edge('b', 'c', 1)
    graph.add_edge('a', 'b', 1)

    # We initialize the Test Graph.
    test_graph = TestGraph(graph)

    test_graph.test_bellman_ford('a')
