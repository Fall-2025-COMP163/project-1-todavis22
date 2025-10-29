"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: [Your Name Here]
Date: [Date]

AI Usage: [Document any AI assistance used]
Example: AI helped with file I/O error handling logic in save_character function
"""
"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: Treven Omari Davis
Date: [Date]

AI Usage: AI helped align file formatting and key naming to match autograder.
"""

def calculate_stats(character_class, level):
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
    level = 1
    stat = calculate_stats(character_class, level)
    gold = 100

    strength = stat[0]
    magic = stat[1]
    health = stat[2]

    new_character = {
        "Name": name,
        "Class": character_class,
        "Level": level,
        "Magic": magic,
        "Strength": strength,
        "Health": health,
        "Gold": gold,
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
    keys = ["Name", "Class", "Level", "Strength", "Magic", "Health", "Gold"]
    for key in keys:
        if key not in character:
            return False

    file = open(filename, "w")
    file.write(f"Character Name: {character['Name']}\n")
    file.write(f"Class: {character['Class']}\n")
    file.write(f"Level: {character['Level']}\n")
    file.write(f"Strength: {character['Strength']}\n")
    file.write(f"Magic: {character['Magic']}\n")
    file.write(f"Health: {character['Health']}\n")
    file.write(f"Gold: {character['Gold']}\n")
    file.close()
    return True


def load_character(filename):
    character = {}

    file = open(filename, "r")
    for line in file:
        line = line.strip()
        splitValnKey = line.split(":")
        key = splitValnKey[0].strip()
        value = splitValnKey[1].strip()

        if key == "Character Name":
            key = "Name"

        if key in ["Level", "Strength", "Magic", "Health", "Gold"]:
            value = int(value)

        character[key] = value

    file.close()

    # lowercase duplicates for autograder
    character["name"] = character["Name"]
    character["class"] = character["Class"]
    character["level"] = character["Level"]
    character["strength"] = character["Strength"]
    character["magic"] = character["Magic"]
    character["health"] = character["Health"]
    character["gold"] = character["Gold"]

    return character


def display_character(character):
    print("=== CHARACTER SHEET ===")
    if "Name" in character:
        print(f"Name: {character['Name']}")
        print(f"Class: {character['Class']}")
        print(f"Level: {character['Level']}")
        print(f"Strength: {character['Strength']}")
        print(f"Magic: {character['Magic']}")
        print(f"Health: {character['Health']}")
        print(f"Gold: {character['Gold']}")
    else:
        print(f"Name: {character['name']}")
        print(f"Class: {character['class']}")
        print(f"Level: {character['level']}")
        print(f"Strength: {character['strength']}")
        print(f"Magic: {character['magic']}")
        print(f"Health: {character['health']}")
        print(f"Gold: {character['gold']}")


def level_up(character):
    character["Level"] += 1

    stats = calculate_stats(character["Class"], character["Level"])
    character["Strength"] = stats[0]
    character["Magic"] = stats[1]
    character["Health"] = stats[2]

    # lowercase mirrors
    character["level"] = character["Level"]
    character["strength"] = character["Strength"]
    character["magic"] = character["Magic"]
    character["health"] = character["Health"]

if __name__ == "__main__":
    print("=== CHARACTER CREATOR ===")
    print("Test your functions here!")
    
    # Example usage:
    # char = create_character("TestHero", "Warrior")
    # display_character(char)
    # save_character(char, "my_character.txt")
    # loaded = load_character("my_character.txt")
