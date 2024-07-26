import json

modlist = []

print("This script will make an update config file! Make sure you've tested them before you deploy.")
print("Return an empty line to finish.")

while True:

    modLink = input("Paste mod link here: ")

    if "forge" in modLink:
            print("Wait, are you sure this is a Fabric mod?")

            modConfirm = input("Return empty if you want to add, or input anything else to cancel: ")

            if modConfirm != "":
                continue

    if not modLink.endswith(".jar"):
            print("Wait, are you sure this is a direct download link to the mod?")

            modConfirm = input("This URL should immediately download the mod. Press enter to add, or input anything else to cancel: ")

            if modConfirm != "":
                continue

    if modLink == "":
        break

    modlist.append(modLink)

with open(input("Input file name (without the .json!): ")+".json", "w", encoding="UTF-8") as configFile:
    json.dump({"modlist": modlist}, configFile, indent=2)