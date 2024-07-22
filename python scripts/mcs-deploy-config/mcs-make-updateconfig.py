import json

modlist = []

print("This script will make an update config file! Make sure you've tested them before you deploy.")

while True:

    modLink = input("Paste mod link here: ")

    if modLink == "":
        break

    modlist.append(modLink)

with open(input("Input file name (without the .json!): ")+".json", "w", encoding="UTF-8") as configFile:
    json.dump({"modlist": modlist}, configFile, indent=2)