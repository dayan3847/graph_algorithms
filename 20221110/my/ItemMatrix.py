from Color import Color
from Node import Node


class ItemMatrix:
    color: Color
    parent: Node | None
    distance: int

    def __init__(self, color: Color, parent: Node | None, distance: int):
        self.color = color
        self.parent = parent
        self.distance = distance
