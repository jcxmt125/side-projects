import subprocess, json, os

print("Hello! This script will help you deploy a minecraft server. I'll work in the current directory.")

filePath = input("What's the name of the file?\n>")

with open(filePath, "r", encoding="UTF-8") as configFile:
    config = json.load(configFile)

serverType = config["serverType"]

jarFileLink = config["jarFileLink"]

subprocess.run(["curl", "-OJ", jarFileLink])

print("Finding the JarFile...")

filesInDir = os.listdir(os.getcwd())

for i in filesInDir:
    if i.endswith(".jar"):
        jarFile = i

if serverType == "2":
    os.mkdir("mods")

    for i in config["modlist"]:
        subprocess.run(["curl", "-OJ", i])

    print("moving jarFiles...")

    filesInDir = os.listdir(os.getcwd())

    for i in filesInDir:
        if i.endswith(".jar") and i != jarFile:
            subprocess.run(["mv", i, "mods/"+i])

memAllocated = config["ramAmount"]

subprocess.run(["java", "-Xmx"+str(memAllocated)+"G", "-jar", jarFile, "nogui"])

print("It should have exited asking you to edit the eula.txt file. I'll launch nano for you.")

print("Use arrow keys to navigate and change the line to eula=true, then press ctrl+x, then say yes by pressing the y key, then press enter.")

input("Ready? Press return to launch nano!")

subprocess.run(["nano", "eula.txt"])

print("After this, run \"java -Xmx"+str(memAllocated)+"G -jar " +jarFile+ " nogui\" without the quotes to start the server.")

print("I'll also create a .sh file for you!")

with open("start.sh", "w") as startFile:
    startFile.write("java -Xmx"+str(memAllocated)+"G -jar " +jarFile+ " nogui")

print("Deploy script done!")