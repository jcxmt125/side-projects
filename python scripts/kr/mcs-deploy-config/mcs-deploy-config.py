import subprocess, json, os

print("안녕하세요! 이 스크립트는 마인크래프트 서버 셋업을 도와줍니다. 현재 디렉토리에서 작업할게요.")

subprocess.run(["ls"])

filePath = input("설정 파일의 이름이 뭔가요?\n>")

with open(filePath, "r", encoding="UTF-8") as configFile:
    config = json.load(configFile)

serverType = config["serverType"]

jarFileLink = config["jarFileLink"]

subprocess.run(["curl", "-OJ", jarFileLink])

print("JarFile을 찾고 있어요...")

filesInDir = os.listdir(os.getcwd())

for i in filesInDir:
    if i.endswith(".jar"):
        jarFile = i

if int(serverType) == 2:
    os.mkdir("mods")

    for i in config["modlist"]:
        subprocess.run(["curl", "-OJ", i])

    print("jarFile을 이동중이에요...")

    filesInDir = os.listdir(os.getcwd())

    for i in filesInDir:
        if i.endswith(".jar") and i != jarFile:
            subprocess.run(["mv", i, "mods/"+i])

memAllocated = config["ramAmount"]

subprocess.run(["java", "-Xmx"+str(memAllocated)+"G", "-jar", jarFile, "nogui"])

print("eula.txt와 관련된 에러가 나며 멈췄을 거에요. 수정할 수 있게 nano를 열어드릴게요.")

print("화살표 키를 이용해 움직이고, eula=true가 되도록 텍스트를 변경해주세요. 그 후, ctrl+x를 누르고, 뒤의 확인창에서 y, 그 다음 엔터를 눌러주세요.")

input("준비됐나요? 엔터를 눌러 nano를 여세요!")

subprocess.run(["nano", "eula.txt"])

print("서버를 실행하려면 \"java -Xmx"+str(memAllocated)+"G -jar " +jarFile+ " nogui\" (따옴표 제외) 명령을 이용해주세요.")

print(".sh 파일도 생성합니다! source start.sh 를 실행하셔도 됩니다.")

with open("start.sh", "w") as startFile:
    startFile.write("java -Xmx"+str(memAllocated)+"G -jar " +jarFile+ " nogui")

print("배포 스크립트 실행 완료!")