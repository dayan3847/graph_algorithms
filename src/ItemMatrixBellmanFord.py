from src.Node import Node


class ItemMatrixBellmanFord:
    distance: float
    predecessor: Node | None

    def __init__(self, predecessor: Node | None, distance: float):
        self.distance = distance
        self.predecessor = predecessor

    def __str__(self) -> str:
        return f'(Distance: {self.distance}, Predecessor: {self.predecessor})'
