import json

print("안녕하세요! 이 스크립트는 마인크래프트 서버 배포를 위한 설정 파일을 생성해 줍니다.")

serverType = int(input("어떤 타입의 서버를 원하시나요? 1. 바닐라 2. 패브릭\n> "))

modlist = []

if serverType == 1:
    print("https://www.minecraft.net/ko-kr/download/server 를 방문해, 서버 다운로드 링크를 복사해주세요.")
    jarFileLink = input("그 다음, 여기에 붙여넣어 주세요: ")

elif serverType == 2:
    print("https://fabricmc.net/use/server/를 방문해, 서버 다운로드 링크를 복사해주세요.")
    jarFileLink = input("그 다음, 여기에 붙여넣어 주세요: ")

    print("이제 모드를 추가합니다! 서버에 배포 전, 꼭 테스트해 주세요. 빈 줄을 입력해 완료합니다.")

    while True:

        modLink = input("모드 다운로드 링크를 여기에 붙여넣어 주세요: ")

        if "forge" in modLink:
            print("잠시만요, 이거 패브릭 모드 맞아요?")

            modConfirm = input("엔터를 눌러 추가하거나, 뭔가 입력해 엔터를 누르면 취소합니다: ")

            if modConfirm != "":
                continue
        
        if not modLink.endswith(".jar"):
            print("잠시만요, 이거 다운로드 링크 맞아요?")

            modConfirm = input("웹사이트가 아닌 직접 다운로드 링크여야 합니다. 엔터를 눌러 추가하거나, 뭔가 입력해 엔터를 누르면 취소합니다: ")

            if modConfirm != "":
                continue

        if modLink == "":
            break

        modlist.append(modLink)

ramAmount = int(input("RAM은 최대 몇 기가바이트 할당할까요? \n>"))

print("이 설정을 파일로 저장합니다.")

with open(input("파일명 (.json 확장자를 제외하고 영어로 입력해주세요): ")+".json", "w", encoding="UTF-8") as configFile:
    json.dump({"serverType": serverType, "jarFileLink": jarFileLink, "modlist": modlist, "ramAmount": ramAmount}, configFile, indent=2)