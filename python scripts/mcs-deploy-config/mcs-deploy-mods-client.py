import subprocess, json, os, shutil

from pathlib import Path

print("Hello! This script will help you deploy mods to your minecraft directory.")

print("This script is made for Windows, and won't work on other OSes.\nPlease execute this script in a folder, as it'll download some files.")

print("By continuing and inputting a config file, you agree to your mods folder being backed up and replaced with the contents of the config file.")

filePath = input("Drag and drop the config file here!\n>")

with open(filePath, "r", encoding="UTF-8") as configFile:
    config = json.load(configFile)

for i in config["modlist"]:
    print(i)
    subprocess.run(["curl", "-OJ", i])

if Path.exists(Path(os.getenv("APPDATA") + "\.minecraft\mods")):
    print("backing up current mods...")
    shutil.move(Path(os.getenv("APPDATA") + "\.minecraft\mods"), Path("mods.old"))

print("moving new mod jarFiles...")

filesInDir = os.listdir(os.getcwd())

try:
    os.mkdir(os.getenv("APPDATA") + "\.minecraft\mods")
except:
    print("WARN: mod directory still exists.")

for i in filesInDir:
    if i.endswith(".jar"):
        shutil.move(Path(i), Path(os.getenv("APPDATA") + "\.minecraft\mods\\" + i))

print("Deploy script done!")