from src.Graph import Graph
from src.TestGraph import TestGraph

if __name__ == "__main__":
    # We initialize the graph.
    graph = Graph()

    # Add nodes to the graph.
    for i in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']:
        graph.add_node(i)

    # Add edges to the graph.
    graph.add_edge('A', 'B')
    graph.add_edge('A', 'E')
    graph.add_edge('A', 'F')
    graph.add_edge('B', 'F')
    graph.add_edge('B', 'C')
    graph.add_edge('C', 'G')
    graph.add_edge('C', 'D')
    graph.add_edge('D', 'G')
    graph.add_edge('D', 'H')
    graph.add_edge('G', 'F')
    graph.add_edge('G', 'H')

    # We initialize the Test Graph.
    test_graph = TestGraph(graph)

    test_graph.test_breadth_first_search('A')
    test_graph.test_breadth_first_search_book('A')
    test_graph.test_breadth_first_search_book_not_initialized('A')

    test_graph.test_depth_first_search('A')
    test_graph.test_depth_first_search_book()
