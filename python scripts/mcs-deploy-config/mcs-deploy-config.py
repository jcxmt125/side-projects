import subprocess, json, os

print("Hello! This script will help you deploy a minecraft server. I'll work in the current directory.")

subprocess.run(["ls"])

filePath = input("What's the name of the config file?\n>")

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

if int(serverType) == 2:
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

subprocess.run(["cat", "eula.txt"])

input("You're about to agree to the EULA. Please retrun to allow this script to do so on behalf of you.")

with open("eula.txt", "r") as eulaFile:
    eula = eulaFile.readlines()

eula[2] = "eula=true\n"

with open("eula.txt", "w") as eulaFile:
    eulaFile.writelines(eula)

print("After this, run \"java -Xmx"+str(memAllocated)+"G -jar " +jarFile+ " nogui\" without the quotes to start the server.")

print("I'll also create a .sh file for you! Run source start.sh to use that instead.")

with open("start.sh", "w") as startFile:
    startFile.write("java -Xmx"+str(memAllocated)+"G -jar " +jarFile+ " nogui")

print("Deploy script done!")