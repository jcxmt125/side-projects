import subprocess, os

print("Hello! This script will help you deploy a minecraft server. I'll work in the current directory.")

print("This script is made for Linux, by the way! Please see https://hackclub.jclink.link/documentations/python-scripts/mc-createserver for more info.")

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
    print("Let's install some mods. (I recommend installing the Fabric API!) Return an empty line to finish!")
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

memAllocated = int(input("Integer> "))

subprocess.run(["java", "-Xmx"+str(memAllocated)+"G", "-jar", jarFile, "nogui"])

print("It should have exited asking you to edit the eula.txt file. I'll launch nano for you.")

print("Use arrow keys to navigate and change the line to eula=true, then press ctrl+x, then say yes by pressing the y key, then press enter.")

input("Ready? Press return to launch nano!")

subprocess.run(["nano", "eula.txt"])

print("Okay, your server should be ready.")

print("After this, run \"java -Xmx"+str(memAllocated)+"G -jar " +jarFile+ " nogui\" without the quotes to start the server.")

print("If that didn't work, you may have to upgrade or install Java. Do so, and run the above command.")

print("Done!")