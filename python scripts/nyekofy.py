originalPhrase = input("Input original script: ")

origPhraseList = originalPhrase.split()

print(origPhraseList)

newPhraseList = []

#Why does in-place replace not work..?
for i in origPhraseList:
    if i == "you":
        newPhraseList.append("nyu")
    elif i == "your":
        newPhraseList.append("nyor")
    elif "ne" in i:
        newPhraseList.append(i + "*")
    else:
        newPhraseList.append(i)

joined = ""

for i in newPhraseList:
    joined += i
    joined += " "

print(joined)