from board import Board
from chess_piece import ChessPiece
from position import Position
from strategy import KnightStrategy, QueenStrategy
from pygame_utils import PuzzleDrawer
BOARD_SIZE = 8
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500


def main():
    board = Board(BOARD_SIZE)
    queen_piece_1 = ChessPiece(
        Position(0, 0), QueenStrategy(), "Q")
    queen_piece_2 = ChessPiece(
        Position(2, 3), QueenStrategy(), "Q")

    knight_piece = ChessPiece(Position(1, 2), KnightStrategy(), "C")
    # board.add_piece(queen_piece_1)
    board.add_piece(queen_piece_2)
    board.add_piece(knight_piece)
    board.print()
    board.executePieceMovements()

    puzzle_drawer = PuzzleDrawer(WINDOW_WIDTH, WINDOW_HEIGHT)
    puzzle_drawer.draw(board)

    # board.solve()


main()
