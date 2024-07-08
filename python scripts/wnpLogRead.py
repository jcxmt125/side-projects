import datetime

with open(input("Drag log file here: "),"r",encoding="UTF-8") as logFile:
    logList = logFile.read().split("\n")

logListSplit = []

for i in logList:
    logListSplit.append(i.split(" || "))

print("Log file imported!\n\
1. List videos by times played")

actionChose = int(input("What would you like to do> "))

if actionChose == 1:

    playTimeDict = dict()

    for i in logListSplit:

        if len(i) == 1:

            continue

        if i[1] in playTimeDict:

            playTimeDict[i[1]] += 1

        else:

            playTimeDict[i[1]] = 1

    playTimeList = []

    for i in playTimeDict:
        playTimeList.append([playTimeDict[i], i])

    print(playTimeList)