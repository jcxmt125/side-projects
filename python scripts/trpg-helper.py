import json
import random

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

    number_list = []

    for i in notation_list:
        if "d" in i:
            dicevalue = i.split("d")
            if dicevalue[0] == "":
                dicevalue[0] = 1
            
            rollresult = 0

            dicevalue[0] = int(dicevalue[0])

            while dicevalue[0] > 0:
                rollresult += random.randint(1,int(dicevalue[1]))
                dicevalue[0] -= 1

            number_list.append(rollresult)
        else:
            number_list.append(i)
    
    print(number_list)

    result = 0

    symbol = 1

    for i in number_list:
        
        if i == "+":
            symbol = 1
        elif i == "-":
            symbol = 0
        elif symbol:
            result += int(i)
        else:
            result -= int(i)

    return result
        

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
    
    base_attack = input("Input base attack in standard dice notation with spaces! (ex. d4, d5 + 2, ...): ")

    print("Let's start adding the inventory!")
    
    armor = [input("Armor name: "), int(input("Armor stat modifier: ")), int(input("Weight of armor: ")), input("Any other notes? (NL): ")]

    weapon = [input("Weapon name: "), input("Range of weapon: "), int(input("Weight of weapon: ")), input("Any other notes? (NL): ")]

    holy_artifact = [input("Name of the artifact: "), int(input("Weight of artifact: ")), input("Any other notes? (NL): ")]

    money = 0

    food = 5

    equipment = 5

    inventory_misc = []

    #actions

    print("Okay, time to add skills...")

    skills = []

    while True:
        skillname = input("Input skill name: ")

        if skillname == "":
            break

        print("1. STR\n2. DEX\n3. CON\n4. INT\n5. WIS\n6. CHA")

        skilldependancy = input("Input related stat: ")
        skilldesc = input("Skill description: ")

        print("You may leave the following fields empty!")

        skillfail = input("On fail: ")

        skillmodsuccess = input("On regular success: ")

        skillsuccess = input("On skill critical success: ")

        



    with open(input("File name to save to: ")+".json","w",encoding="UTF-8") as f:
        
        charFile = {
            "stats":stats,
            "max_hp":stats["constitution"] + 8,
            "max_carry":10 + stat_to_delta(stats["strength"]),
            "current_carry":armor[2] + weapon[2] + holy_artifact[1] + round(money/100) + round(food/5) + round(equipment/5),
            "base_attack":base_attack,
            "inventory":{
                "weapon":weapon,
                "armor":armor,
                "artifact":holy_artifact,
                "money":money,
                "food":food,
                "equipment":equipment,
                "other":inventory_misc
            },
            "skills":skills
        }

        json.dump(charFile, f)

if __name__ == "__main__":
    #print(roll_dice_from_notation(input("Dice Notation: ")))
    make_savefile_cleric_interactive()