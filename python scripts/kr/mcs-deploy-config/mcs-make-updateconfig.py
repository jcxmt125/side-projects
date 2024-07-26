import json

modlist = []

print("이 파일은 모드 업데이트 전용 설정 파일을 만들어 줍니다! 서버에 배포 전, 꼭 테스트해 주세요.")
print("빈 줄을 입력해 완료합니다.")

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

with open(input("파일명 (.json 확장자를 제외하고 영어로 입력해주세요): ")+".json", "w", encoding="UTF-8") as configFile:
    json.dump({"modlist": modlist}, configFile, indent=2)