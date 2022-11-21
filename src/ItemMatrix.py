from src.Color import Color
from src.Node import Node


class ItemMatrix:
    color: Color
    parent: Node | None
    d: int
    f: int

    def __init__(self, color: Color, parent: Node | None, d: int = -1, f: int = -1):
        self.color = color
        self.parent = parent
        self.d = d
        self.f = f

    def __str__(self) -> str:
        result = f"({self.color}, Parent: {self.parent}, d: {self.d}"
        if self.f != -1:
            result += f", f: {self.f}"
        result += ')'
        return result
