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
) -> list[list[int]]:
    """TODO:"""

    move_rook = []

    for xx in range(x, 7):
        move_rook.append(move_once(self, xx + 1, y, board))
        if evaluate_movement(self, board[xx + 1][y]) in [
            MovementType.CAPTURE,
            MovementType.INVALID,
        ]:
            break
    for xx in range(x, 0, -1):
        move_rook.append(move_once(self, xx - 1, y, board))
        if evaluate_movement(self, board[xx - 1][y]) in [
            MovementType.CAPTURE,
            MovementType.INVALID,
        ]:
            break
    for yy in range(y, 7):
        move_rook.append(move_once(self, x, yy + 1, board))
        if evaluate_movement(self, board[x][yy + 1]) in [
            MovementType.CAPTURE,
            MovementType.INVALID,
        ]:
            break
    for yy in range(y, 0, -1):
        move_rook.append(move_once(self, x, yy - 1, board))
        if evaluate_movement(self, board[x][yy - 1]) in [
            MovementType.CAPTURE,
            MovementType.INVALID,
        ]:
            break

    return (move_rook := remove_none(move_rook))


def bishop_movement(
    self: ChessPiece, x: int, y: int, board: list[list[ChessPiece]]
) -> list[list[int]]:
    """TODO:"""

    move_bishop = []

    for xx, yy in zip(range(x, 7), range(y, 7)):
        move_bishop.append(move_once(self, xx + 1, yy + 1, board))
        if evaluate_movement(self, board[xx + 1][yy + 1]) in [
            MovementType.CAPTURE,
            MovementType.INVALID,
        ]:
            break
    for xx, yy in zip(range(x, 0, -1), range(y, 0, -1)):
        move_bishop.append(move_once(self, xx - 1, yy - 1, board))
        if evaluate_movement(self, board[xx - 1][yy - 1]) in [
            MovementType.CAPTURE,
            MovementType.INVALID,
        ]:
            break
    for xx, yy in zip(range(x, 0, -1), range(y, 7)):
        move_bishop.append(move_once(self, xx - 1, yy + 1, board))
        if evaluate_movement(self, board[xx - 1][yy + 1]) in [
            MovementType.CAPTURE,
            MovementType.INVALID,
        ]:
            break
    for xx, yy in zip(range(x, 7), range(y, 0, -1)):
        move_bishop.append(move_once(self, xx + 1, yy - 1, board))
        if evaluate_movement(self, board[xx + 1][yy - 1]) in [
            MovementType.CAPTURE,
            MovementType.INVALID,
        ]:
            break

    return (move_bishop := remove_none(move_bishop))


def remove_none(item: list):
    remove_none = filter(None.__ne__, item)
    item = list(remove_none)
    return item


def move_once(
    self: ChessPiece, x: int, y: int, board: list[list[ChessPiece]]
) -> list[int] | None:
    """TODO:"""

    target = board[x][y]
    movement = evaluate_movement(self, target)
    options = check_validity(x, y, movement, target)
    return options


def pawn_capture(
    self: ChessPiece, x: int, y: int, board: list[list[ChessPiece]]
) -> list[int] | None:
    """TODO:"""

    target = board[x][y]
    if (movement := evaluate_movement(self, target)) == MovementType.CAPTURE:
        options = check_validity(x, y, movement, target)
        return options


def pawn_move(
    self: ChessPiece, x: int, y: int, board: list[list[ChessPiece]]
) -> list[int] | None:
    target = board[x][y]
    if (movement := evaluate_movement(self, target)) != MovementType.CAPTURE:
        options = check_validity(x, y, movement, target)
        return options


