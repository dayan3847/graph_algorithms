from src.Graph import Graph
from src.GraphSearches import GraphSearches
from src.BellmanFord import BellmanFord
from src.ItemMatrix import ItemMatrix
from src.ItemMatrixBellmanFord import ItemMatrixBellmanFord


class TestGraph:
    graph: Graph

    def __init__(self, graph: Graph):
        self.graph = graph
        self.print_graph()

    def print_graph(self):
        print(str(self.graph))
        text = 'Valencies: '
        nodes = self.graph.get_nodes()
        for node in nodes:
            text += f"({str(node)} = {self.graph.valency(str(node))}) "
        print(text + '\n')

    def test_remove_node(self, node_data: str):
        print(f'Removing Node: ({node_data})')
        self.graph.remove_node(node_data)
        print()
        self.print_graph()

    def test_remove_edge(self, node_from_data: str, node_to_data: str):
        print(f'Removing Edge: ({node_from_data}->{node_to_data})')
        self.graph.remove_edge(node_from_data, node_to_data)
        print()
        self.print_graph()

    def test_breadth_first_search(self, node_data: str):
        print(f'Breadth First Search: ({node_data})')
        nodes = self.graph.breadth_first_search(node_data)
        text = f"Nodes({len(nodes)}): [ "
        for node in nodes:
            text += str(node) + ' '
        text += str(']\n')
        print(text)

    def test_breadth_first_search_book(self, node_data: str):
        graph_searches = GraphSearches(self.graph)
        print(f'Breadth First Search: ({node_data}) Book')
        matrix: dict[str, ItemMatrix] = graph_searches.breadth_first_search_book(node_data)
        for i in range(len(matrix)):
            print(f"{list(matrix.keys())[i]}: {str(list(matrix.values())[i])}")
        print()

    def test_breadth_first_search_book_not_initialized(self, node_data: str):
        graph_searches = GraphSearches(self.graph)
        print(f'Breadth First Search: ({node_data}) Book (not initialized)')
        matrix: dict[str, ItemMatrix] = graph_searches.breadth_first_search_book_not_initialized(node_data)
        for i in range(len(matrix)):
            print(f"{list(matrix.keys())[i]}: {str(list(matrix.values())[i])}")
        print()

    def test_depth_first_search(self, node_data: str):
        print(f'Depth First Search: ({node_data})')
        nodes = self.graph.depth_first_search(node_data)
        text = f"Nodes({len(nodes)}): [ "
        for node in nodes:
            text += str(node) + ' '
        text += str(']\n')
        print(text)

    def test_depth_first_search_book(self):
        print('Depth First Search: Book')
        graph_searches = GraphSearches(self.graph)
        print('')
        matrix: dict[str, ItemMatrix] = graph_searches.depth_first_search_book()
        for i in range(len(matrix)):
            print(f"{list(matrix.keys())[i]}: {str(list(matrix.values())[i])}")
        print()

    def test_bellman_ford(self, node_data: str):
        print(f'Bellman Ford: ({node_data})')
        bellman_ford = BellmanFord(self.graph)
        matrix: dict[str, ItemMatrixBellmanFord] = bellman_ford.bellman_ford(node_data)
        for i in range(len(matrix)):
            print(f"{list(matrix.keys())[i]}: {str(list(matrix.values())[i])}")
        print()
