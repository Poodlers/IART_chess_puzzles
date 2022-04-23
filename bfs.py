from time import sleep
from chess_piece import ChessPiece
from position import Position
from itertools import combinations
from node import Node
from solver import Solver

class BFSNode(Node):
    def __init__(self, snake):
        super().__init__(snake)

    def get_node_sucessors(self, board_size, board, chess_pieces):
        successors = []

        sucessor_generation = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for suc in sucessor_generation:
            suc_x = self.snake[-1].x + suc[0]
            suc_y = self.snake[-1].y + suc[1]
            suc_pos = Position(suc_x, suc_y)
            if suc_x >= 0 and suc_x < board_size and suc_y >= 0 and suc_y < board_size and suc_pos not in self.snake and self.not_adjacent_to_snake(suc_pos) and type(board[suc_pos.x][suc_pos.y]) != ChessPiece:
                new_snake = self.snake + [suc_pos]
                successor = BFSNode(new_snake)
                successors.append(successor)
        return successors

class BFSSolver(Solver):
    def __init__(self, initial_node, final_pos, board_size, board, chess_pieces) -> None:
        super().__init__(initial_node, final_pos, board_size, board, chess_pieces)
