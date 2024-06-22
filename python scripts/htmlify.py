with open("source.txt", 'r', encoding="UTF-8") as src:
    fulltext = src.readlines()

for i in range(len(fulltext)):
    if fulltext[i][-1] == "\n":
        fulltext[i] = "                " + fulltext[i][:-1] + "<br>\n"

with open("results.txt", 'w', encoding="UTF-8") as rsl:
    
    toWrite = ""
    
    for j in fulltext:
        toWrite += j

    rsl.write(toWrite)
    
print("wrote " + str(i) + " lines")