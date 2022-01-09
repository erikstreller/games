"""
Classes and functions to define a chess piece object and his actions.
"""

from enum import Enum


class TextFormating:
    """Colors and text formating for chess pieces."""

    DARKCYAN = "\033[36m"
    PURPLE = "\033[95m"
    ITALICIZED = "\033[3m"
    BOLD = "\033[1m"
    END = "\033[0m"


class ChessPieceType(Enum):
    """All types of available chess pieces."""

    PAWN = "P"
    ROOK = "R"
    KNIGHT = "N"
    BISHOP = "B"
    QUEEN = "Q"
    KING = "K"
    EMPTY = " "


class ChessPieceColor(Enum):
    """Set the color attribute for both players."""

    BLACK = TextFormating.DARKCYAN
    WHITE = TextFormating.PURPLE


class ChessPiece:
    """Creates one chess piece object."""

    def __init__(self, type: ChessPieceType, color: ChessPieceColor) -> None:
        self.type = type
        self.color = color

    def print(self) -> str:
        return f"{self.color.value}{self.type.value}{TextFormating.END}"


class MovementType(Enum):
    """Types of movement available to a chess piece."""

    VALID = 0
    CAPTURE = 1
    INVALID = 2


def evaluate_movement(self: ChessPiece, target: ChessPiece) -> MovementType:
    """Evaluates the destination for empty squares, player or opponent pieces."""

    if target.type == ChessPieceType.EMPTY:
        return MovementType.VALID
    elif target.color != self.color:
        return MovementType.CAPTURE
    else:
        return MovementType.INVALID


def rook_movement(
    self: ChessPiece, x: int, y: int, board: list[list[ChessPiece]]
) -> None:
    """TODO:"""

    for xx in range(x, 7):
        target = board[xx + 1][y]
        movement = evaluate_movement(self, target)
        check_validity(xx + 1, y, movement, target)
        if movement in [MovementType.CAPTURE, MovementType.INVALID]:
            break
    for xx in range(x, 0, -1):
        target = board[xx - 1][y]
        movement = evaluate_movement(self, target)
        check_validity(xx, y, movement, target)
        if movement in [MovementType.CAPTURE, MovementType.INVALID]:
            break
    for yy in range(y, 7):
        target = board[x][yy + 1]
        movement = evaluate_movement(self, target)
        check_validity(x, yy + 1, movement, target)
        if movement in [MovementType.CAPTURE, MovementType.INVALID]:
            break
    for yy in range(y, 0, -1):
        target = board[x][yy - 1]
        movement = evaluate_movement(self, target)
        check_validity(x, yy - 1, movement, target)
        if movement in [MovementType.CAPTURE, MovementType.INVALID]:
            break


def bishop_movement(
    self: ChessPiece, x: int, y: int, board: list[list[ChessPiece]]
) -> None:
    """TODO:"""

    for xx, yy in zip(range(x, 7), range(y, 7)):
        if move_continuously(self, xx + 1, yy + 1, board) == True:
            break
    for xx, yy in zip(range(x, 0, -1), range(y, 0, -1)):
        if move_continuously(self, xx - 1, yy - 1, board) == True:
            break
    for xx, yy in zip(range(x, 0, -1), range(y, 7)):
        if move_continuously(self, xx - 1, yy + 1, board) == True:
            break
    for xx, yy in zip(range(x, 7), range(y, 0, -1)):
        if move_continuously(self, xx + 1, yy - 1, board) == True:
            break


def move_continuously(
    self: ChessPiece, x: int, y: int, board: list[list[ChessPiece]]
) -> bool:
    """TODO:"""

    target = board[x][y]
    movement = evaluate_movement(self, target)
    check_validity(x, y, movement, target)
    if movement in [MovementType.CAPTURE, MovementType.INVALID]:
        return True
    else:
        return False


def move_once(self: ChessPiece, x: int, y: int, board: list[list[ChessPiece]]) -> None:
    """TODO:"""

    target = board[x][y]
    movement = evaluate_movement(self, target)
    check_validity(x, y, movement, target)


