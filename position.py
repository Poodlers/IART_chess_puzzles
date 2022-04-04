from __future__ import annotations


class Position:
    def __init__(self, X: int, Y: int):
        self.x = X
        self.y = Y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def setX(self, x: int):
        self.x = x

    def setY(self, y: int):
        self.y = y

    def __str__(self) -> str:
        return '({self.x}, {self.y})'.format(self=self)
