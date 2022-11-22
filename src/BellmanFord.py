from typing import List

from src.Graph import Graph
from src.Node import Node
from src.Edge import Edge
from src.ItemMatrixBellmanFord import ItemMatrixBellmanFord


class BellmanFord:
    graph: Graph

    def __init__(self, graph: Graph):
        self.graph = graph

    # bellman ford algorithm
    def bellman_ford(self, node_root_data: str) -> dict[str, ItemMatrixBellmanFord]:
        node_root = self.graph.get_node(node_root_data)
        if node_root is None:
            return {}
        matrix: dict[str, ItemMatrixBellmanFord] = {}
        nodes: List[Node] = self.graph.get_nodes()
        edges: List[Edge] = self.graph.get_edges()
        for node in nodes:
            matrix[str(node)] = ItemMatrixBellmanFord(None, float('inf'))
        matrix[str(node_root)].distance = 0
        node_length: int = len(nodes)
        for _ in range(1, node_length):
            updated: bool = False
            for edge in edges:
                if matrix[str(edge.node_to)].distance > matrix[str(edge.node_from)].distance + edge.weight:
                    matrix[str(edge.node_to)].distance = matrix[str(edge.node_from)].distance + edge.weight
                    matrix[str(edge.node_to)].predecessor = edge.node_from
                    updated = True
            if not updated:
                break
        # check for negative weight cycles
        for edge in edges:
            if matrix[str(edge.node_from)].distance + edge.weight < matrix[str(edge.node_to)].distance:
                return {}
        return matrix
