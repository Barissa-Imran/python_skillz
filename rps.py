import random

def play():
    # rock, paper, scissors
    player = input("Play rock, paper, scissors. Pick r, p, s respectively:\n")
    computer = random.choice(["r", "p", "s"])
    if player.lower() == computer:
        print("You have tied")
    else:
        is_win(player, computer)

def is_win(player, computer):
    if player.lower() == "r" and computer == "s":
        print("You win!")
    elif player.lower() == "p" and computer == "r":
        print("You win!")
    elif player.lower() == "s" and computer == "p":
        print("You win!")
    else:
        is_loss(player, computer)

def is_loss(player, computer):
    if computer == "p" and player.lower() == "r":
        print("You lose!")
    elif computer == "s" and player.lower() == "p":
        print("You lose!")
    elif computer == "r" and player.lower() == "s":
        print("You lose!")
    pass

play()