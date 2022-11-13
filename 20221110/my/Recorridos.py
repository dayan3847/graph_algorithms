from Graph import Graph
from typing import List
from Node import Node
from ItemMatrix import ItemMatrix
from Color import Color


class Recorridos:
    graph: Graph

    def __init__(self, graph: Graph):
        self.graph = graph

    def recorrido_ancho_with_matrix(self, node_data: str) -> dict[str, ItemMatrix]:
        matrix = {}
        for node in self.graph.get_nodes():
            matrix[str(node)] = ItemMatrix(Color.BLACK, None, -1)
        node = self.graph.get_node(node_data)
        if node is None:
            return {}
        queue: List[Node] = [node]
        while len(queue) > 0:
            node = queue.pop(0)
            if matrix[str(node)].color == Color.BLACK:
                matrix[str(node)].color = Color.GRAY
                adjacent_nodes = self.graph.adjacent(str(node))
                for adjacent_node in adjacent_nodes:
                    queue.append(adjacent_node)
                    matrix[str(adjacent_node)].parent = node
                    matrix[str(adjacent_node)].distance = matrix[str(node)].distance + 1
                matrix[str(node)].color = Color.WHITE
        return matrix

    def recorrido_ancho_with_matrix_not_initialized(self, node_data: str) -> dict[str, ItemMatrix]:
        matrix = {}
        node = self.graph.get_node(node_data)
        if node is None:
            return {}
        queue: List[Node] = [node]
        while len(queue) > 0:
            node = queue.pop(0)
            if str(node) not in matrix or matrix[str(node)].color == Color.BLACK:
                matrix[str(node)].color = Color.GRAY
                adjacent_nodes = self.graph.adjacent(str(node))
                for adjacent_node in adjacent_nodes:
                    queue.append(adjacent_node)
                    matrix[str(adjacent_node)] = ItemMatrix(Color.BLACK, node, matrix[str(node)].distance + 1)
                matrix[str(node)].color = Color.WHITE
        return matrix
