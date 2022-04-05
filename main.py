from board import Board
from chess_piece import ChessPiece
from position import Position
from strategy import KnightStrategy, QueenStrategy, KingStrategy, RookStrategy
from pygame_utils import PuzzleDrawer
BOARD_SIZE = 6
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500


def main():
    board = Board(BOARD_SIZE)

    king_piece = ChessPiece(Position(4, 2), KingStrategy(), "K")
    #queen_piece = ChessPiece(Position(0, 0), QueenStrategy(), "Q")
    rook_piece = ChessPiece(Position(3, 0), RookStrategy(), "R")
    knight_piece = ChessPiece(Position(3, 3), KnightStrategy(), "k")

    # board.add_piece(queen_piece)
    board.add_piece(rook_piece)
    board.add_piece(king_piece)
    board.add_piece(knight_piece)
    board.print()
    board.executePieceMovements()
    # board.print_all_attacked_squares()

    puzzle_drawer = PuzzleDrawer(WINDOW_WIDTH, WINDOW_HEIGHT)
    puzzle_drawer.draw(board)

    # board.solve()


main()
