import subprocess

print("This script will help you deploy on Oracle's linux distro.")

print("I'll execute some sudo commands. Please be aware!")

print("Make sure you also have the mcs-deploy-config script!")

extFileDL = input("If you haven't, do you want to download it now? [y/n]")

if extFileDL == "y":
    subprocess.run(["curl", "-OJ", "https://raw.githubusercontent.com/jcxmt125/side-projects/main/python%20scripts/mcs-deploy-config/mcs-deploy-config.py"])

print("I'll update packages before we start. This might take a bit!")

subprocess.run(["sudo", "yum", "update"])

subprocess.run(["yum", "list", "jdk*"])

packageName = input("Input appropriate package name here: ")

print("Please look over the install, and input y to continue the install.")

subprocess.run(["sudo", "yum", "install", packageName])

subprocess.run(["python", "mcs-deploy-config.py"])

print("Configuring network...")

subprocess.run(["sudo", "firewall-cmd", "--permanent", "--zone=public" ,"--add-port=25565/tcp"])
subprocess.run(["sudo", "firewall-cmd", "--permanent", "--zone=public" ,"--add-port=25565/udp"])

subprocess.run(["sudo", "firewall-cmd", "--reload"])

installTmux = input("Do you want to install Tmux? [y/n]")

if installTmux == "y":
    subprocess.run(["sudo", "yum", "install", "tmux"])

print("All done. Please finish setup on the Oracle dashboard.")

print("However, this doesn't configure whitelisting, which is highly recommended, or disabling enforce-secure-profile for mods like NoChatReports. Please do that asap after deployment!")