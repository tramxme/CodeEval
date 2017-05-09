import sys, re

#This method inserts firstChar into position i in a word
def insertChar(word, firstChar,i):
    return word[0:i] + firstChar + word[i:]

def getPerms(string):
    permList = []

    if string == "":
    	permList.append("")
    	return permList

    firstChar = string[0]
    words = getPerms(string[1:])
    for word in words:
        for i in range(len(word) + 1):
            permList.append(insertChar(word, firstChar, i))
    return permList


def doStuff(string):
    string = re.sub(r'\n', '', string)

    words = getPerms(string)
    words.sort()

    print(",".join(words))


def main(file_name):
    fileName = open(file_name, 'r')
    for line in fileName.readlines():
        doStuff(line)

if __name__ == '__main__':
    main(sys.argv[1])

