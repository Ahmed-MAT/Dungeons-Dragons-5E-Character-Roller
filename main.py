import random

def get_input(prompt="??"):
    result = input(prompt)
    return result

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

def get_num_rolls(num_rolls: int = None):
    prompt = "How many d6's do you want to roll? 3 or 4? "
    while num_rolls != 3 and num_rolls != 4:
        num_rolls = get_int(prompt)
    return num_rolls

def roll_die():
    die = random.randint(1, 6)
    if die == 1:
        die = random.randint(1, 6)
    return die

def generate_character(num_characters: int = 1, num_rolls: int = None, num_sets: int = 3, num_rolls_per_set: int = 6):
   
    if not (num_characters and num_rolls):
        return "Character generation failed"
  
    for character in range(num_characters):
        sets = []
        for i in range(num_sets):
            rolls = []
            for j in range(num_rolls_per_set):
                roll_totals = []
                for k in range(num_rolls):
                    roll = roll_die()
                    roll_totals.append(roll)
                while len(roll_totals) > 3:
                    roll_totals.remove(min(roll_totals))
                rolls.append(sum(roll_totals))
            sets.append(rolls)
        print(sets)
        print()
    return "Character generation complete"


def generate_characters(num_characters: int = None, num_rolls: int = None):
    if not num_characters:
        prompt = "How many characters would you like to generate? "
        num_characters = get_int(prompt)
    if not num_rolls:
        prompt = "How many d6's do you want to roll? 3 or 4? "
        num_rolls = get_int(prompt)
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
