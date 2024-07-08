from pywnp import WNPRedux
import time
import datetime

# Custom logger, type can be 'Error', 'Debug' or 'Warning'
def logger(type, message):
  print(f'{type}: {message}')

# Start WNP, providing a port, version number and a logger
def start():
    WNPRedux.start(1234, '1.0.0', logger)

    npCatch = "N/A"
    
    while True:

        if npCatch != WNPRedux.media_info.title and WNPRedux.media_info.title != "":
            with open('wnplog.txt', 'a', encoding="UTF-8") as f:
                print(WNPRedux.media_info.title)
                f.write(str(datetime.datetime.now()) + " || " + WNPRedux.media_info.title + " || " + WNPRedux.media_info.artist + "\n")
                npCatch = WNPRedux.media_info.title

        time.sleep(1)

if __name__ == "__main__":
    try: 
        start()
    except:
        WNPRedux.stop()