"""
Tic Tac Toe with python.
"""

import random

################### board ###################

board = [" " for x in range(1, 10)]

################### start ###################


def draw_board() -> None:
    print(board[6] + " | " + board[7] + " | " + board[8])
    print("-- --- --")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("-- --- --")
    print(board[0] + " | " + board[1] + " | " + board[2])


def greeting() -> None:
    print("Your are playing Tic Tac Toe against me.")


def choose_letter() -> str:
    letter = input("Please choose a letter: X or O to continue: ")

    if letter.capitalize() == "X":
        print("You choose X.")
        letter = "X"
        return letter
    elif letter.capitalize() == "O":
        print("You choose O.")
        letter = "O"
        return letter
    else:
        print("Wrong letter input.")
        return choose_letter()


################# game loop #################


def recurring_player_turn(letter: str) -> list[str]:
    print("Choose a position.")

    try:
        position = int(input())
        options = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        if position in options:
            return insert_letter(position - 1, letter)
        else:
            print("Choose a number between 1 and 9.")
            return recurring_player_turn(letter)
    except ValueError:
        print("Invalid Input. Enter a number between 1 and 9.")
        return recurring_player_turn(letter)


def recurring_cpu_turn(letter: str) -> list[str]:
    cpu_letter = ""
    if letter == "X":
        cpu_letter = "O"
    elif letter == "O":
        cpu_letter = "X"
    else:
        raise Exception(f"Letter: {letter} is not considered.")

    free_space = [i for i, x in enumerate(board) if x == " "]
    cpu_position = random.choice(free_space)

    return insert_letter(cpu_position, cpu_letter)


def insert_letter(position: int, letter: str) -> list[str]:
    if board[position] == " ":
        board[position] = letter
        return board
    else:
        print("Space is not empty.")
        return recurring_player_turn(letter)


def won(board: list[str], letter: str) -> bool:
    return (
        (board[0] == letter and board[1] == letter and board[2] == letter)
        or (board[3] == letter and board[4] == letter and board[5] == letter)
        or (board[6] == letter and board[7] == letter and board[8] == letter)
        or (board[0] == letter and board[3] == letter and board[6] == letter)
        or (board[1] == letter and board[4] == letter and board[7] == letter)
        or (board[2] == letter and board[5] == letter and board[8] == letter)
        or (board[0] == letter and board[4] == letter and board[8] == letter)
        or (board[2] == letter and board[4] == letter and board[6] == letter)
    )


def full_board() -> bool:
    if " " not in board:
        return True
    else:
        return False


def check_won(letter: str) -> bool:
    if won(board, "X") == True:
        if letter == "X":
            won_message()
            return True
        else:
            lost_message()
            return True
    elif won(board, "O") == True:
        if letter == "O":
            won_message()
            return True
        else:
            lost_message()
            return True
    else:
        return False


################# messages ##################


def tie_message() -> None:
    print("")
    print("###################")
    print("### It's a tie. ###")
    print("###################")
    print("")


def won_message() -> None:
    print("")
    print("################")
    print("### You won! ###")
    print("################")
    print("")


def lost_message() -> None:
    print("")
    print("#################")
    print("### You lost. ###")
    print("#################")
    print("")


################### main ####################


def main():
    greeting()
    letter = choose_letter()

    while not full_board():
        draw_board()
        recurring_player_turn(letter)
        if check_won(letter) == True:
            break
        if full_board():
            tie_message()
            break
        if not full_board():
            recurring_cpu_turn(letter)
            if check_won(letter) == True:
                break
            if full_board():
                tie_message()
                break

    draw_board()
    print("")


if __name__ == "__main__":
    main()
