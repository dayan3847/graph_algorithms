from src.Graph import Graph
from src.TestGraph import TestGraph

if __name__ == "__main__":
    # We initialize the graph.
    graph = Graph(True)

    # Add nodes to the graph.
    for i in [
        'saco',
        'corbata',
        'cinturon',
        'camisa',
        'reloj',
        'zapatos',
        'pantalones',
        'calzones',
        'calcetin',
    ]:
        graph.add_node(i)

    # Add edges to the graph.
    graph.add_edge('calzones', 'zapatos')
    # TODO complete the graph.

    # We initialize the Test Graph.
    test_graph = TestGraph(graph)
    # We print the graph with the valencies of each node.
    test_graph.print_graph()

    test_graph.test_depth_first_search_book()
