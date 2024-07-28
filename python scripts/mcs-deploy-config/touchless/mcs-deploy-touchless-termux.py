import subprocess, json, os

print("Starting touchless deploy for aarch64 termux...")

tlconfigLink = "https://raw.githubusercontent.com/jcxmt125/side-projects/main/python%20scripts/mcs-deploy-config/touchless/touchless-config-termux.json"

subprocess.run(["curl", "-OJ", tlconfigLink])



filePath = "touchless-config-oracle-aarch.json"

with open(filePath, "r", encoding="UTF-8") as configFile:
    config = json.load(configFile)

serverType = config["serverType"]

jarFileLink = config["jarFileLink"]

javaName = config["javaName"]

print("Downloading Java...")

subprocess.run(["curl", "-OJ", javaName])

print("Finding and extracting Java...")

filesInDir = os.listdir(os.getcwd())

for i in filesInDir:
    if i.endswith(".tar.gz"):
        compressedFile = i
        break

subprocess.run(["tar", "-xvf", compressedFile])

filesInDir = os.listdir(os.getcwd())

for i in filesInDir:
    if i.startswith("jdk-"):
        javapath = i+"/bin/"+"java"
        break

subprocess.run(["free", "-h"])

print("Please input the amount of RAM to assign to the Minecraft server.")

memAllocated = input("RAM in GBs (int)> ")

subprocess.run(["curl", "-OJ", jarFileLink])

filesInDir = os.listdir(os.getcwd())

for i in filesInDir:
    if i.endswith(".jar"):
        jarFile = i
        break

if int(serverType) == 2:
    os.mkdir("mods")

    for i in config["modlist"]:
        subprocess.run(["curl", "-OJ", i])

    filesInDir = os.listdir(os.getcwd())

    for i in filesInDir:
        if i.endswith(".jar") and i != jarFile:
            subprocess.run(["mv", i, "mods/"+i])

memAllocated = config["ramAmount"]

subprocess.run([javapath, "-Xmx"+str(memAllocated)+"G", "-jar", jarFile, "nogui"])

with open("eula.txt", "r") as eulaFile:
    eula = eulaFile.readlines()

eula[2] = "eula=true\n"

with open("eula.txt", "w") as eulaFile:
    eulaFile.writelines(eula)

print("I'll create a .sh file to launch your server. Run source start.sh to launch.")

with open("start.sh", "w") as startFile:
    startFile.write(javapath+" -Xmx"+str(memAllocated)+"G -jar " +jarFile+ " nogui")

print("Complete! However, this doesn't configure whitelisting, which is highly recommended. Please do that asap after deployment!")