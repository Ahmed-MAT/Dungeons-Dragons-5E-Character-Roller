import random


def get_input(prompt="??"):
    result = input(prompt)
    return result

# Shorten this function by removing the else
# def get_int(prompt="??"):
#     result = get_input(prompt)
#     while result:
#         try:
#             result = int(result)
#         except:
#             print("You must enter an integer.")
#             result = get_input(prompt)
#         else:
#             result = int(result)
#             return result


def get_int(prompt="??"):
    result = None
    while not result:
        try:
            result = get_input(prompt)
            result = int(result)
        except:
            print("You must enter an integer.")
            result = None
    return result


# Add get_num_rolls function
def get_num_rolls(num_rolls: int = None):
    prompt = "How many d6's do you want to roll? 3 or 4? "
    while num_rolls != 3 and num_rolls != 4:
        num_rolls = get_int(prompt)
    return num_rolls


# Add roll_die function
def roll_die():
    die = random.randint(1, 6)
    if die == 1:
        die = random.randint(1, 6)
    return die


# Shorten this function by only using 1 loop
# change variable names to be more clear
# def generate_character(num_characters=1, x=None):
#     num_characters = int(num_characters)
#     while not x == 3 and not x == 4:
#         x = get_int("How many d6's do you want to roll? 3 or 4? ")

#     rolls = []
#     sets = []

#     for character in range(num_characters):
#         if x == 3:
#             for i in range(3):
#                 for e in range(6):
#                     total = 0
#                     for z in range(3):
#                         roll = random.randint(1, 6)
#                         if roll == 1:
#                             roll = random.randint(1, 6)
#                         total = total + roll
#                     rolls.append(total)
#                 sets.append(rolls)
#                 rolls = []
#             print(f"{sets}")
#             sets = []
#         if x == 4:
#             for i in range(3):
#                 for e in range(6):
#                     total = 0
#                     elimination = []
#                     for z in range(4):
#                         roll = random.randint(1, 6)
#                         if roll == 1:
#                             roll = random.randint(1, 6)
#                         elimination.append(roll)
#                     elimination.sort()
#                     elimination.pop(0)
#                     for z in range(len(elimination)):
#                         total = total + elimination[z]
#                     rolls.append(total)
#                 sets.append(rolls)
#                 rolls = []
#             print(f"{sets}")
#             sets = []

#     complete = "Character generation complete."
#     return complete


def generate_character(num_characters: int = 1, num_rolls: int = None, num_sets: int = 3, num_rolls_per_set: int = 6):
    # handle errors
    if not (num_characters and num_rolls):
        return "Character generation failed"
    # num_characters and num_rolls should already be decided at this point
    # don't need seperate loops
    for character in range(num_characters):
        sets = []
        for i in range(num_sets):
            rolls = []
            # convention for nested loop
            for j in range(num_rolls_per_set):
                roll_totals = []
                for k in range(num_rolls):
                    roll = roll_die()
                    roll_totals.append(roll)
                # For 4 rolls, we want to remove the lowest roll
                # For 3 rolls, we roll 3 times
                while len(roll_totals) > 3:
                    roll_totals.remove(min(roll_totals))
                # Just sum up roll_totals and add it
                rolls.append(sum(roll_totals))
            sets.append(rolls)
        print(sets)
    return "Character generation complete"


def generate_characters(num_characters: int = None, num_rolls: int = None):
    if not num_characters:
        prompt = "How many characters would you like to generate? "
        num_characters = get_int(prompt)
    if not num_rolls:
        prompt = "How many d6's do you want to roll? 3 or 4? "
        num_rolls = get_int(prompt)
    print(generate_character(num_characters, num_rolls))
    print(generate_character(num_characters, num_rolls))
    go_again = get_int("Do you want to generate another? 1 = Yes, 2 = No ")
    valid_inputs = [1, 2]

    while go_again not in valid_inputs:
        print("Please input 1 or 2")
        go_again = get_int("Do you want to generate another? 1 = Yes, 2 = No ")

    while go_again == 1:
        print(generate_character(num_characters, num_rolls))
        go_again = get_int("Do you want to generate another? 1 = Yes, 2 = No ")

    if go_again == 2:
        farewell = "Goodbye!"
        return farewell


if __name__ == '__main__':
    print(generate_characters())
