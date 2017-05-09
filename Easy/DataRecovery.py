'''
CHALLENGE DESCRIPTION:

Your friends decided to make fun of you. They have installed a script on your computer which shuffled all words within a text. It is a joke, so they have left hints for each sentence. The hints will allow you to rebuild the data easily, but you need to find out how to use them.

Your task is to write a program which reconstructs each sentence out of a set of words and prints out the original sentences.


CONSTRAINTS:

The number of test cases is in a range from 20 to 40.
The words consist of ASCII uppercase and lowercase letters, digits, and punctuation marks.

'''
import sys, re, math

def doStuff(string):
    string = re.sub(r'\n','', string)
    words = string.split(";")[0].split()
    digits = string.split(";")[1].split()
    digits = [int(x) for x in digits]
    res = [""] * len(words)

    for i in range(1, len(words)+1):
        if i in digits:
            res[i-1] = words[digits.index(i)]
        else:
            res[i-1] = words[-1]


    print(" ".join(res))

def main(file_name):
    fileName = open(file_name, 'r')
    for line in fileName.readlines():
        doStuff(line)

if __name__ == '__main__':
    main(sys.argv[1])


