#Vincent Johnson, Battle Simulator
'''
Character Creation and Management:

Create new characters with attributes (name, health, strength, defense, speed)
    Save characters to a CSV file
    Load characters from a CSV file
    Display character information

Battle System:
    Implement a turn-based battle system between two characters
    Calculate damage based on character attributes
    Include a simple leveling system where characters gain experience after battles

Program Structure:
    Use inner functions for main features (character creation, battle system, menu)
    Implement helper functions for repetitive tasks (save/load, display character info)
    Create a main menu for user interaction

File Operations:
    Save character data to a CSV file
    Load character data from a CSV file

Additional Features (Optional): (NOTE: only awarded IF all 20 of the required points are earned, they cannot make up for lost points)

    Implement character classes (warrior, mage, rogue) with unique attributes 
    Implementation of basic character classes (e.g. warrior, mage, rouge) with slight variations in starting attributes (1 point)
    Implement character classes with unique abilities or skills (2 points)
    Add a simple inventory system 
    Allow characters to hold items (1 point)
    Inventory with equippable items that affect character stats (2 points)
    Advanced inventory system with item crafting or combining (3 points)
    Create special abilities for characters
    Implement one or two special abelites for characters (1 point)
    Implement a diverse set of special abilities that significantly impact battles (2 points)
    Enhanced Battle System
    Add status effects (e.g. poison, stun, frozen) to the battle system
    Implement a more complex battle system with multiple characters per side (3 points)
'''
import csv
from games import game


def main(repeat):
    ans = input('''What would you like to do?
    Play game (1)
    Make profile (2)
''')
    try:
        ans = int(ans)
    except:
        main(repeat)

    if ans == 1:
        game()
    elif ans == 2:
        mke_prfl()
    else:
        repeat = 0
    return repeat
if __name__ == "__main__":
    repeat = 1
    while repeat > 0:
        main(repeat)