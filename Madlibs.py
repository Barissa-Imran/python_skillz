# Test cases:
# noun(goat)
# pronoun(a)
# adjective(cook)

def play():
    while True:
        que = input("would you like to play madlibs? Y or N\n")
        if que.lower() == "y":
            noun = input("Enter a noun of your choosing: ")
            pronoun = input("Enter a pronoun of your choosing: ")
            adjective = input("Enter an adjective of your choosing: ")
            madlibs(noun, pronoun, adjective)
            continue
        else:
            break


def madlibs(noun, pronoun, adjective):
    print(f"""Once there lived a {noun} and his donkey in a village. &
    During the day, {pronoun} donkey would carry the {noun}'s bags. 
    During the night the {noun} would set him free in the field to {adjective} grass. 
    However, the donkey would sneak into nearby farms &
    and {adjective} the fresh vegetables there.""")


play()
