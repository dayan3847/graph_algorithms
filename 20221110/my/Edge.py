from Node import Node


class Edge:
    node_from: Node
    node_to: Node

    def __init__(self, node_from: Node, node_to: Node):
        self.node_from = node_from
        self.node_to = node_to
