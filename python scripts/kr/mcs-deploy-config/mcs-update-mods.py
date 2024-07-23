import subprocess, os, json, shutil
from pathlib import Path

print("이 스크립트는 모드 디렉토리의 모든 내용을 삭제하고, 설정 파일의 모드들로 대체합니다.")

print("배포 설정 파일과 업데이트 전용 설정 파일 모두 사용 가능합니다.")

input("엔터를 눌러 계속하거나 Ctrl+C (KeyboardInturrupt)를 눌러 취소하세요.")

subprocess.run(["ls"])

filePath = input("설정 파일 이름: ")

with open(filePath, "r", encoding="UTF-8") as configFile:
    config = json.load(configFile)

shutil.rmtree(Path("mods"))

os.mkdir("mods")

filesInDir = os.listdir(os.getcwd())

for i in filesInDir:
    if i.endswith(".jar"):
        jarFile = i
        break

for i in config["modlist"]:
    subprocess.run(["curl", "-OJ", i])

print("jarFile 이동중...")

filesInDir = os.listdir(os.getcwd())

for i in filesInDir:
    if i.endswith(".jar") and i != jarFile:
        subprocess.run(["mv", i, "mods/"+i])

print("완료되었습니다! 준비되면 마인크래프트 서버를 다시 시작해주세요.")