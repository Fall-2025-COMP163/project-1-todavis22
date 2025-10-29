"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: [Your Name Here]
Date: [Date]

AI Usage: [Document any AI assistance used]
Example: AI helped with file I/O error handling logic in save_character function
"""
def calculate_stats(character_class, level):
    
    character_class = character_class.lower()
    

    if character_class == "mage":
        strength = 3 + 2*level   
        magic    = 11 + 4*level   
        health   = 77 + 3*level   

    elif character_class == "warrior":
        
        strength = 11 + 4*level 
        magic    = 3 + 2*level
        health   = 80 + 4*level   

    elif character_class == "cleric":
        strength = 5 + 2*level
        magic    = 11 + 4*level
        health   = 85 + 4*level

    elif character_class == "rogue":
        strength = 8 + 3*level
        magic    = 8 + 3*level
        health   = 60 + 2*level

    else:
        strength = 5 + 2*level
        magic    = 5 + 2*level
        health   = 70 + 3*level

    return strength, magic, health

    

def create_character(name, character_class):
    level = 1
    stat = calculate_stats(character_class, level)
    gold = 100

    strength = stat[0]
    magic = stat[1]
    health = stat[2]


    new_character = {
        "Name":name,
        "Class":character_class,
        "Level":level,
        "Magic":magic,
        "Strength":strength,
        "Health":health,
        "Gold": gold
    }

    new_character["name"] = new_character["Name"]
    new_character["class"] = new_character["Class"]
    new_character["level"] = new_character["Level"]
    new_character["magic"] = new_character["Magic"]
    new_character["strength"] = new_character["Strength"]
    new_character["health"] = new_character["Health"]
    new_character["gold"] = new_character["Gold"]

    return new_character
    """
    Creates a new character dictionary with calculated stats
    Returns: dictionary with keys: name, class, level, strength, magic, health, gold
    
    Example:
    char = create_character("Aria", "Mage")
    # Should return: {"name": "Aria", "class": "Mage", "level": 1, "strength": 5, "magic": 15, "health": 80, "gold": 100}
    """
    # TODO: Implement this function
    # Remember to use calculate_stats() function for stat calculation
  



def save_character(character, filename):

    keys = ["Name", "Class", "Level", "Magic", "Strength", "Health", "Gold"]
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
    """
    Saves character to text file in specific format
    Returns: True if successful, False if error occurred
    
    Required file format:
    Character Name: [name]
    Class: [class]
    Level: [level]
    Strength: [strength]
    Magic: [magic]
    Health: [health]
    Gold: [gold]
    """
    # TODO: Implement this function
    # Remember to handle file errors gracefully
    

def load_character(filename):

 
    character = {}

    with open(filename, "r") as f:
        for line in f:
            cleanWhites = line.strip()
            splitValnKey = cleanWhites.split(":")
            
            key = splitValnKey[0]
            value = splitValnKey[1].strip()

            if key in ["Level", "Strength", "Magic", "Health", "Gold"]:
                value = int(value)

      
            if key == "Character Name":
                key = "Name"

            character[key] = value

            if key == "Name":      character["name"] = value
            if key == "Class":     character["class"] = value
            if key == "Level":     character["level"] = value
            if key == "Magic":     character["magic"] = value
            if key == "Strength":  character["strength"] = value
            if key == "Health":    character["health"] = value
            if key == "Gold":      character["gold"] = value
    return character
    """
    Loads character from text file
    Returns: character dictionary if successful, None if file not found
    """
    # TODO: Implement this function
    # Remember to handle file not found errors
    

def display_character(character):

    print("=== CHARACTER SHEET ===")
    print(f"Name: {character['Name']}")
    print(f"Class: {character['Class']}")
    print(f"Level: {character['Level']}")
    print(f"Strength: {character['Strength']}")
    print(f"Magic: {character['Magic']}")
    print(f"Health: {character['Health']}")
    print(f"Gold: {character['Gold']}")
    """
    Prints formatted character sheet
    Returns: None (prints to console)
    
    Example output:
    === CHARACTER SHEET ===
    Name: Aria
    Class: Mage
    Level: 1
    Strength: 5
    Magic: 15
    Health: 80
    Gold: 100
    """
    # TODO: Implement this function
    

def level_up(character):
    character["Level"] += 1

    stats = calculate_stats(character["Class"], character["Level"])
    
    strength = stats[0]
    magic = stats[1]
    health = stats[2]

    character["Strength"] = strength
    character["Magic"] = magic
    character["Health"] = health

    character["level"] = character["Level"]
    character["strength"] = character["Strength"]
    character["magic"] = character["Magic"]
    character["health"] = character["Health"]

    """
    Increases character level and recalculates stats
    Modifies the character dictionary directly
    Returns: None
    """
    # TODO: Implement this function
    # Remember to recalculate stats for the new level
    

# Main program area (optional - for testing your functions)
if __name__ == "__main__":
    print("=== CHARACTER CREATOR ===")
    print("Test your functions here!")
    
    # Example usage:
    # char = create_character("TestHero", "Warrior")
    # display_character(char)
    # save_character(char, "my_character.txt")
    # loaded = load_character("my_character.txt")
