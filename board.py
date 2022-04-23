from board_element import BoardElement, EmptySquare
from chess_piece import ChessPiece
from a_star import AStarSolver, AStarNode
from position import Position


class Board:
    def __init__(self, size: int) -> None:
        self.size = size
        self.matrix = [[EmptySquare() for x in range(size)]
                       for x in range(size)]
        self.chess_pieces = []

    def add_piece(self, chess_piece: ChessPiece) -> None:
        x = chess_piece.position.getX()
        y = chess_piece.position.getY()
        for piece in self.chess_pieces:
            if (piece.position.x == x and piece.position.y == y):
                raise Exception("square already has another chess piece")
        self.chess_pieces.append(chess_piece)
        self.matrix[x][y] = chess_piece

    def executePieceMovements(self):
        for piece in self.chess_pieces:
            attackedPositions = piece.implementStrategy(self.size, self.matrix)
            for position in attackedPositions:
                x = position.getX()
                y = position.getY()
                self.matrix[x][y].addAttackingPiece(piece)

    def solve(self, puzzle_drawer):
        final_pos = Position(0, self.size - 1)
        initial_pos = Position(self.size - 1, 0)
        initial_node = AStarNode(
            [initial_pos], 0, 0)

        a_star_solver = AStarSolver(
            initial_node, final_pos, self.size, self.matrix, self.chess_pieces)
        solution_nodes = a_star_solver.solve(puzzle_drawer)

        return solution_nodes

    def print(self) -> None:
        for i in self.matrix:
            print("[", end=" ")
            for j in i:
                print(j, end=" ")
            print("]")

    def print_all_attacked_squares(self):
        for i in range(self.size):
            for j in range(self.size):
                print("(", i, ",", j, ") - >",
                      self.matrix[i][j].getAttackingPieces())
