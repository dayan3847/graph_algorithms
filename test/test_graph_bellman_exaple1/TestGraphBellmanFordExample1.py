from src.Graph import Graph
from src.TestGraph import TestGraph

if __name__ == "__main__":
    # We initialize the graph.
    graph = Graph(True)

    # Add nodes to the graph.
    for i in ['a', 'b', 'c', 'd', 'e']:
        graph.add_node(i)

    # Add edges to the graph.
    graph.add_edge('a', 'b', -1)
    graph.add_edge('a', 'c', 4)
    graph.add_edge('b', 'c', 3)
    graph.add_edge('b', 'd', 2)
    graph.add_edge('b', 'e', 2)
    graph.add_edge('d', 'b', 1)
    graph.add_edge('d', 'c', 5)
    graph.add_edge('e', 'd', -3)

    # We initialize the Test Graph.
    test_graph = TestGraph(graph)

    test_graph.test_bellman_ford('a')
