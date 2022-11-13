from Graph import Graph
from typing import List
from Node import Node
from ItemMatrix import ItemMatrix
from Color import Color


class GraphSearches:
    graph: Graph
    time: int

    def __init__(self, graph: Graph):
        self.graph = graph

    # Breadth-first search
    def breadth_first_search_book(self, node_root_data: str) -> dict[str, ItemMatrix]:
        node_root = self.graph.get_node(node_root_data)
        if node_root is None:
            return {}
        matrix = {}
        for node in self.graph.get_nodes():
            matrix[str(node)] = ItemMatrix(Color.WHITE, None, -1)
        matrix[str(node_root)] = ItemMatrix(Color.GRAY, None, 0)
        queue: List[Node] = [node_root]
        while len(queue) > 0:
            node = queue.pop(0)
            adjacent_nodes = self.graph.adjacent(str(node))
            for adjacent_node in adjacent_nodes:
                if matrix[str(adjacent_node)].color == Color.WHITE:
                    matrix[str(adjacent_node)].color = Color.GRAY
                    matrix[str(adjacent_node)].parent = node
                    matrix[str(adjacent_node)].d = matrix[str(node)].d + 1
                    queue.append(adjacent_node)
            matrix[str(node)].color = Color.BLACK
        return matrix

    def breadth_first_search_book_not_initialized(self, node_root_data: str) -> dict[str, ItemMatrix]:
        node_root = self.graph.get_node(node_root_data)
        if node_root is None:
            return {}
        matrix = {str(node_root): ItemMatrix(Color.GRAY, None, 0)}
        queue: List[Node] = [node_root]
        while len(queue) > 0:
            node = queue.pop(0)
            adjacent_nodes = self.graph.adjacent(str(node))
            for adjacent_node in adjacent_nodes:
                if str(adjacent_node) not in matrix:
                    matrix[str(adjacent_node)] = ItemMatrix(Color.GRAY, node, matrix[str(node)].d + 1)
                    queue.append(adjacent_node)
            matrix[str(node)].color = Color.BLACK
        return matrix

    # Depth-first search
    def depth_first_search_book(self) -> dict[str, ItemMatrix]:
        matrix = {}
        for node in self.graph.get_nodes():
            matrix[str(node)] = ItemMatrix(Color.WHITE, None)
        self.time = 0
        for node in self.graph.get_nodes():
            if matrix[str(node)].color == Color.WHITE:
                self.__depth_first_search_visit_book(node, matrix)
        return matrix

    def __depth_first_search_visit_book(self, node: Node, matrix: dict[str, ItemMatrix]):
        self.time += 1
        matrix[str(node)].d = self.time
        matrix[str(node)].color = Color.GRAY
        adjacent_nodes = self.graph.adjacent(str(node))
        for adjacent_node in adjacent_nodes:
            if matrix[str(adjacent_node)].color == Color.WHITE:
                matrix[str(adjacent_node)].parent = node
                self.__depth_first_search_visit_book(adjacent_node, matrix)
        matrix[str(node)].color = Color.BLACK
        self.time += 1
        matrix[str(node)].f = self.time
