from Graph import Graph


class TestGraph:
    graph: Graph

    def __init__(self):
        self.graph = Graph()

        # Add nodes to the graph.
        for i in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']:
            self.graph.add_node(i)

        # Add edges to the graph.
        self.graph.add_edge('A', 'B')
        self.graph.add_edge('A', 'E')
        self.graph.add_edge('A', 'F')
        self.graph.add_edge('B', 'F')
        self.graph.add_edge('B', 'C')
        self.graph.add_edge('C', 'G')
        self.graph.add_edge('C', 'D')
        self.graph.add_edge('D', 'G')
        self.graph.add_edge('D', 'H')
        self.graph.add_edge('G', 'F')
        self.graph.add_edge('G', 'H')

    def print_valences(self):
        text = 'Valencies: '
        nodes = self.graph.get_nodes()
        for node in nodes:
            text += f"({str(node)} = {self.graph.valency(str(node))}) "
        print(text)


if __name__ == "__main__":
    # We initialize the graph.
    test_graph = TestGraph()
    # We print the graph.
    print(str(test_graph.graph))
    # We print the valencies of the nodes.
    test_graph.print_valences()
