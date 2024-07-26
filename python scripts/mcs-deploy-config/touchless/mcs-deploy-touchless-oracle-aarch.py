import subprocess, json, os

print("Starting touchless deploy for aarch64 oracle...")

tlconfigLink = "https://raw.githubusercontent.com/jcxmt125/side-projects/main/python%20scripts/mcs-deploy-config/touchless/touchless-config-oracle-aarch.json"

subprocess.run(["curl", "-OJ", tlconfigLink])

filePath = "touchless-config-oracle-aarch.json"

with open(filePath, "r", encoding="UTF-8") as configFile:
    config = json.load(configFile)

serverType = config["serverType"]

jarFileLink = config["jarFileLink"]

javaName = config["javaName"]

subprocess.run(["sudo", "yum", "install", "-y", javaName])

subprocess.run(["curl", "-OJ", jarFileLink])

filesInDir = os.listdir(os.getcwd())

for i in filesInDir:
    if i.endswith(".jar"):
        jarFile = i

if int(serverType) == 2:
    os.mkdir("mods")

    for i in config["modlist"]:
        subprocess.run(["curl", "-OJ", i])

    filesInDir = os.listdir(os.getcwd())

    for i in filesInDir:
        if i.endswith(".jar") and i != jarFile:
            subprocess.run(["mv", i, "mods/"+i])

memAllocated = config["ramAmount"]

subprocess.run(["java", "-Xmx"+str(memAllocated)+"G", "-jar", jarFile, "nogui"])

with open("eula.txt", "r") as eulaFile:
    eula = eulaFile.readlines()

eula[2] = "eula=true\n"

with open("eula.txt", "w") as eulaFile:
    eulaFile.writelines(eula)

subprocess.run(["sudo", "firewall-cmd", "--permanent", "--zone=public" ,"--add-port=25565/tcp"])
subprocess.run(["sudo", "firewall-cmd", "--permanent", "--zone=public" ,"--add-port=25565/udp"])

subprocess.run(["sudo", "firewall-cmd", "--reload"])

subprocess.run(["sudo", "yum", "install", "-y", "tmux"])

print("I'll create a .sh file to launch your server. Run source start.sh in installed tmux to launch.")

with open("start.sh", "w") as startFile:
    startFile.write("java -Xmx"+str(memAllocated)+"G -jar " +jarFile+ " nogui")

print("Complete! However, this doesn't configure whitelisting, which is highly recommended. Please do that asap after deployment!")