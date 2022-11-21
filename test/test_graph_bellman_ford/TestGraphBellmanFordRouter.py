from src.Graph import Graph
from src.TestGraph import TestGraph

if __name__ == "__main__":
    # We initialize the graph.
    graph = Graph(True)

    # Add nodes to the graph.
    for i in ['a', 'b', 'c', 'd', 'e', 'f']:
        graph.add_node(i)

    # Add edges to the graph.
    graph.add_edge('a', 'b', 1)
    graph.add_edge('a', 'c', 2)
    graph.add_edge('a', 'd', 8)
    graph.add_edge('b', 'e', 3)
    graph.add_edge('c', 'd', 5)
    graph.add_edge('c', 'e', 3)
    graph.add_edge('c', 'f', 8)
    graph.add_edge('d', 'f', 12)
    graph.add_edge('e', 'f', 4)

    # We initialize the Test Graph.
    test_graph = TestGraph(graph)

    test_graph.test_bellman_ford('a')
