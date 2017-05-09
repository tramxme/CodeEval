'''
CHALLENGE DESCRIPTION:
Your good friend Tom is admirer of tasting different types of fine wines. What he loves even more is to guess their names. One day, he was sipping very extraordinary wine. Tom was sure he had tasted it before, but what was its name? The taste of this wine was so familiar, so delicious, so pleasant… but what is it exactly? To find the answer, Tom decided to taste the wines we had. He opened wine bottles one by one, tasted different varieties of wines, but still could not find the right one. He was getting crazy, “No, it’s not that!” desperately breaking a bottle of wine and opening another one. Tom went off the deep end not knowing what this wine was. Everything he could say is just several letters of its name. You can no longer look at it and decided to help him.
Your task is to write a program that will find the wine name, containing all letters that Tom remembers.

CONSTRAINTS:
Wine name length can be from 2 to 15 characters.
Number of letters that Tom remembered does not exceed 5.
Number of wine names in a test case can be from 2 to 10.
If there is no wine name containing all letters, print False.
The number of test cases is 40.

'''
import sys, re, math

def countChar(s):
    count = {}
    for c in s:
        if c in count:
            count[c] += 1
        else:
            count.setdefault(c,1)

    return count

def doStuff(string):
    values = string.split(" | ")
    wines = values[0].split()

    rememberedChars_count = countChar(values[1])

    res = []
    for wine in wines:
        temp = countChar(wine)

        correctWine = True
        for k,v in rememberedChars_count.items():
            if k not in temp or temp[k] < v:
                correctWine = False
                break

        if correctWine == True:
            res.append(wine)

    if len(res) == 0:
        print("False")
    else:
        print(" ".join(res))


def main(file_name):
    fileName = open(file_name, 'r')
    for line in fileName.readlines():
        doStuff(re.sub(r'\n','', line))

if __name__ == '__main__':
    main(sys.argv[1])


