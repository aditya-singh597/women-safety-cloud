import random

def get_choice():
    options = ["rock","paper","scissors"]
    player_choice = input("Enter your choice: rock, paper, or scissors: ")
    computer_choice = random.choice(options)
    choices = {"player":player_choice, "computer":computer_choice}
    return choices

def check_win(player,computer):
    print(f"You chose {player}, computer chose {computer}")
    if player == computer :
        return "It's a tie"
    elif player == "rock":
        if computer == "scissors":
            return "Rock smashes scissors! You win!"
        else:
            return "Paper covers rock! You lose!"
    elif player == "paper":
        if computer == "scissors":
            return "scissors cut paper! You lose!"
        else:
            return "Paper covers rock! You win!"
    elif player == "scissors":
        if computer == "paper":
            return "scissors cuts paper! You win!"
        else:
            return "Rock smashes scissors! You lose!"        
              

choices = get_choice()
result = check_win(choices["player"],choices["computer"])
print(result)
    