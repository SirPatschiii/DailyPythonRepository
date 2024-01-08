import random


global possible_actions


def calc_result(user_action, computer_action):
    if user_action in possible_actions:
        if user_action == computer_action:
            return 2
        if user_action == "rock" and computer_action == "paper":
            return 0
        if user_action == "rock" and computer_action == "scissors":
            return 1
        if user_action == "paper" and computer_action == "rock":
            return 1
        if user_action == "paper" and computer_action == "scissors":
            return 0
        if user_action == "scissors" and computer_action == "paper":
            return 1
        if user_action == "scissors" and computer_action == "rock":
            return 0
    else:
        return -1


def main():
    global possible_actions

    user_action = input("Enter a choice (rock, paper, scissors): ")
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
    user_action = user_action.lower()

    state = calc_result(user_action, computer_action)

    if state != -1:
        print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

    match state:
        case -1:
            print(f"\nInvalid input!")
        case 0:
            print("You've lost!")
        case 1:
            print("You've won!")
        case 2:
            print("It's a tie!")


if __name__ == '__main__':
    main()
