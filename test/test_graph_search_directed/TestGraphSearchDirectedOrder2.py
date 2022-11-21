from src.Graph import Graph
from src.TestGraph import TestGraph

if __name__ == "__main__":
    # We initialize the graph.
    graph = Graph(True)

    # Add nodes to the graph.
    for i in ['S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']:
        graph.add_node(i)

    # Add edges to the graph.
    graph.add_edge('S', 'Z')
    graph.add_edge('S', 'W')
    graph.add_edge('T', 'U')
    graph.add_edge('T', 'V')
    graph.add_edge('U', 'T')
    graph.add_edge('U', 'V')
    graph.add_edge('V', 'S')
    graph.add_edge('V', 'W')
    graph.add_edge('W', 'X')
    graph.add_edge('X', 'Z')
    graph.add_edge('Y', 'X')
    graph.add_edge('Z', 'Y')
    graph.add_edge('Z', 'W')

    # We initialize the Test Graph.
    test_graph = TestGraph(graph)
    # We print the graph with the valencies of each node.
    test_graph.print_graph()

    test_graph.test_depth_first_search_book()
