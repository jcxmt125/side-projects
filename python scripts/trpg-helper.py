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
        
        dependancyCode = ["strength","dexterity","constitution","intelligence","wisdom","charisma"][int(skilldependancy)]

        skilldesc = input("Skill description: ")

        print("You may leave the following fields empty!")

        skillfail = input("On fail: ")

        if skillfail == "":
            skillfail = "Fail!"

        skillmodsuccess = input("On regular success: ")

        if skillmodsuccess == "":
            skillmodsuccess = "Success!"

        skillsuccess = input("On skill critical success: ")

        if skillsuccess == "":
            skillsuccess = "Critical success!"

        assembledSkill = {
            "name":skillname,
            "depend":dependancyCode,
            "description":skilldesc,
            "actions":[skillfail,skillmodsuccess,skillsuccess]
        }  

        skills.append(assembledSkill)



    with open(input("File name to save to: ")+".json","w",encoding="UTF-8") as f:
        
        charFile = {
            "name":character_name,
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
            "skills":skills,
            "effects":{
                "stats":{
                    "strength":0,
                    "dexterity":0,
                    "constitution":0,
                    "intelligence":0,
                    "wisdom":0,
                    "charisma":0
                },
                "other":[]
            }
        }

        json.dump(charFile, f, indent=2)

def fix_partial_charfile(charFileName):
    with open(charFileName, "r", encoding="UTF-8") as charFile:
        character = json.load(charFile)
    
    if not ("name" in character):
        character["name"] = input("Input character name: ")

    if not ("stats" in character):
        stats = {
            "strength":int(input("Input strength: ")),
            "dexterity":int(input("Input dexterity: ")),
            "constitution":int(input("Input constitution: ")),
            "intelligence":int(input("Input intelligence: ")),
            "wisdom":int(input("Input wisdom: ")),
            "charisma":int(input("Input charisma: "))
        }
        character["stats"] = stats

    if not ("max_hp" in character):
        character["max_hp"] = character["stats"]["constitution"] + 8

    with open(charFileName, "w", encoding="UTF-8") as charFile:
        json.dump(character,charFile,indent=2)

def modify_stats_interactive(charFileName):
    with open(charFileName, "r", encoding="UTF-8") as charFile:
        character = json.load(charFile)
    
    print(character["stats"])

    modifyTarget = input("What to modify: ")

    modifyValue = int(input("Modify value to: "))

    character["stats"][modifyTarget] = modifyValue

    print("Modified "+modifyTarget+" to "+str(modifyValue)+", resulting in delta of "+str(stat_to_delta(modifyValue)))

    with open(charFileName, "w", encoding="UTF-8") as charFile:
        json.dump(character,charFile,indent=2)

#Item: name, desc, units, unitweight

def modify_misc_inventory_interactive(charFileName):
    with open(charFileName, "r", encoding="UTF-8") as charFile:
        character = json.load(charFile)
    
    inventory = character["inventory"]["other"]

    for i in range(len(inventory)):
        print(str(i)+". "+inventory[0])
    
    modifyTarget = input("Input item number to modify, or return to add item!")

    if modifyTarget == "":
        itemName = input("Input item name: ")
        itemDesc = input("Input item description: ")
        itemUnits = int(input("Input number of items: "))
        itemUnitWeight = int(input("Input unit weight of item: "))

        assembledItem = [itemName,itemDesc,itemUnits,itemUnitWeight]

        character["current_carry"] += itemUnits*itemUnitWeight

        inventory.append(assembledItem)

    else:
        modifyTarget = int(modifyTarget)

        itemLoad = inventory[modifyTarget]

        itemName = itemLoad[0]
        itemDesc = itemLoad[1]

        print(itemName+": "+itemDesc)

        itemUnits = itemLoad[2]
        itemUnitWeight = itemLoad[3]

        character["current_carry"] -= itemUnits*itemUnitWeight
        
        delta_units = int(input("Item number to increment: "))

        itemUnits += delta_units

        if itemUnits == 0:
            del inventory[modifyTarget]
            
            print("Item removed from inventory")
        else:
            character["current_carry"] += itemUnits*itemUnitWeight

        

    with open(charFileName, "w", encoding="UTF-8") as charFile:
        json.dump(character,charFile,indent=2)

def use_skill_interactive(charFileName):
    with open(charFileName, "r", encoding="UTF-8") as charFile:
        character = json.load(charFile)

    skillList = character["skills"]

    for i in range(len(skillList)):
        print(str(i) + ". " + skillList[i]["name"])
    
    skillIndex = int(input("Skill to use: "))

    selectedSkill = skillList[skillIndex]

    rollResult = input("Input roll result or return to roll: ")

    if rollResult == "":
        rollResult = roll_dice_from_notation("d12")
        print("Result of roll: "+str(rollResult))
    
    rollResult = int(rollResult)

    finalRoll = rollResult + stat_to_delta(character["stats"][selectedSkill["depend"]]) + character["effects"]["stats"][selectedSkill["depend"]]

    print("Final Roll " + str(finalRoll))

    if finalRoll <6:
        print(selectedSkill["actions"][0])
    elif finalRoll <10:
        print(selectedSkill["actions"][1])
    else:
        print(selectedSkill["actions"][2])

def apply_effect_interactive(charFileName):
    with open(charFileName, "r", encoding="UTF-8") as charFile:
        character = json.load(charFile)

    with open(charFileName, "w", encoding="UTF-8") as charFile:
        json.dump(character,charFile,indent=2)
    
def add_skill_interactive(charFileName):
    with open(charFileName, "r", encoding="UTF-8") as charFile:
        character = json.load(charFile)
    
    with open(charFileName, "w", encoding="UTF-8") as charFile:
        json.dump(character,charFile,indent=2)

if __name__ == "__main__":
    fileLoc = input("Drag file here: ")

    while True:

        use_skill_interactive(fileLoc)