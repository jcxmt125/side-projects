import subprocess

print("This script will help you deploy on Ubuntu.")

print("I'll execute some sudo commands. Please be aware!")

print("Make sure you also have the mcs-deploy-config script!")

extFileDL = input("If you haven't, do you want to download it now? [y/n]")

if extFileDL == "y":
    subprocess.run(["curl", "-OJ", "https://raw.githubusercontent.com/jcxmt125/side-projects/main/python%20scripts/mcs-deploy-config/mcs-deploy-config.py"])

subprocess.run(["sudo", "apt", "update"])

packUp = input("Upgrade packages now? [y/n]")

if packUp == "y":
    subprocess.run(["sudo", "apt", "upgrade", "-y"])

subprocess.run(["apt", "search", "jre"])

packageName = input("Input appropriate package name here: ")

print("Please look over the install, and input y to continue the install.")

subprocess.run(["sudo", "apt", "install", packageName])

subprocess.run(["python3", "mcs-deploy-config.py"])

print("Configuring network...")

subprocess.run(["sudo", "ufw", "allow" ,"25565"])

installTmux = input("Do you want to install screen? (preinstalled in most Ubuntu installations) [y/n]")

if installTmux == "y":
    subprocess.run(["sudo", "apt", "install", "screen"])

print("All done. Please finish setup on the provider's dashboard.")

print("However, this doesn't configure whitelisting, which is highly recommended, or disabling enforce-secure-profile for mods like NoChatReports. Please do that asap after deployment!")