import json

print("Hello! This script will allow you to make a JSON file to preconfigure a minecraft server deployment.")

serverType = int(input("What server type do you want? 1. Vanilla 2. Fabric\nSelect> "))

modlist = []

if serverType == 1:
    print("Please visit https://www.minecraft.net/en-us/download/server and copy the link to the jarfile.")
    jarFileLink = input("When done, please paste here: ")

elif serverType == 2:
    print("Please visit https://fabricmc.net/use/server/ and copy the link to the jarfile.")
    jarFileLink = input("When done, please paste here: ")

    print("Let's add mods now! Make sure you've tested them before you deploy.")
    print("Return an empty line to finish.")

    while True:

        modLink = input("Paste mod link here: ")

        if modLink == "":
            break

        modlist.append(modLink)

ramAmount = int(input("How many gigabytes of RAM do you want? \n>"))

print("We'll dump the current settings to a config file.")

with open(input("Input file name (without the .json!): ")+".json", "w", encoding="UTF-8") as configFile:
    json.dump({"serverType": serverType, "jarFileLink": jarFileLink, "modlist": modlist, "ramAmount": ramAmount}, configFile, indent=2)