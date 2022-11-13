from typing import List
from Node import Node
from Edge import Edge


class Graph:
    # graph nodes
    __nodes: List[Node]
    # graph edges
    __edges: List[Edge]
    # indicate whether the graph is directed or not
    __directed: bool

    def __init__(self, directed: bool = False):
        self.__nodes = []
        self.__edges = []
        self.__directed = directed

    # add a node to the graph by data
    def add_node_by_data(self, data: str):
        if self.get_node_by_data(data) is None:
            self.__nodes.append(Node(data))

    # add a node to the graph
    def add_node(self, node: Node):
        if node not in self.__nodes:
            self.__nodes.append(node)

    # add an edge to the graph
    def add_edge(self, node_from: Node, node_to: Node):
        if node_from not in self.__nodes or node_to not in self.__nodes:
            return
        if self.get_edge(node_from, node_to) is not None:
            return
        self.__edges.append(Edge(node_from, node_to))
        if not self.__directed:
            self.__edges.append(Edge(node_to, node_from))

    # add an edge to the graph by node data
    def add_edge_by_data(self, data_from: str, data_to: str):
        node_from = self.get_node_by_data(data_from)
        if node_from is None:
            return
        node_to = self.get_node_by_data(data_to)
        if node_to is None:
            return
        self.add_edge(node_from, node_to)

    # delete a node from the graph, and all edges that are connected to it
    def remove_node(self, node: Node):
        if node not in self.__nodes:
            return
        self.__nodes.remove(node)
        edges = self.get_edges_by_node(node)
        for edge in edges:
            self.__edges.remove(edge)

    # remove an edge from the graph
    def remove_edge(self, node_from: Node, node_to: Node):
        edge = self.get_edge(node_from, node_to)
        if edge is None:
            return
        self.__edges.remove(edge)
        if not self.__directed:
            edge_inverted = self.get_edge(node_to, node_from)
            self.__edges.remove(edge_inverted)

    # obtain node by data
    def get_node_by_data(self, data: str) -> Node | None:
        for node in self.__nodes:
            if str(node) == data:
                return node
        return None

    # obtain the edge that connects the two nodes
    def get_edge(self, node_from: Node, node_to: Node) -> Edge | None:
        for edge in self.__edges:
            if edge.node_from == node_from and edge.node_to == node_to:
                return edge
            return None

    # obtain all edges that are connected to the node
    def get_edges_by_node(self, node: Node) -> List[Edge]:
        edges: List[Edge] = []
        for edge in self.__edges:
            if edge.node_from == node or edge.node_to == node:
                edges.append(edge)
        return edges

    # obtain valency of the node
    def valency(self, node: Node) -> int:
        valency = 0
        for edge in self.__edges:
            if edge.node_from == node:
                valency += 1
        return valency

    def adjacent(self, node: Node) -> List[Node]:
        if node not in self.__nodes:
            return []
        adjacent_nodes: List[Node] = []
        for edge in self.__edges:
            if edge.node_from == node:
                adjacent_nodes.append(edge.node_to)
        return adjacent_nodes

    def get_nodes(self) -> List[Node]:
        return self.__nodes

    def get_edges(self) -> List[Edge]:
        return self.__edges
