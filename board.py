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
        self.chess_pieces.append(chess_piece)
        x = chess_piece.position.getX()
        y = chess_piece.position.getY()
        self.matrix[x][y] = chess_piece

    def executePieceMovements(self):
        for piece in self.chess_pieces:
            attackedPositions = piece.implementStrategy(self.size)
            for position in attackedPositions:
                x = position.getX()
                y = position.getY()
                self.matrix[x][y].addAttackingPiece(piece)

    def solve(self):
        initial_pos = Position(0, self.size - 1)
        final_pos = Position(self.size - 1, 0)
        initial_node = AStarNode(
            initial_pos, initial_pos.get_manhattan_distance_between(final_pos), 0, None)
        final_node = AStarNode(
            final_pos, 0, 0, None)
        print("hello")
        a_star_solver = AStarSolver(initial_node, final_node, self.size)
        solution_nodes = a_star_solver.solve()
        print(solution_nodes)

        return solution_nodes

    def print(self) -> None:
        for i in self.matrix:
            print("[", end=" ")
            for j in i:
                print(j, end="   ")
            print("]")
