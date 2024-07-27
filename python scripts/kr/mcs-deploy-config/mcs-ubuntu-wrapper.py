import subprocess

print("이 스크립트는 Ubuntu에 마인크래프트 서버 배포를 도와줍니다.")

print("sudo 커맨드 몇 개를 실행합니다!")

print("mcs-deploy-config 스크립트도 있어야 합니다.")

extFileDL = input("혹시 까먹으셨다면, 지금 다운로드할까요? [y/n]")

if extFileDL == "y":
    subprocess.run(["curl", "-OJ", "https://raw.githubusercontent.com/jcxmt125/side-projects/main/python%20scripts/kr/mcs-deploy-config/mcs-deploy-config.py"])

subprocess.run(["sudo", "apt", "update"])

packUp = input("지금 패키지를 업그레이드 할까요? [y/n]")

if packUp == "y":
    subprocess.run(["sudo", "apt", "upgrade"])

subprocess.run(["apt", "search", "jre"])

packageName = input("패키지명을 붙여넣어 주세요: ")

print("설치 과정을 확인하고, y를 입력해 승인해주세요.")

subprocess.run(["sudo", "apt", "install", packageName])

subprocess.run(["python3", "mcs-deploy-config.py"])

print("네트워크 구성 중...")

subprocess.run(["sudo", "ufw", "allow" ,"25565"])

installTmux = input("screen을 설치할까요? [y/n]")

if installTmux == "y":
    subprocess.run(["sudo", "apt", "install", "screen"])

print("완료했습니다! 서버 제공자의 대시보드에서 설정을 마쳐주세요.")

print("다만, 이 스크립트는 화이트리스트나 enforce-secure-profile 제거 등의 설정은 진행하지 않습니다! 서버 시작 후, 직접 해주세요.")