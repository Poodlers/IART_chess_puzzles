from board_element import BoardElement, EmptySquare
from chess_piece import ChessPiece


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

    def print(self) -> None:
        for i in self.matrix:
            print("[", end=" ")
            for j in i:
                print(j, end="   ")
            print("]")
