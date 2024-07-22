import subprocess, os, json, shutil
from pathlib import Path

print("This script will delete everything in the mods folder, and replace it with the mods in the config file.")

print("It's compatible with the deploy config file, as well as an update-only (small) config file.")

input("Return to continue or Ctrl+C (KeyboardInturrupt) to cancel")

filePath = input("Name of config file: ")

with open(filePath, "r", encoding="UTF-8") as configFile:
    config = json.load(configFile)

shutil.rmtree(Path("mods"))

os.mkdir("mods")

filesInDir = os.listdir(os.getcwd())

for i in filesInDir:
    if i.endswith(".jar"):
        jarFile = i
        break

for i in config["modlist"]:
    subprocess.run(["curl", "-OJ", i])

print("moving jarFiles...")

filesInDir = os.listdir(os.getcwd())

for i in filesInDir:
    if i.endswith(".jar") and i != jarFile:
        subprocess.run(["mv", i, "mods/"+i])

print("Done! Re-execute server when ready.")