import json

modlist = []

print("이 파일은 모드 업데이트 전용 설정 파일을 만들어 줍니다! 서버에 배포 전, 꼭 테스트해 주세요.")
print("빈 줄을 입력해 완료합니다.")

while True:

    modLink = input("모드 다운로드 링크를 여기에 붙여넣어 주세요: ")

    if modLink == "":
        break

    modlist.append(modLink)

with open(input("파일명 (.json 확장자를 제외하고 영어로 입력해주세요): ")+".json", "w", encoding="UTF-8") as configFile:
    json.dump({"modlist": modlist}, configFile, indent=2)