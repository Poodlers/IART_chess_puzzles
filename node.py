from time import sleep
from chess_piece import ChessPiece
from position import Position
from itertools import combinations

class Node:
    def __init__(self, snake):
        self.snake = snake
    
    def not_adjacent_to_snake(self, new_pos):
        # at the time of putting a square, check that it has no more than one diagonal adjacent already on the snake
        # if he does have, then its not a valid snake!

        new_pos_adjacents = [
            Position(new_pos.x - 1, new_pos.y), Position(new_pos.x +
                                                         1, new_pos.y), Position(new_pos.x, new_pos.y - 1),
            Position(new_pos.x, new_pos.y + 1)]

        new_pos_diagonals = [
            Position(new_pos.x - 1, new_pos.y - 1), Position(new_pos.x +
                                                             1, new_pos.y - 1), Position(new_pos.x + 1, new_pos.y + 1),
            Position(new_pos.x - 1, new_pos.y + 1)]
        num_of_adjacents = 0
        for neighbour in new_pos_diagonals:
            if neighbour in self.snake:
                num_of_adjacents += 1
        if num_of_adjacents > 1:
            return False

        num_of_adjacents = 0
        for neighbour in new_pos_adjacents:
            if neighbour in self.snake:
                num_of_adjacents += 1
        if num_of_adjacents != 1:
            return False
        return True