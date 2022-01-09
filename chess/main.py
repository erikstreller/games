"""
Chess with python.
"""

from piece import (
    ChessPiece,
    ChessPieceColor,
    ChessPieceType,
    TextFormating,
    movement_options,
)

################### board ###################

"""The chess board as grid 8x8."""
board = [
    [ChessPiece(ChessPieceType.EMPTY, ChessPieceColor.WHITE) for x in range(8)]
    for y in range(8)
]


def initialize_board() -> None:
    """Sets the starting positions of the chess pieces on the board for both players."""

    board[0][0] = ChessPiece(ChessPieceType.ROOK, ChessPieceColor.BLACK)
    board[1][0] = ChessPiece(ChessPieceType.KNIGHT, ChessPieceColor.BLACK)
    board[2][0] = ChessPiece(ChessPieceType.BISHOP, ChessPieceColor.BLACK)
    board[3][0] = ChessPiece(ChessPieceType.QUEEN, ChessPieceColor.BLACK)
    board[4][0] = ChessPiece(ChessPieceType.KING, ChessPieceColor.BLACK)
    board[5][0] = ChessPiece(ChessPieceType.BISHOP, ChessPieceColor.BLACK)
    board[6][0] = ChessPiece(ChessPieceType.KNIGHT, ChessPieceColor.BLACK)
    board[7][0] = ChessPiece(ChessPieceType.ROOK, ChessPieceColor.BLACK)

    for i in range(8):
        board[i][1] = ChessPiece(ChessPieceType.PAWN, ChessPieceColor.BLACK)

    for j in range(8):
        board[j][6] = ChessPiece(ChessPieceType.PAWN, ChessPieceColor.WHITE)

    board[0][7] = ChessPiece(ChessPieceType.ROOK, ChessPieceColor.WHITE)
    board[1][7] = ChessPiece(ChessPieceType.KNIGHT, ChessPieceColor.WHITE)
    board[2][7] = ChessPiece(ChessPieceType.BISHOP, ChessPieceColor.WHITE)
    board[3][7] = ChessPiece(ChessPieceType.QUEEN, ChessPieceColor.WHITE)
    board[4][7] = ChessPiece(ChessPieceType.KING, ChessPieceColor.WHITE)
    board[5][7] = ChessPiece(ChessPieceType.BISHOP, ChessPieceColor.WHITE)
    board[6][7] = ChessPiece(ChessPieceType.KNIGHT, ChessPieceColor.WHITE)
    board[7][7] = ChessPiece(ChessPieceType.ROOK, ChessPieceColor.WHITE)


def draw_board() -> None:
    """
    Displays the chess board with pieces and borders.
    Y-axis is drawn top to bottom and x-axis left to right.
    """

    for y in range(8):
        for x in range(8):
            status = board[x][y].print()
            if x == 7:
                print(status)
            else:
                print(f"{status} | ", end="")

        if y != 7:
            print("--+---+---+---+---+---+---+--")


################ player turn ################


def transform_x(input_x: str) -> int:
    """Transforms the players x-axis input to the corresponding location on the grid."""

    x = ["a", "b", "c", "d", "e", "f", "g", "h"]
    return x.index(input_x)


def transform_y(input_y: int) -> int:
    """Transforms the players y-axis input to the corresponding location on the grid."""

    y = [7, 6, 5, 4, 3, 2, 1, 0]
    return y[input_y]


def wrong_input():
    print("Please enter the matching letter and position of the piece, e.g. Nb1 or Pe7")


def player_turn(color: ChessPieceColor):
    """A Turn where the player can choose a chess piece at a certain position and
    move it to a new position."""
    # FIXME: return type

    index0 = ("R", "N", "B", "Q", "K", "P")
    index1 = ("a", "b", "c", "d", "e", "f", "g", "h")
    index2 = ("1", "2", "3", "4", "5", "6", "7", "8")

    choose_piece = input(f"{color.value}Choose a chess piece: {TextFormating.END}")

    if len(choose_piece) != 3:
        wrong_input()
        return player_turn(color)
    if (
        choose_piece[0].upper() not in index0
        and choose_piece[1].lower() not in index1
        and choose_piece[2] not in index2
    ):
        wrong_input()
        return player_turn(color)

    input_x = choose_piece[1].lower()
    input_y = int(choose_piece[2]) - 1
    x = transform_x(input_x)
    y = transform_y(input_y)

    if board[x][y].type.value != choose_piece[0].upper():
        wrong_input()
        return player_turn(color)

    options = movement_options(board[x][y], x, y, board)
    move_to = player_move(color, options)
    move_piece(board[x][y], x, y, move_to, options)


def player_move(color: ChessPieceColor, options: list) -> int:
    """Takes the movement options for the choosen piece. Displays the
    input number for the available movement options and"""

    for i in range(len(options)):
        target_position = options[i]
        target_type = board[target_position[0]][target_position[1]].type

        if target_type == ChessPieceType.EMPTY:
            print(f"({i + 1}) {transform(options[i])}")

        if target_type != ChessPieceType.EMPTY:
            if color == ChessPieceColor.BLACK:
                print(
                    f"{ChessPieceColor.WHITE.value}({i + 1}) {target_type.value}{transform(options[i])}{TextFormating.END}"
                )
            if color == ChessPieceColor.WHITE:
                print(
                    f"{ChessPieceColor.BLACK.value}({i + 1}) {target_type.value}{transform(options[i])}{TextFormating.END}"
                )

    move_to = input("Move to?: ")
    try:
        int(move_to)
    except ValueError:
        if len(options) != 1:
            print(f"Invalid Input. Enter a number between 1 and {len(options)}.")
            return player_move(color, options)
        else:
            print(f"Invalid Input. To only valid move is number 1.")
            return player_move(color, options)

    if int(move_to) > len(options) or int(move_to) <= 0:
        print(f"Invalid Input. Enter a number between 1 and {len(options)}.")
        return player_move(color, options)

    return int(move_to)


def move_piece(
    self: ChessPiece, x: int, y: int, move_to: int, options: list[list[int]]
) -> None:
    """Sets origin to empty and destination to chess piece opbject."""

    board[x][y] = ChessPiece(ChessPieceType.EMPTY, self.color)

    xx, yy = options[move_to - 1]
    board[xx][yy] = ChessPiece(self.type, self.color)


def transform(input: list[int]) -> str:
    """Transform the internal coordinate system to chess coordinate pairs."""

    x, y = input[0], input[1]

    visual_x = ("a", "b", "c", "d", "e", "f", "g", "h")
    visual_y = ("8", "7", "6", "5", "4", "3", "2", "1")

    display_x = visual_x[x]
    display_y = visual_y[y]

    output = display_x + display_y
    return output


################### win? ####################


def win() -> bool:
    two_kings = []
    for i in range(8):
        for j in range(8):
            if board[i][j].type == ChessPieceType.KING:
                two_kings.append(board[i][j].type.value)

    if len(two_kings) != 2:
        return True
    else:
        return False


################### main ####################


def main() -> None:
    """The main function."""

    print("")
    initialize_board()
    draw_board()
    print("")
    while not win():
        player_turn(ChessPieceColor.WHITE)
        draw_board()
        if not win():
            player_turn(ChessPieceColor.BLACK)
            draw_board()

    print("")


if __name__ == "__main__":
    main()
