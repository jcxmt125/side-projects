import subprocess

print("This script will help you deploy on Ubuntu.")

print("I'll execute some sudo commands. Please be aware!")

print("Make sure you also have the mcs-deploy-config script!")

subprocess.run(["sudo", "apt", "update"])

packUp = input("Upgrade packages now? [y/n]")

if packUp == "y":
    subprocess.run(["sudo", "apt", "upgrade"])

subprocess.run(["apt", "search", "jre"])

packageName = input("Input appropriate package name here: ")

print("Please look over the install, and input y to continue the install.")

subprocess.run(["sudo", "apt", "install", packageName])

subprocess.run(["python3", "mcs-deploy-config.py"])

print("Configuring network...")

subprocess.run(["sudo", "ufw", "allow" ,"25565"])

installTmux = input("Do you want to install screen? [y/n]")

if installTmux == "y":
    subprocess.run(["sudo", "apt", "install", "screen"])

print("All done. Please finish setup on the provider's dashboard.")