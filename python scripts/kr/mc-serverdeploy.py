import subprocess, os

print("안녕하세요! 이 스크립트는 마인크래프트 서버 제작을 도와줍니다. 현재 디렉토리에서 작업할게요.")

print("이 스크립트는 리눅스 전용으로 만들어졌습니다! https://ghpages.jclink.link//documentations/python-scripts/mc-createserver 에서 더 많은 정보를 확인해주세요.")

print("Java가 준비되어 있는지 확인할게요...")

subprocess.run(["java", "-version"])

print("애러가 나거나, 버젼이 너무 낮나요? Java를 업데이트하거나 설치해야 할 수 있어요. 스크립트를 멈추고 지금 해주세요.")

print("우선 서버 파일이 필요해요. 바닐라 서버를 원하시나요, 패브릭 서버를 원하시나요?")

serverType = input("1. 바닐라\n2. 패브릭\n선택> ")

if serverType == "1":
    print("https://www.minecraft.net/en-us/download/server 를 방문해 파일 다운로드 링크를 복사해주세요.")
    jarFileLink = input("그 다음, 여기 붙여넣어 주세요: ")
elif serverType == "2":
    print("https://fabricmc.net/use/server/ 를 방문해 파일 다운로드 링크를 복사해주세요.")
    jarFileLink = input("그 다음, 여기 붙여넣어 주세요: ")


subprocess.run(["curl", "-OJ", jarFileLink])

print("Jar 파일 찾는 중...")

filesInDir = os.listdir(os.getcwd())

for i in filesInDir:
    if i.endswith(".jar"):
        jarFile = i

if serverType == "2":
    print("모드를 설치할게요. (Fabric API는 필수로 설치하는걸 권장해요!) 빈 줄을 입력해 완료하세요.")
    os.mkdir("mods")

    while True:
        mod = input("모드 다운로드 링크 붙여넣기: ")
        if mod == "":
            break
        subprocess.run(["curl", "-OJ", mod])

    print("jar 파일 이동하는 중...")

    filesInDir = os.listdir(os.getcwd())

    for i in filesInDir:
        if i.endswith(".jar") and i != jarFile:
            subprocess.run(["mv", i, "mods/"+i])

print("서버를 시작할 준비가 거의 되었습니다. RAM을 몇 기가바이트 할당할까요?")

memAllocated = int(input("자연수> "))

subprocess.run(["java", "-Xmx"+str(memAllocated)+"G", "-jar", jarFile, "nogui"])

print("eula.txt 파일 수정을 요청하며 정지됐을 거에요. nano 를 열어드릴게요.")

print("화살표 키를 이용하여 이동해 eula=true로 변경한 뒤, ctrl+x를 누르고, 그 뒤 y 키, 다음 엔터를 눌러 저장하세요.")

input("준비되었다면, 엔터를 눌러 nano를 켜세요!")

subprocess.run(["nano", "eula.txt"])

print("서버가 준비되었습니다.")

print("\"java -Xmx"+str(memAllocated)+"G -jar " +jarFile+ " nogui\" (따옴표 제외)를 실행하여 서버를 시작하세요.")

print("뭔가 잘못되었다면, Java 버젼의 문제일 수 있습니다.")