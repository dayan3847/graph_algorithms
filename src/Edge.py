from src.Node import Node


class Edge:
    node_from: Node
    node_to: Node
    weight: int

    def __init__(self, node_from: Node, node_to: Node, weight: int = 1):
        self.node_from = node_from
        self.node_to = node_to
        self.weight = weight

    def __str__(self) -> str:
        return f"({self.node_from}->{self.node_to})"
