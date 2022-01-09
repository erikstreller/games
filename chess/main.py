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
        board[i][5] = ChessPiece(ChessPieceType.PAWN, ChessPieceColor.BLACK)

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


def playerTurn(color: ChessPieceColor) -> None:
    """A Turn where the player can choose a chess piece at a certain position and
    move it to a new position."""

    index0 = ("R", "N", "B", "Q", "K", "P")
    index1 = ("a", "b", "c", "d", "e", "f", "g", "h")
    index2 = ("1", "2", "3", "4", "5", "6", "7", "8")

    choose_piece = input(f"{color.value}Choose a chess piece: {TextFormating.END}")

    # TODO: add safty for input, e.g. Ba1 but Ra1 would be correct
    # FIXME: currently the input from choose_piece[0] is compared with the whole list in index0
    # not only with the ChessPieceType at the position choose_piece[1] and choose_piece[2]
    if len(choose_piece) == 3:
        if (
            choose_piece[0].upper() in index0
            and choose_piece[1].lower() in index1
            and choose_piece[2] in index2
        ):
            input_x = choose_piece[1].lower()
            input_y = int(choose_piece[2]) - 1
            x = transform_x(input_x)
            y = transform_y(input_y)

            return movement_options(board[x][y], x, y, board)
        else:
            print("Please enter the letter and position of the piece, e.g. Nb1 or Pe7")
            return playerTurn(color)
    else:
        print("Please enter the letter and position of the piece, e.g. Nb1 or Pe7")
        return playerTurn(color)


################### main ####################


def main() -> None:
    """The main function."""

    print("")
    initialize_board()
    draw_board()
    print("")
    playerTurn(ChessPieceColor.BLACK)
    print("")


if __name__ == "__main__":
    main()
