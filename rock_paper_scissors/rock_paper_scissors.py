"""
Rock Paper Scissors with python.
"""

import random

################### start ###################


def greeting() -> None:
    print("\n---------------------------------------")
    print("Welcome to a round Rock Paper Scissors.")
    print("---------------------------------------")
    print("You will play against me.")


def rounds_playing() -> int:
    try:
        rounds = int(input("-> How many rounds do you want to play?: "))
        if rounds >= 3 and rounds % 2 == 1:
            print("Okay. We are playing " + str(rounds) + " rounds.")
            return rounds
        else:
            print("It's not an odd number and 3 or higher, isn't it?")
            return rounds_playing()
    except:
        print("Nope. Not doing this.")
        return rounds_playing()


################# game loop #################


def player_turn() -> str:
    player_input = input("\n-> Chosse one: 1 Rock, 2 Paper or 3 Scissors: ")

    if player_input == "1" or player_input.capitalize() == "Rock":
        player_choice = "Rock"
        return player_choice
    elif player_input == "2" or player_input.capitalize() == "Paper":
        player_choice = "Paper"
        return player_choice
    elif player_input == "3" or player_input.capitalize() == "Scissors":
        player_choice = "Scissors"
        return player_choice
    else:
        print("Thats not a valid input. Try again.")
        return player_turn()


def cpu_turn() -> str:
    choices = ["Rock", "Paper", "Scissors"]
    cpu_choice = random.choice(choices)
    return cpu_choice


def compare_choices(player_choice: str, cpu_choice: str) -> str:
    rock_tie = player_choice == "Rock" and cpu_choice == "Rock"
    paper_tie = player_choice == "Paper" and cpu_choice == "Paper"
    scissors_tie = player_choice == "Scissors" and cpu_choice == "Scissors"

    player_rock_win = player_choice == "Rock" and cpu_choice == "Scissors"
    player_paper_win = player_choice == "Paper" and cpu_choice == "Rock"
    player_scissors_win = player_choice == "Scissors" and cpu_choice == "Paper"

    player_rock_loss = player_choice == "Rock" and cpu_choice == "Paper"
    player_paper_loss = player_choice == "Paper" and cpu_choice == "Scissors"
    player_scissors_loss = player_choice == "Scissors" and cpu_choice == "Rock"

    if rock_tie or paper_tie or scissors_tie:
        print("We both chose " + player_choice + ". A Tie it is.")
        result = "Tie"
        return result
    elif player_rock_win or player_paper_win or player_scissors_win:
        print(
            "Good play. You won with " + player_choice + " over my " + cpu_choice + "."
        )
        result = "Win"
        return result
    elif player_rock_loss or player_paper_loss or player_scissors_loss:
        print("Yes. I won! My " + cpu_choice + " beat your " + player_choice + ".")
        result = "Loss"
        return result
    else:
        raise Exception(
            f"Case for player choice: {player_choice} and cpu coice: {player_choice} is not considered."
        )


def score_count(result: str, score: list[int]) -> list[int]:
    if result == "Win":
        score[0] += 1
        return score
    elif result == "Loss":
        score[1] += 1
        return score
    else:
        return score


def check_win(rounds: int, score: list) -> bool:
    win_condition = score[0] == (rounds // 2) + 1
    loss_condition = score[1] == (rounds // 2) + 1

    if win_condition:
        print("\n### You won. Well done! ###")
        return True
    elif loss_condition:
        print("\n### You lost against a mighty me! ###")
        return True
    else:
        return False


def display_score(score: list) -> None:
    if score[0] > score[1]:
        print("# You are in the lead: " + str(score))
    elif score[0] < score[1]:
        print("# You are behind: " + str(score))
    elif score[0] == score[1]:
        print("# It is even: " + str(score))


#################### end ####################


def ending(score: list) -> None:
    print(
        "You have scored ["
        + str(score[0])
        + "] wins against ["
        + str(score[1])
        + "].\n"
    )


################### main ####################


def main() -> None:
    greeting()
    rounds = rounds_playing()
    score = [0, 0]

    while True:
        player_choice = player_turn()
        cpu_choice = cpu_turn()
        result = compare_choices(player_choice, cpu_choice)
        score = score_count(result, score)
        game_is_finished = check_win(rounds, score)

        if game_is_finished == True:
            break

        display_score(score)

    ending(score)


#############################################


if __name__ == "__main__":
    main()
