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
    # saves the character but first checks to see if the keys are fiund
    #oopens file writes in it then closes it the return true
    #I understand it but chat helped me check the keys in the list
    # Chat told me to check for keys in the dictionaty
    keys = ["name", "class", "level", "strength", "magic", "health", "gold"]
    for key in keys:
        if key not in character:
            return False

    file = open(filename, "w")
    file.write(f"Character Name: {character['name']}\n")
    file.write(f"Class: {character['class']}\n")
    file.write(f"Level: {character['level']}\n")
    file.write(f"Strength: {character['strength']}\n")
    file.write(f"Magic: {character['magic']}\n")
    file.write(f"Health: {character['health']}\n")
    file.write(f"Gold: {character['gold']}\n")
    file.close()
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
            cleanWhites = line.strip()
            splitValnKey = cleanWhites.split(":")
            key = splitValnKey[0]
            value = splitValnKey[1].strip()
        # Chat told me to do this but basically what chat is saying is that when i write it as a file
        # it says character name but theres no such thing as character name in my dictionary so
        # basically its saying when you see this just store it ini the name dictionary6
            if key == "Character Name":
                key = "Name"

            if key in ["level", "strength", "magic", "health", "gold"]:
                value = int(value)

            character[key] = value

    #lowercase the program just incase they did lower or higher so the program dont crash chat told me to do this
    character["name"] = character["Name"]
    character["class"] = character["Class"]
    character["level"] = character["Level"]
    character["strength"] = character["Strength"]
    character["magic"] = character["Magic"]
    character["health"] = character["Health"]
    character["gold"]  = character["Gold"]

    return character




def display_character(character):
    # displays the results
    print("=== CHARACTER SHEET ===")
    print(f"Name: {character['Name']}")
    print(f"Class: {character['Class']}")
    print(f"Level: {character['Level']}")
    print(f"Strength: {character['Strength']}")
    print(f"Magic: {character['Magic']}")
    print(f"Health: {character['Health']}")
    print(f"Gold: {character['Gold']}")


def level_up(character):
    #This is the levelup funcction basicallu its getting the the stats from my tuple,
    # I index it to assign it to the value in my tuple
    character["level"] += 1

    stats = calculate_stats(character["class"], character["level"])
    character["strength"] = stats[0]
    character["magic"] = stats[1]
    character["health"] = stats[2]

    # lowercase incase for bugs so the program dosent crash chat told me to do it
    character["level"] = character["Level"]
    character["strength"] = character["Strength"]
    character["magic"] = character["Magic"]
    character["health"] = character["Health"]

if __name__ == "__main__":
    print("=== CHARACTER CREATOR ===")
    print("Test your functions here!")
    
    char = create_character("Test", "Mage")
    display_character(char)
    save_character(char, "my_character.txt")
    loaded = load_character("my_character.txt")

    print("Loaded Character:")
    display_character(loaded)
    # Example usage:
    # char = create_character("TestHero", "Warrior")
    # display_character(char)
    # save_character(char, "my_character.txt")
    # loaded = load_character("my_character.txt")
