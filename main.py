import random

def get_input(prompt="??"):
    result = input(prompt)
    return result

def get_int(prompt="??"):
    result = get_input(prompt)
    while result:
        try:
            result = int(result)
        except:
            print("You must enter an integer.")
            result = get_input(prompt)
        else:
            result = int(result)
            return result

def generate_character(number_of_characters=1, x=None):
    number_of_characters = int(number_of_characters)
    while not x == 3 and not x == 4:
        x = get_int("How many d6's do you want to roll? 3 or 4? ")

    rolls = []
    sets = []

    for character in range(number_of_characters):
        if x == 3:
            for i in range(3):
                for e in range(6):
                    total = 0
                    for z in range(3):
                        roll = random.randint(1, 6)
                        if roll == 1:
                            roll = random.randint(1, 6)
                        total = total + roll
                    rolls.append(total)
                sets.append(rolls)
                rolls = []
            print(f"{sets}")
            sets = []
        if x == 4:
            for i in range(3):
                for e in range(6):
                    total = 0
                    elimination = []
                    for z in range(4):
                        roll = random.randint(1, 6)
                        if roll == 1:
                            roll = random.randint(1, 6)
                        elimination.append(roll)
                    elimination.sort()
                    elimination.pop(0)
                    for z in range(len(elimination)):
                        total = total + elimination[z]
                    rolls.append(total)
                sets.append(rolls)
                rolls = []
            print(f"{sets}")
            sets = []

    complete = "Character generation complete."
    return complete

def generate_characters(number_of_characters=None):
    number_of_characters = number_of_characters
    if not number_of_characters:
        number_of_characters = get_int("How many characters would you like to generate? ")
    print(generate_character(number_of_characters))
    print(generate_character(number_of_characters))
    go_again = get_int("Do you want to generate another? 1 = Yes, 2 = No ")
    valid_inputs = [1, 2]

    while go_again not in valid_inputs:
        print("Please input 1 or 2")
        go_again = get_int("Do you want to generate another? 1 = Yes, 2 = No ")

    while go_again == 1:
        print(generate_character(number_of_characters))
        go_again = get_int("Do you want to generate another? 1 = Yes, 2 = No ")

    if go_again == 2:
        farewell = "Goodbye!"
        return farewell

if __name__ == '__main__':
    print(generate_characters())
