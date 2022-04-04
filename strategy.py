from abc import ABC, abstractmethod
from chess_piece import ChessPiece

from position import Position


class Strategy(ABC):  # Strategy
    @abstractmethod
    def execute(self, position: Position, board_size, matrix):
        pass


class KingStrategy(Strategy):
    def execute(self, position: Position, board_size, matrix):
        attackedPositions = []

        return attackedPositions


class KnightStrategy(Strategy):
    def execute(self, position: Position, board_size, matrix):
        attackedPositions = []

        return attackedPositions


class QueenStrategy(Strategy):
    def execute(self, position: Position, board_size, matrix):
        attackedPositions = []
        x = position.getX()
        y = position.getY()
        curr_row = x
        curr_col = y
        while curr_row > 0 and curr_col > 0:
            curr_col -= 1
            curr_row -= 1
        # we have coordinate of the upper left of this diagonal
        diagonal_1_attacked = []
        while curr_col < board_size and curr_row < board_size:
            if curr_row < x and type(matrix[curr_row][curr_col]) == ChessPiece:
                diagonal_1_attacked = []
            if curr_row > x and type(matrix[curr_row][curr_col]) == ChessPiece:
                break
            if curr_row != x and curr_col != y:
                diagonal_1_attacked.append(Position(curr_row, curr_col))
            curr_col += 1
            curr_row += 1

        curr_row = x
        curr_col = y

        while curr_row > 0 and curr_col < board_size - 1:
            curr_row -= 1
            curr_col += 1
        # we have coordinate of the upper right of this diagonal
        diagonal_2_attacked = []
        while curr_col >= 0 and curr_row < board_size:
            if curr_row < x and type(matrix[curr_row][curr_col]) == ChessPiece:
                diagonal_2_attacked = []
            if curr_row > x and type(matrix[curr_row][curr_col]) == ChessPiece:
                break
            if curr_row != x and curr_col != y:
                diagonal_2_attacked.append(Position(curr_row, curr_col))

            curr_col -= 1
            curr_row += 1

        curr_col = y
        curr_row = x
        attackedPositions = diagonal_1_attacked + diagonal_2_attacked
        while curr_row > 0:
            curr_row -= 1
            if type(matrix[curr_row][y]) == ChessPiece:
                break
            attackedPositions.append(Position(curr_row, y))

        curr_row = x
        while curr_row < board_size - 1:
            curr_row += 1
            if type(matrix[curr_row][y]) == ChessPiece:
                break
            attackedPositions.append(Position(curr_row, y))

        curr_col = y
        while curr_col > 0:
            curr_col -= 1
            if type(matrix[x][curr_col]) == ChessPiece:
                break
            attackedPositions.append(Position(x, curr_col))

        curr_col = y
        while curr_col < board_size - 1:
            curr_col += 1
            if type(matrix[x][curr_col]) == ChessPiece:
                break
            attackedPositions.append(Position(x, curr_col))

        return attackedPositions
