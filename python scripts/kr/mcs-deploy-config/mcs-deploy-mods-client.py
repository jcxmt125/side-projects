import subprocess, json, os, shutil

from pathlib import Path

print("이 스크립트는 마인크래프트 모드 디렉토리로 빠른 모드 설치를 도와줍니다.")

print("윈도우 전용 스크립트입니다.\n폴더를 만들어 그 안에서 실행해주세요.")

print("계속하면, 설정 파일 내의 내용으로 마인크래프트 모드 디렉토리가 변경되는 것에 동의합니다. 이전 모드들은 백업됩니다.")

filePath = input("설정 파일을 끌어다 놓으세요!\n>")

with open(filePath, "r", encoding="UTF-8") as configFile:
    config = json.load(configFile)

for i in config["modlist"]:
    print(i)
    subprocess.run(["curl", "-OJ", i])

if Path.exists(Path(os.getenv("APPDATA") + "\.minecraft\mods")):
    print("backing up current mods...")
    shutil.move(Path(os.getenv("APPDATA") + "\.minecraft\mods"), Path("mods.old"))

print("moving new mod jarFiles...")

filesInDir = os.listdir(os.getcwd())

try:
    os.mkdir(os.getenv("APPDATA") + "\.minecraft\mods")
except:
    print("WARN: 기존 모드 디렉토리가 삭제되지 않았습니다.")

for i in filesInDir:
    if i.endswith(".jar"):
        shutil.move(Path(i), Path(os.getenv("APPDATA") + "\.minecraft\mods\\" + i))

print("설치 스크립트 실행 완료!")

input("엔터 키를 눌러 종료하세요.")