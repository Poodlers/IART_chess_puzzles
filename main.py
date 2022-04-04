from board import Board
from chess_piece import ChessPiece
from position import Position
from strategy import QueenStrategy
from pygame_utils import PuzzleDrawer
BOARD_SIZE = 8
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500


def main():
    board = Board(BOARD_SIZE)
    queen_piece = ChessPiece(
        Position(2, 2), QueenStrategy(), "Q")
    board.add_piece(queen_piece)
    board.print()
    board.executePieceMovements()

    puzzle_drawer = PuzzleDrawer(WINDOW_WIDTH, WINDOW_HEIGHT)
    puzzle_drawer.draw(board)

    # board.solve()


main()
