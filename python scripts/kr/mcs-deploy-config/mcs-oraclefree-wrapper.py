import subprocess

print("이 스크립트는 Oracle 리눅스에 마인크래프트 서버 배포를 도와줍니다.")

print("sudo 커맨드 몇 개를 실행합니다!")

print("mcs-deploy-config 스크립트도 있어야 합니다.")

extFileDL = input("혹시 까먹으셨다면, 지금 다운로드할까요? [y/n]")

if extFileDL == "y":
    subprocess.run(["curl", "-OJ", "https://raw.githubusercontent.com/jcxmt125/side-projects/main/python%20scripts/kr/mcs-deploy-config/mcs-deploy-config.py"])

subprocess.run(["yum", "list", "jdk*"])

packageName = input("패키지명을 붙여넣어 주세요: ")

print("설치 과정을 확인하고, y를 입력해 승인해주세요.")

subprocess.run(["sudo", "yum", "install", packageName])

subprocess.run(["python", "mcs-deploy-config.py"])

print("네트워크 구성 중...")

subprocess.run(["sudo", "firewall-cmd", "--permanent", "--zone=public" ,"--add-port=25565/tcp"])
subprocess.run(["sudo", "firewall-cmd", "--permanent", "--zone=public" ,"--add-port=25565/udp"])

subprocess.run(["sudo", "firewall-cmd", "--reload"])

installTmux = input("Tmux를 설치할까요? [y/n]")

if installTmux == "y":
    subprocess.run(["sudo", "yum", "install", "tmux"])

print("완료했습니다! Oracle 대시보드에서 설정을 마쳐주세요.")
print("다만, 이 스크립트는 화이트리스트나 enforce-secure-profile 제거 등의 설정은 진행하지 않습니다! 서버 시작 후, 직접 해주세요.")