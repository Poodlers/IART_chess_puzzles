from abc import ABC, abstractmethod

from position import Position


class Strategy(ABC):  # Strategy
    @abstractmethod
    def execute(self, position: Position, board_size):
        pass


class KingStrategy(Strategy):
    def execute(self, position: Position, board_size):
        attackedPositions = []

        return attackedPositions


class QueenStrategy(Strategy):
    def execute(self, position: Position, board_size):
        attackedPositions = []
        x = position.getX()
        y = position.getY()
        curr_row = x
        curr_col = y
        while curr_row > 0 and curr_col > 0:
            curr_col -= 1
            curr_row -= 1
        # we have coordinate of the upper left of this diagonal
        while curr_col < board_size and curr_row < board_size:
            if curr_row != x and curr_col != y:
                attackedPositions.append(Position(curr_row, curr_col))
            curr_col += 1
            curr_row += 1

        curr_row = x
        curr_col = y

        while curr_row > 0 and curr_col < board_size:
            curr_row -= 1
            curr_col += 1
        # we have coordinate of the upper right of this diagonal
        while curr_col >= 0 and curr_row < board_size:
            if curr_row != x and curr_col != y:
                attackedPositions.append(Position(curr_row, curr_col))
            curr_col -= 1
            curr_row += 1

        for s in range(board_size):
            attackedPositions.append(Position(x, s))
            attackedPositions.append(Position(s, y))
        return attackedPositions
