import random


def play():
    while True:
        player = input("Would you like to roll the dice? Y or N\n")
        if player.lower() == "y":
            dice()
            continue
        else:
            break


def dice():
    roll = random.randrange(1, 6)
    print(f"You have rolled: {roll}")


play()
