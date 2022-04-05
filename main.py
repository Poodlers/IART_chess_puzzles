from board import Board
from chess_piece import ChessPiece
from position import Position
from strategy import KnightStrategy, QueenStrategy, KingStrategy, RookStrategy
from pygame_utils import PuzzleDrawer
BOARD_SIZE = 5
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500


def main():
    board = Board(BOARD_SIZE)

    king_piece = ChessPiece(Position(3, 1), KingStrategy(), "K")
    # queen_piece = ChessPiece(Position(2, 3), QueenStrategy(), "Q")
    rook_piece = ChessPiece(Position(1, 1), RookStrategy(), "R")
    #knight_piece = ChessPiece(Position(4, 2), KnightStrategy(), "k")

    # board.add_piece(queen_piece)
    board.add_piece(rook_piece)
    board.add_piece(king_piece)
    board.print()
    board.executePieceMovements()

    puzzle_drawer = PuzzleDrawer(WINDOW_WIDTH, WINDOW_HEIGHT)
    puzzle_drawer.draw(board)

    # board.solve()


main()