def movement_options(
    self: ChessPiece, x: int, y: int, board: list[list[ChessPiece]]
) -> list[list[int]]:
    """Defines how the pieces move."""

    if self.type == ChessPieceType.ROOK:
        print("Rook")
        move_rook = rook_movement(self, x, y, board)
        return move_rook

    if self.type == ChessPieceType.KNIGHT:
        move_knight = []

        if x + 2 < 8 and y + 1 < 8:
            move_knight.append(move_once(self, x + 2, y + 1, board))

        if x + 1 < 8 and y + 2 < 8:
            move_knight.append(move_once(self, x + 1, y + 2, board))

        if x - 2 >= 0 and y - 1 >= 0:
            move_knight.append(move_once(self, x - 2, y - 1, board))

        if x - 1 >= 0 and y - 2 >= 0:
            move_knight.append(move_once(self, x - 1, y - 2, board))

        if x + 2 < 8 and y - 1 >= 0:
            move_knight.append(move_once(self, x + 2, y - 1, board))

        if x + 1 < 8 and y - 2 >= 0:
            move_knight.append(move_once(self, x + 1, y - 2, board))

        if x - 2 >= 0 and y + 1 < 8:
            move_knight.append(move_once(self, x - 2, y + 1, board))

        if x - 1 >= 0 and y + 2 < 8:
            move_knight.append(move_once(self, x - 1, y + 2, board))

        return (move_knight := remove_none(move_knight))

    if self.type == ChessPieceType.BISHOP:
        print("Bishop")
        move_bishop = bishop_movement(self, x, y, board)
        return move_bishop

    if self.type == ChessPieceType.QUEEN:
        print("Queen")
        move_queen = []
        move_queen = rook_movement(self, x, y, board) + bishop_movement(
            self, x, y, board
        )
        return move_queen

    if self.type == ChessPieceType.KING:
        print("King")
        move_king = []

        if x + 1 != 8:
            move_king.append(move_once(self, x + 1, y, board))
        if y + 1 != 8:
            move_king.append(move_once(self, x, y + 1, board))

        if x - 1 != -1:
            move_king.append(move_once(self, x - 1, y, board))

        if y - 1 != -1:
            move_king.append(move_once(self, x, y - 1, board))

        if x + 1 != 8 and y + 1 != 8:
            move_king.append(move_once(self, x + 1, y + 1, board))

        if x + 1 != 8 and y - 1 != -1:
            move_king.append(move_once(self, x + 1, y - 1, board))

        if x - 1 != -1 and y + 1 != 8:
            move_king.append(move_once(self, x - 1, y + 1, board))

        if x - 1 != -1 and y - 1 != -1:
            move_king.append(move_once(self, x - 1, y - 1, board))

        return (move_king := remove_none(move_king))

    if self.type == ChessPieceType.PAWN:
        print("Pawn")
        move_pawn = []
        if self.color == ChessPieceColor.BLACK:
            if y + 1 != 8:
                move_pawn.append(pawn_move(self, x, y + 1, board))
            if y == 1 and board[x][y + 1].type == ChessPieceType.EMPTY:
                move_pawn.append(pawn_move(self, x, y + 2, board))

            if x + 1 != 8 and y + 1 != 8:
                move_pawn.append(pawn_capture(self, x + 1, y + 1, board))

            if x - 1 != -1 and y + 1 != 8:
                move_pawn.append(pawn_capture(self, x - 1, y + 1, board))

        if self.color == ChessPieceColor.WHITE:
            if y - 1 != -1:
                move_pawn.append(pawn_move(self, x, y - 1, board))

            if y == 6 and board[x][y - 1].type == ChessPieceType.EMPTY:
                move_pawn.append(pawn_move(self, x, y - 2, board))

            if x + 1 != 8 and y - 1 != -1:
                move_pawn.append(pawn_capture(self, x + 1, y - 1, board))

            if x - 1 != -1 and y - 1 != -1:
                move_pawn.append(pawn_capture(self, x - 1, y - 1, board))

        return (move_pawn := remove_none(move_pawn))

    else:
        raise Exception(f"Type {self.type} is not considered.")


def check_validity(
    x: int, y: int, movement: MovementType, target: ChessPiece
) -> list[int] | None:
    """TODO:"""
    # TODO: remove duplicates (only one if for .VALID and .CAPTURE)
    # if tests are complete

    if movement in [MovementType.VALID]:
        # print(f"[{x}, {y}]")
        return [x, y]
    elif movement in [MovementType.CAPTURE]:
        # print(f"{target.color.value}{target.type.value} [{x}, {y}]{TextFormating.END}")
        return [x, y]