def pawn_capture(
    self: ChessPiece, x: int, y: int, board: list[list[ChessPiece]]
) -> None:
    """TODO:"""

    target = board[x][y]
    if (movement := evaluate_movement(self, target)) == MovementType.CAPTURE:
        check_validity(x, y, movement, target)


def pawn_move(self: ChessPiece, x: int, y: int, board: list[list[ChessPiece]]) -> None:
    target = board[x][y]
    if (movement := evaluate_movement(self, target)) != MovementType.CAPTURE:
        check_validity(x, y, movement, target)


def movement_options(
    self: ChessPiece, x: int, y: int, board: list[list[ChessPiece]]
) -> None:
    """Defines how the pieces move."""

    if self.type == ChessPieceType.ROOK:
        print("Rook")
        rook_movement(self, x, y, board)

    if self.type == ChessPieceType.KNIGHT:
        if x + 2 < 8 and y + 1 < 8:
            move_once(self, x + 2, y + 1, board)

        if x + 1 < 8 and y + 2 < 8:
            move_once(self, x + 1, y + 2, board)

        if x - 2 >= 0 and y - 1 >= 0:
            move_once(self, x - 2, y - 1, board)

        if x - 1 >= 0 and y - 2 >= 0:
            move_once(self, x - 1, y - 2, board)

        if x + 2 < 8 and y - 1 >= 0:
            move_once(self, x + 2, y - 1, board)

        if x + 1 < 8 and y - 2 >= 0:
            move_once(self, x + 1, y - 2, board)

        if x - 2 < 8 and y + 1 < 8:
            move_once(self, x - 2, y + 1, board)

        if x - 1 < 8 and y + 2 < 8:
            move_once(self, x - 1, y + 2, board)

    if self.type == ChessPieceType.BISHOP:
        print("Bishop")
        bishop_movement(self, x, y, board)

    if self.type == ChessPieceType.QUEEN:
        print("Queen")
        rook_movement(self, x, y, board)
        bishop_movement(self, x, y, board)

    if self.type == ChessPieceType.KING:
        print("King")
        if x + 1 != 8:
            move_once(self, x + 1, y, board)

        if y + 1 != 8:
            move_once(self, x, y + 1, board)

        if x - 1 != -1:
            move_once(self, x - 1, y, board)

        if y - 1 != -1:
            move_once(self, x, y - 1, board)

        if x + 1 != 8 and y + 1 != 8:
            move_once(self, x + 1, y + 1, board)

        if x + 1 != 8 and y - 1 != -1:
            move_once(self, x + 1, y - 1, board)

        if x - 1 != -1 and y + 1 != 8:
            move_once(self, x - 1, y + 1, board)

        if x - 1 != -1 and y - 1 != -1:
            move_once(self, x - 1, y - 1, board)

    if self.type == ChessPieceType.PAWN:
        print("Pawn")
        if self.color == ChessPieceColor.BLACK:
            if y + 1 != 8:
                pawn_move(self, x, y + 1, board)

            if y == 1 and board[x][y + 1] == ChessPieceType.EMPTY:
                pawn_move(self, x, y + 2, board)

            if x + 1 != 8 and y + 1 != 8:
                pawn_capture(self, x + 1, y + 1, board)

            if x - 1 != -1 and y + 1 != 8:
                pawn_capture(self, x - 1, y + 1, board)

        if self.color == ChessPieceColor.WHITE:
            if y - 1 != -1:
                pawn_move(self, x, y - 1, board)

            if y == 6 and board[x][y - 1] == ChessPieceType.EMPTY:
                pawn_move(self, x, y - 2, board)

            if x + 1 != 8 and y - 1 != -1:
                pawn_capture(self, x + 1, y - 1, board)

            if x - 1 != -1 and y - 1 != -1:
                pawn_capture(self, x - 1, y - 1, board)


def check_validity(x: int, y: int, movement: MovementType, target: ChessPiece) -> None:
    """TODO:"""

    # TODO: user friendly output, e.g. e4
    if movement in [MovementType.VALID]:
        print(f"[{x}, {y}]")
    elif movement in [MovementType.CAPTURE]:
        print(f"{target.color.value}{target.type.value} [{x}, {y}]{TextFormating.END}")
    else:
        pass
