from strategy import KingStrategy, QueenStrategy, KnightStrategy, RookStrategy
from chess_piece import ChessPiece
from position import Position
from board import Board


def hard_game_board_init():
    BOARD_SIZE = 6
    board = Board(BOARD_SIZE)

    king_piece = ChessPiece(Position(4, 2), KingStrategy(), "K")
    rook_piece = ChessPiece(Position(3, 0), RookStrategy(), "R")
    knight_piece = ChessPiece(Position(3, 3), KnightStrategy(), "k")

    board.add_piece(rook_piece)
    board.add_piece(king_piece)
    board.add_piece(knight_piece)
    board.executePieceMovements()
    board.print()
    return board


def easy_game_board_init():
    BOARD_SIZE = 5
    board = Board(BOARD_SIZE)

    king_piece = ChessPiece(Position(3, 1), KingStrategy(), "K")
    rook_piece = ChessPiece(Position(1, 1), RookStrategy(), "R")

    board.add_piece(rook_piece)
    board.add_piece(king_piece)
    board.executePieceMovements()
    board.print()
    return board
