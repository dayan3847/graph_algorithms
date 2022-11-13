from Graph import Graph


def initialize_graph() -> Graph:
    # We instantiate an object of class graph.
    graph = Graph()

    # We add nodes to the graph.
    for i in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']:
        graph.add_node_by_data(i)

    # We add edges to the graph.
    graph.add_edge_by_data('A', 'B')
    graph.add_edge_by_data('A', 'B')
    graph.add_edge_by_data('A', 'E')
    graph.add_edge_by_data('A', 'F')
    graph.add_edge_by_data('B', 'F')
    graph.add_edge_by_data('B', 'C')
    graph.add_edge_by_data('C', 'G')
    graph.add_edge_by_data('C', 'D')
    graph.add_edge_by_data('D', 'G')
    graph.add_edge_by_data('D', 'H')
    graph.add_edge_by_data('G', 'F')
    graph.add_edge_by_data('G', 'H')

    return graph


def print_valences(graph: Graph):
    for node in graph.get_nodes():
        print(f"The valency of node: {str(node)} is {graph.valency(node)}")


if __name__ == "__main__":
    # We initialize the graph.
    my_graph = initialize_graph()
    # We print the valencies of the nodes.
    print_valences(my_graph)
