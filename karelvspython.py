"""
Karel versus Python!

The player steps into Karel's shoes, and ventures out into a whole new world. In this strange new world, Karel faces an enormous, venomous python. Karel can fight off the python by throwing beeper bombs, building walls out of beepers, and by digging up beepers from the ground. The python randomly chooses its attacks, so Karel needs to balance digging for beepers with her more offensive strategies.
"""

import random

# Setting Karel's basic statts
KAREL_AMOUNT_BEEPERS = 100
KAREL_BOMB_BEEPERS = 15
KAREL_BOMB_HP = 15
KAREL_WALL_BEEPERS = 10
KAREL_WALL_HP = 5
KAREL_DIG_MIN = 0 
KAREL_DIG_MAX = 20


# Setting all the constants the python will need
PYTHON_INIT_HEALTH = 100
PYTHON_BITE_MIN = 1
PYTHON_BITE_MAX = 15
PYTHON_BITE_CHANCE = .20
PYTHON_STRANGLE_MIN = 5
PYTHON_STRANGLE_MAX = 10
PYTHON_STRANGLE_CHANCE = .40
PYTHON_STATES = ["healthy", "slightly wounded", "getting weaker", "near defeat"]

def main():
    # Initializing Karel and the python's health and state
    karel_health = KAREL_AMOUNT_BEEPERS
    python_health = PYTHON_INIT_HEALTH
    python_state = PYTHON_STATES[0]
    karel_defending = False

    print("It's a beautiful sunny day, and Karel is enjoying a well-deserved day off from Code in Place.")
    print("\n'A perfect day for a walk!', Karel says to herself. So she turns left, turns left, and turns left again, all the way around the block.")
    print("\nOn the way back to her house, though, Karel notices a hole in one of the walls. 'How strange!', Karel thinks. Curious as Karel is, she walks towards the hole in the wall, and steps through it.")
    print("\nAll of a sudden, Karel finds herself in a new world, facing a giant python! The python hisses angrily, and shows off its venomous fangs.")
    while (karel_health > 0) and (python_health > 0):
        # Karel gets the first move. She can choose between 3 options
        print("\nYou have " + str(karel_health) + " beepers! The python has " +str(python_health) + " hp.")
        pick_move = int(input("\nWhat do you do? [1] Throw bomb, [2] Build a wall, [3] Mine beepers: "))
        while not input_is_valid(pick_move):
            pick_move = int(input("Oops, something went wrong. Try again! Choose 1, 2, or 3: "))
        print("")

        # Determine the impact on Karel's amount of beepers and the python's health
        if pick_move == 1:
            print("Karel quickly throws a bomb made out of " + str(KAREL_BOMB_BEEPERS) + " beepers at the python.")
            karel_health -= KAREL_BOMB_BEEPERS
            python_health -=KAREL_BOMB_HP
            print("The python recoils. It looses " + str(KAREL_BOMB_HP) + " hp!")
        elif pick_move == 2:
            print("Karel builds a wall made out of " + str(KAREL_WALL_BEEPERS) + " beepers, and hides behind it.")
            karel_health -= KAREL_WALL_BEEPERS
            python_health -= KAREL_WALL_HP
            karel_defending = True
            print("The python looks confused, but angry!")
        else:
            digged_up_beepers = random.randint(KAREL_DIG_MIN, KAREL_DIG_MAX)
            karel_health += digged_up_beepers
            print("Karel starts digging for beepers and finds " + str(digged_up_beepers) + " beepers.")
            if digged_up_beepers == 0:
                print("Bummer!")
            python_state = set_python_state(python_health)
        python_state = set_python_state(python_health)
        print("The python is " + str(python_state) + ".")
        print("")
        # Now it's time for the python to attack. Determine the impact on Karel's amount of beepers after the attack
        if python_health > 0:
            karel_health -= python_attack(karel_defending)
        karel_defending = False    
    if karel_health > 0:
        print("Karel has defeated the python! She can now go back to her own world, and enjoy the rest of her day off in peace.")    
    elif python_health > 0:
        print("Karel has no more beepers left. \nGAME OVER!")
    else:
        print("Somehow, Karel and the python have defeated each other. Now what?")

def python_attack(karel_defending):
    random_move = random.random()
    # The python attacks with a venomous bite
    if random_move < PYTHON_BITE_CHANCE:
        if karel_defending:
            print("\nThe python strikes to bite Karel, but hit the wall of beepers Karel has build.")
            return 0
        else:
            damage = random.randint(PYTHON_BITE_MIN, PYTHON_BITE_MAX)
            print("\nThe python strikes to bite Karel, causing Karel to loose " + str(damage) + " beepers.")
            return damage
    # The python strangles Karel
    elif random_move < PYTHON_STRANGLE_CHANCE:
        if karel_defending:
            print("\nThe python swiftly slithers towards Karel to strangle her, but is blocked by the wall of beepers.")
            return 0
        else: 
            damage = random.randint(PYTHON_STRANGLE_MIN, PYTHON_STRANGLE_MAX)
            print("\nThe python swiftly slithers towards Karel to strangle her, and squeezes " + str(damage) + " beepers out of Karel.")
            return damage
    # The python does nothing that damages Karel
    else:
        print("The python hisses furiously! But nothing happens")
        return 0

def set_python_state(python_health):
    if python_health > (PYTHON_INIT_HEALTH * .75):
        return PYTHON_STATES[0]
    elif python_health > (PYTHON_INIT_HEALTH * .5):
        return PYTHON_STATES[1]
    elif python_health > (PYTHON_INIT_HEALTH * .25):
        return PYTHON_STATES[2]
    else:
        return PYTHON_STATES[3]


# Make sure player only choses a valid number (1, 2 or 3)
def input_is_valid(pick_move):
    if 0 < pick_move < 4:
        return True
    else:
        return False



if __name__ == "__main__":
    main()