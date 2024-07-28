pkg update
pkg upgrade -y
pkg install -y git
pkg install -y python
curl -OJ https://raw.githubusercontent.com/jcxmt125/side-projects/main/python%20scripts/mcs-deploy-config/touchless/mcs-deploy-touchless-termux.py
python mcs-deploy-touchless-termux.py