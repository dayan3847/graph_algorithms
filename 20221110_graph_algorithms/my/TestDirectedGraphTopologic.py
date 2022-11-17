from Graph import Graph
from GraphSearches import GraphSearches
from ItemMatrix import ItemMatrix


class TestGraph:
    graph: Graph

    def __init__(self):
        self.graph = Graph(True)

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
            self.graph.add_node(i)

        # Add edges to the graph.
        self.graph.add_edge('S', 'Z')

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
        print('Breadth First Search: (A)')
        nodes = self.graph.breadth_first_search('A')
        text = f"Nodes({len(nodes)}): [ "
        for node in nodes:
            text += str(node) + ' '
        text += str(']\n')
        print(text)

    def test_breadth_first_search_book(self):
        graph_searches = GraphSearches(self.graph)
        print('Breadth First Search: (A) Book')
        matrix: dict[str, ItemMatrix] = graph_searches.breadth_first_search_book('A')
        for i in range(len(matrix)):
            print(f"{list(matrix.keys())[i]}: {str(list(matrix.values())[i])}")
        print()

    def test_breadth_first_search_book_not_initialized(self):
        graph_searches = GraphSearches(self.graph)
        print('Breadth First Search: (A) Book (not initialized)')
        matrix: dict[str, ItemMatrix] = graph_searches.breadth_first_search_book_not_initialized('A')
        for i in range(len(matrix)):
            print(f"{list(matrix.keys())[i]}: {str(list(matrix.values())[i])}")
        print()

    def test_depth_first_search(self):
        print('Depth First Search:')
        nodes = self.graph.depth_first_search('A')
        text = f"Nodes({len(nodes)}): [ "
        for node in nodes:
            text += str(node) + ' '
        text += str(']\n')
        print(text)

    def test_depth_first_search_book(self):
        print('Depth First Search: (A) Book')
        graph_searches = GraphSearches(self.graph)
        print('')
        matrix: dict[str, ItemMatrix] = graph_searches.depth_first_search_book()
        for i in range(len(matrix)):
            print(f"{list(matrix.keys())[i]}: {str(list(matrix.values())[i])}")
        print()

    def test_depth_first_search_book_edge(self):
        print('Depth First Search: (A) Book Edge')
        graph_searches = GraphSearches(self.graph)
        print('')
        matrix_edge: dict[str, str] = graph_searches.depth_first_search_book_edges()
        for i in range(len(matrix_edge)):
            print(f"{list(matrix_edge.keys())[i]}: {str(list(matrix_edge.values())[i])}")
        print()


if __name__ == "__main__":
    # We initialize the graph.
    test_graph = TestGraph()
    # We print the graph with the valencies of each node.
    test_graph.print_graph()
    test_graph.test_breadth_first_search()
    test_graph.test_breadth_first_search_book()
    test_graph.test_breadth_first_search_book_not_initialized()
    test_graph.test_depth_first_search()
    test_graph.test_depth_first_search_book()
    test_graph.test_depth_first_search_book_edge()

    # test_graph.print_graph()
    # test_graph.test_remove_edge()
    # test_graph.print_graph()
    # test_graph.test_remove_node()
    # test_graph.print_graph()
