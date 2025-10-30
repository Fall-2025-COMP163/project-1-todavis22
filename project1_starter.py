"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: Treven Omari Davis
Date: [Date]

AI Usage: AI helped align file formatting and key naming to match autograder.
"""

def calculate_stats(character_class, level):
    # i used .lower because python and csae sesntive and if the use my type in all caps
    # it automatically make it loer so the program won't crash
    #use if statements to calculate the per level basically if level was 2 it level up the strength by 2 * 2 + 5 = 9
    character_class = character_class.lower()

    if character_class == "mage":
        strength = 5 + (level * 2)
        magic = 15 + (level * 3)
        health = 80 + (level * 5)
    elif character_class == "warrior":
        strength = 15 + (level * 4)
        magic = 5 + (level * 2)
        health = 90 + (level * 6)
    elif character_class == "cleric":
        strength = 8 + (level * 3)
        magic = 12 + (level * 4)
        health = 85 + (level * 5)
    elif character_class == "rogue":
        strength = 10 + (level * 3)
        magic = 10 + (level * 3)
        health = 75 + (level * 4)
    else:
        strength = 5 + (level * 2)
        magic = 5 + (level * 2)
        health = 70 + (level * 3)

    return strength, magic, health


def create_character(name, character_class):
    # started off at level by defaault 
    #changing later but gold is hardcoded at 100
    # i acces my stats from calculate stats
    #made a dictionary to assign my keys names to the acutally use value
    #chat told me to use level = 1 at the beginning
    level = 1
    stat = calculate_stats(character_class, level)
    gold = 100

    strength = stat[0]
    magic = stat[1]
    health = stat[2]

    new_character = {
        "name": name,
        "class": character_class,
        "level": level,
        "magic": magic,
        "strength": strength,
        "health": health,
        "gold": gold
    }
    return new_character


def save_character(character, filename):
    # saves the character but first checks to see if the keys are fiund
    #oopens file writes in it then closes it the return true
    #I understand it but chat helped me check the keys in the list
    # Chat told me to check for keys in the dictionaty
    keys = ["name", "class", "level", "strength", "magic", "health", "gold"]
    for key in keys:
        if key not in character:
            return False

    # changed the output format to match autograder exactly
    with open(filename, "w") as file:
        file.write(f"Name: {character['name']}\n")
        file.write(f"Class: {character['class']}\n")
        file.write(f"Level: {character['level']}\n")
        file.write(f"Strength: {character['strength']}\n")
        file.write(f"Magic: {character['magic']}\n")
        file.write(f"Health: {character['health']}\n")
        file.write(f"Gold: {character['gold']}\n")

    return True


def load_character(filename):
    #this function is loading our character basically using import os is letting us acces our loaded data file
    # the if statement checks if it exist and if not return none
    # the with statement open my file and reads it after then it strips the white spaces
    #Then it splits my key and values using the colon 
    #uses indexs to assign it
    #import os chat help me out with that
    import os
    if not os.path.exists(filename):
        return None

    character = {}
    with open(filename, "r") as file:
        for line in file:
            if ":" not in line:
                continue
            cleanWhites = line.strip()
            splitValnKey = cleanWhites.split(":")
            key = splitValnKey[0].lower().strip()
            value = splitValnKey[1].strip()

            if key in ["level", "strength", "magic", "health", "gold"]:
                value = int(value)

            character[key] = value

    return character


def display_character(character):
    # displays the results
    print("=== CHARACTER SHEET ===")
    print(f"Name: {character['name']}")
    print(f"Class: {character['class']}")
    print(f"Level: {character['level']}")
    print(f"Strength: {character['strength']}")
    print(f"Magic: {character['magic']}")
    print(f"Health: {character['health']}")
    print(f"Gold: {character['gold']}")


def level_up(character):
    #This is the levelup funcction basicallu its getting the the stats from my tuple,
    # I index it to assign it to the value in my tuple
    character["level"] += 1

    stats = calculate_stats(character["class"], character["level"])
    character["strength"] = stats[0]
    character["magic"] = stats[1]
    character["health"] = stats[2]

if __name__ == "__main__":
    print("=== CHARACTER CREATOR ===")
    print("Test your functions here!")
    
    char = create_character("Test", "Mage")
    display_character(char)
    save_character(char, "my_character.txt")
    loaded = load_character("my_character.txt")

    print("Loaded Character:")
    display_character(loaded)
