import subprocess, os

print("Hello! This script will help you deploy a minecraft server. I'll work in the current directory.")

print("This script is made for Linux!")

print("Let's see if your system has Java ready...")

subprocess.run(["java", "-version"])

print("Did this error out? Or is the version too low? You may have to update or reinstall Java. Please exit the script and do that now.")

print("We'll need the server file. Are you planning to play vanilla or Fabric?")

serverType = input("1. Vanilla\n2. Fabric\nSelect> ")

if serverType == "1":
    print("Please visit https://www.minecraft.net/en-us/download/server and copy the link to the jarfile.")
    jarFileLink = input("When done, please paste here: ")
elif serverType == "2":
    print("Please visit https://fabricmc.net/use/server/ and copy the link to the jarfile.")
    jarFileLink = input("When done, please paste here: ")


subprocess.run(["curl", "-OJ", jarFileLink])

print("Finding the JarFile...")

filesInDir = os.listdir(os.getcwd())

for i in filesInDir:
    if i.endswith(".jar"):
        jarFile = i

if serverType == "2":
    print("Let's install some mods. (I recommend installing the Fabric API!)")
    os.mkdir("mods")

    while True:
        mod = input("Paste link to mod: ")
        if mod == "":
            break
        subprocess.run(["curl", "-OJ", mod])

    print("moving jarFiles...")

    filesInDir = os.listdir(os.getcwd())

    for i in filesInDir:
        if i.endswith(".jar") and i != jarFile:
            subprocess.run(["mv", i, "mods/"+i])

print("We're almost ready to run the server. How many gigabytes of RAM would you like to give the server?")

print("It'll likely ask you to edit the eula.txt file. Please do so!")

memAllocated = int(input("Integer> "))

subprocess.run(["java", "-Xmx"+str(memAllocated)+"G", "-jar", jarFile, "nogui"])

print("After this, run \"java -Xmx"+str(memAllocated)+"G -jar" +jarFile+ " nogui\" without the quotes to start the server.")

print("If that didn't work, you may have to upgrade or install Java. Do so, and run the above command.")

print("Done!")