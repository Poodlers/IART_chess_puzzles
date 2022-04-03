from __future__ import annotations
from abc import ABC, abstractmethod
from tokenize import Number
from typing import List

class Position:
    def __init__(self, X: int, Y: int):
        self.X = X
        self.Y = Y

class Board:
    def __init__(self, size: int):
        self.size = size
        self.matrix= list(size * [size * [0]])

class Strategy(ABC): # Strategy
    @abstractmethod
    def execute(self, board: Board):
        pass

class KingStrategy(Strategy):
    def execute(self, board):
        if type(board.matrix[self.position.X][self.position.Y]) != int:
            raise Exception("Position already occupied by another chess piece")

        thislist = []
        for i in range (board.size):
            intlist = []
            for j in range (board.size):
                if (i == self.position.X and j == self.position.Y):
                    intlist.append('K')
                else:
                    intlist.append(0)
            thislist.append(intlist)
            intlist = []
        board.matrix = thislist

class ChessPiece: #Context
    def __init__(self, position: Position, move_strategy: Strategy) -> None:
        self.move_strategy = move_strategy
        self.position = position
    
    @property
    def getMoveStrategy(self) -> Strategy:
        return self.move_strategy

    def setMoveStrategy(self, move_strategy: Strategy) -> None:
        self.move_strategy = move_strategy

    def implementStrategy(self, board: Board) -> None:
        self.move_strategy.execute(self, board)


def main():
    board = Board(7)

    king = ChessPiece(Position(6, 6), KingStrategy)
    print(board.matrix)
    king.implementStrategy(board)
    king.implementStrategy(board)
    print(board.matrix)

main()
