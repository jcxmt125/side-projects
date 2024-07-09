import datetime

with open(input("Drag log file here: "),"r",encoding="UTF-8") as logFile:
    logList = logFile.read().split("\n")

logListSplit = []

for i in logList:
    logListSplit.append(i.split(" || "))

print("Log file imported!\n\
1. List videos by times played\n\
2. List artists (channels) by times played")

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

    playTimeList.sort(reverse=True)

    if len(playTimeList) < 5:

        print(f"Top {str(len(playTimeList))} songs played: ")

        for i in playTimeList:
            print(str(i[0]) + " times: " + i[1])

    else:

        print("Top 5 songs played: ")

        for i in range(5):
            print(str(playTimeList[i][0]) + " times: " + playTimeList[i][1])

elif actionChose == 2:

    playTimeDict = dict()

    for i in logListSplit:

        if len(i) == 1:

            continue

        if i[2] in playTimeDict:

            playTimeDict[i[2]] += 1

        else:

            playTimeDict[i[2]] = 1

    playTimeList = []

    for i in playTimeDict:
        playTimeList.append([playTimeDict[i], i])

    playTimeList.sort(reverse=True)

    if len(playTimeList) < 5:

        print(f"Top {str(len(playTimeList))} artists played: ")

        for i in playTimeList:
            print(str(i[0]) + " times: " + i[1])

    else:

        print("Top 5 artists played: ")

        for i in range(5):
            print(str(playTimeList[i][0]) + " times: " + playTimeList[i][1])\

