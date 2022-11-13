from typing import List
from Node import Node
from Edge import Edge


class Graph:
    # graph name
    __name: str
    # graph nodes
    __nodes: List[Node]
    # graph edges
    __edges: List[Edge]
    # indicate whether the graph is directed or not
    __directed: bool

    def __init__(self, directed: bool = False, name: str = 'My Graph'):
        self.__name = name
        self.__nodes = []
        self.__edges = []
        self.__directed = directed

    def get_nodes(self) -> List[Node]:
        return self.__nodes

    def get_edges(self) -> List[Edge]:
        return self.__edges

    # obtain node by data
    def get_node(self, node_data: str) -> Node | None:
        for node in self.__nodes:
            if str(node) == node_data:
                return node
        return None

    # add a node to the graph by data
    def add_node(self, node_data: str):
        if self.get_node(node_data) is None:
            self.__nodes.append(Node(node_data))

    # delete a node from the graph, and all edges that are connected to it
    def remove_node(self, node_data: str):
        node = self.get_node(node_data)
        if node is None:
            return
        self.__nodes.remove(node)
        edges = self.__get_edges_by_node(node)
        for edge in edges:
            self.__edges.remove(edge)

    # obtain the edge that connects the two nodes
    def get_edge(self, node_from_data: str, node_to_data: str) -> Edge | None:
        node_from = self.get_node(node_from_data)
        if node_from is None:
            return None
        node_to = self.get_node(node_to_data)
        if node_to is None:
            return None
        return self.__get_edge_by_nodes(node_from, node_to)

    # add an edge to the graph by node data
    def add_edge(self, node_from_data: str, node_to_data: str):
        node_from = self.get_node(node_from_data)
        if node_from is None:
            return
        node_to = self.get_node(node_to_data)
        if node_to is None:
            return
        if self.__get_edge_by_nodes(node_from, node_to) is not None:
            return
        self.__edges.append(Edge(node_from, node_to))
        if not self.__directed:
            self.__edges.append(Edge(node_to, node_from))

    # remove an edge from the graph
    def remove_edge(self, node_from_data: str, node_to_data: str):
        edge = self.get_edge(node_from_data, node_to_data)
        if edge is None:
            return
        self.__edges.remove(edge)
        if not self.__directed:
            edge_inverted = self.get_edge(node_to_data, node_from_data)
            self.__edges.remove(edge_inverted)

    # obtain valency of the node
    def valency(self, node_data: str) -> int:
        node = self.get_node(node_data)
        if node is None:
            return -1
        valency = 0
        for edge in self.__edges:
            if edge.node_from == node:
                valency += 1
        return valency

    def adjacent(self, node_data: str) -> List[Node]:
        node = self.get_node(node_data)
        if node is None:
            return []
        adjacent_nodes: List[Node] = []
        for edge in self.__edges:
            if edge.node_from == node:
                adjacent_nodes.append(edge.node_to)
        return adjacent_nodes

    def __get_edge_by_nodes(self, node_from: Node, node_to: Node) -> Edge | None:
        for edge in self.__edges:
            if edge.node_from == node_from and edge.node_to == node_to:
                return edge
        return None

    # obtain all edges that are connected to the node
    def __get_edges_by_node(self, node: Node) -> List[Edge]:
        edges: List[Edge] = []
        for edge in self.__edges:
            if edge.node_from == node or edge.node_to == node:
                edges.append(edge)
        return edges

    def __str__(self) -> str:
        graph_str = f"{self.__name}:\n"
        graph_str += f"Nodes({len(self.__nodes)}): [ "
        for node in self.__nodes:
            graph_str += str(node) + ' '
        graph_str += str(']\n')
        graph_str += f"Edges({len(self.__edges)}): [ "
        for edge in self.__edges:
            graph_str += str(edge) + ' '
        graph_str += str(']')

        return graph_str
