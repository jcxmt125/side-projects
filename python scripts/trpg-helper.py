import json

#This script is a WIP!

def stat_to_delta(statvalue):
    if statvalue <= 3:
        return -3
    elif statvalue <= 5:
        return -2
    elif statvalue <= 8:
        return -1
    elif statvalue <= 12:
        return 0
    elif statvalue <= 15:
        return 1
    elif statvalue <= 17:
        return 2
    else:
        return 3
    
def roll_dice_from_notation(dice_notation):
    notation_list = dice_notation.split()

    

def make_savefile_cleric_interactive():
    character_name = input("What is the name of the character? ")
    
    stats = {
        "strength":int(input("Input strength: ")),
        "dexterity":int(input("Input dexterity: ")),
        "constitution":int(input("Input constitution: ")),
        "intelligence":int(input("Input intelligence: ")),
        "wisdom":int(input("Input wisdom: ")),
        "charisma":int(input("Input charisma: "))
    }
    
    max_hp = stats["constitution"] + 8
    
    base_attack = input("Input base attack in standard dice notation (ex. d4, d5 + 2, ...): ")

    max_carry = 10 + stat_to_delta(stats["strength"])

    print("Let's start adding the inventory!")

    carry = 0
    
    armor = [input("Armor name: "), int(input("Armor stat modifier: ")), int(input("Weight of armor: ")), input("Any other notes? (NL): ")]

    armor_modifier = armor[1]

    carry += armor[2]

    weapon = [input("Weapon name: "), input("Range of weapon: "), int(input("Weight of weapon: ")), input("Any other notes? (NL): ")]

    carry += weapon[2]

    holy_artifact = [input("Name of the artifact: "), int(input("Weight of artifact: ")), input("Any other notes? (NL): ")]
    
    carry += holy_artifact[1]

    inventory_misc = {}

if __name__ == "__main__":
    make_savefile_cleric_interactive()