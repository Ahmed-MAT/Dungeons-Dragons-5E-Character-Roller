import random

def get_input(prompt = "??"):
    result = input(prompt)
    return result

def get_int(prompt = "??"):
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

def generate_character(x = None):
    while not x == 3 and not x == 4:
        x = get_int("How many d6's do you want to roll? 3 or 4? ")

    rolls = []
    sets = []

    if x == 3:
        for i in range(3):
            for i in range(6):
                total = 0
                for e in range(3):
                    roll = random.randint(1, 6)
                    if roll == 1:
                        roll = random.randint(1, 6)
                    total = total + roll
                rolls.append(total)
            sets.append(rolls)
            rolls = []
        return sets
    if x == 4:
        for i in range(3):
            for i in range(6):
                total = 0
                elimination = []
                for e in range(4):
                    roll = random.randint(1, 6)
                    if roll == 1:
                        roll = random.randint(1, 6)
                    elimination.append(roll)
                elimination.sort()
                elimination.pop(0)
                for i in range(len(elimination)):
                    total = total + elimination[i]
                rolls.append(total)
            sets.append(rolls)
            rolls = []
        return sets

def generate_characters():
    print(generate_character())
    go_again = get_int("Do you want to generate another? 1 = Yes, 2 = No ")
    valid_inputs = [1, 2]

    while go_again not in valid_inputs:
        print("Please input 1 or 2")
        go_again = get_int("Do you want to generate another? 1 = Yes, 2 = No ")

    while go_again == 1:
        print(generate_character())
        go_again = get_int("Do you want to generate another? 1 = Yes, 2 = No ")

    if go_again == 2:
        farewell = "Goodbye!"
        return farewell

if __name__ == '__main__':
    print(generate_characters())
