from Graph import Graph
from GraphSearches import GraphSearches
from ItemMatrix import ItemMatrix


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

    def print_graph(self):
        print(str(test_graph.graph))
        text = 'Valencies: '
        nodes = self.graph.get_nodes()
        for node in nodes:
            text += f"({str(node)} = {self.graph.valency(str(node))}) "
        print(text + '\n')

    def test_remove_node(self):
        print('Removing Node: (D)')
        self.graph.remove_node('D')
        print()

    def test_remove_edge(self):
        print('Removing Edge: (A->F)')
        self.graph.remove_edge('A', 'F')
        print()

    def test_breadth_first_search(self):
        graph_searches = GraphSearches(self.graph)
        print('Breadth First Search: (A)')
        matrix: dict[str, ItemMatrix] = graph_searches.breadth_first_search_book('A')
        for i in range(len(matrix)):
            print(f"{list(matrix.keys())[i]}: {str(list(matrix.values())[i])}")
        print()

    def test_breadth_first_search_not_initialized(self):
        graph_searches = GraphSearches(self.graph)
        print('Breadth First Search: (A) (not initialized)')
        matrix: dict[str, ItemMatrix] = graph_searches.breadth_first_search_book_not_initialized('A')
        for i in range(len(matrix)):
            print(f"{list(matrix.keys())[i]}: {str(list(matrix.values())[i])}")
        print()


if __name__ == "__main__":
    # We initialize the graph.
    test_graph = TestGraph()
    # We print the graph with the valencies of each node.
    test_graph.print_graph()
    # test_graph.test_remove_edge()
    # test_graph.print_graph()
    # test_graph.test_remove_node()
    # test_graph.print_graph()
    test_graph.test_breadth_first_search()
    test_graph.test_breadth_first_search_not_initialized()
