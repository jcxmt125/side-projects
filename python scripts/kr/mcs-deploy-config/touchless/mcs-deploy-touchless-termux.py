import subprocess, json, os

print("aarch64 Termux를 위한 빠른 설치를 시작합니다......")

tlconfigLink = "https://raw.githubusercontent.com/jcxmt125/side-projects/main/python%20scripts/mcs-deploy-config/touchless/touchless-config-termux.json"

subprocess.run(["curl", "-OJ", tlconfigLink])



filePath = "touchless-config-oracle-aarch.json"

with open(filePath, "r", encoding="UTF-8") as configFile:
    config = json.load(configFile)

serverType = config["serverType"]

jarFileLink = config["jarFileLink"]

javaName = config["javaName"]

print("Java 다운로드중...")

subprocess.run(["curl", "-OJ", javaName])

print("Java를 찾고 압축 해제하는 중...")

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

print("마인크래프트 서버에 할당할 RAM을 기가바이트 단위로 입력해주세요.")

memAllocated = input("RAM GB (자연수)> ")

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

print("서버 시작을 도와주는 .sh 파일을 만들어 드릴게요. source start.sh를 실행해 시작하세요.")

with open("start.sh", "w") as startFile:
    startFile.write(javapath+" -Xmx"+str(memAllocated)+"G -jar " +jarFile+ " nogui")

print("완료했어요! 다만, 화이트리스트 기능은 설정하지 않았어요. 서버를 시작하고 가능한 한 빨리 설정해주세요!")