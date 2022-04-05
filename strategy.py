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
        x = position.getX()
        y = position.getY()

        for i in range(x - 1, x + 2):
            if i < 0 or i >= board_size:
                continue
            for j in range(y - 1, y + 2):
                if j < 0 or j >= board_size:
                    continue
                elif type(matrix[i][j]) != ChessPiece:
                    attackedPositions.append(Position(i, j))

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


class RookStrategy(Strategy):
    def execute(self, position: Position, board_size, matrix):
        attackedPositions = []
        x = position.getX()
        y = position.getY()

        for j in range(y + 1, board_size):
            if type(matrix[x][j]) == ChessPiece:
                break
            attackedPositions.append(Position(x, j))
        for j in range(y - 1, -1, -1):
            if type(matrix[x][j]) == ChessPiece:
                break
            attackedPositions.append(Position(x, j))

        for i in range(x - 1, -1, -1):
            if type(matrix[i][y]) == ChessPiece:
                break
            attackedPositions.append(Position(i, y))

        for i in range(x + 1, board_size):
            if type(matrix[i][y]) == ChessPiece:
                break
            attackedPositions.append(Position(i, y))

        return attackedPositions


class KnightStrategy(Strategy):

    def check_in_board(self, x, y, board_size):
        return x >= 0 and x < board_size and y >= 0 and y < board_size

    def execute(self, position: Position, board_size, matrix):
        attackedPositions = []
        x = position.getX()
        y = position.getY()

        if type(matrix[x+3][y+2]) != ChessPiece and self.check_in_board(x+2, y+1, board_size):
            attackedPositions.append(Position(x+2, y+1))
        if type(matrix[x+3][y-2]) != ChessPiece and self.check_in_board(x+2, y-1, board_size):
            attackedPositions.append(Position(x+2, y-1))
        if type(matrix[x-3][y+2]) != ChessPiece and self.check_in_board(x-2, y+1, board_size):
            attackedPositions.append(Position(x-2, y+1))
        if type(matrix[x-3][y-2]) != ChessPiece and self.check_in_board(x-2, y-1, board_size):
            attackedPositions.append(Position(x-2, y-1))
        if type(matrix[x+2][y+3]) != ChessPiece and self.check_in_board(x+1, y+2, board_size):
            attackedPositions.append(Position(x+1, y+2))
        if type(matrix[x+2][y-3]) != ChessPiece and self.check_in_board(x+1, y-2, board_size):
            attackedPositions.append(Position(x+1, y-2))
        if type(matrix[x-2][y+3]) != ChessPiece and self.check_in_board(x-1, y+2, board_size):
            attackedPositions.append(Position(x-1, y+2))
        if type(matrix[x-2][y-3]) != ChessPiece and self.check_in_board(x-1, y-2, board_size):
            attackedPositions.append(Position(x-1, y-2))

        return attackedPositions
