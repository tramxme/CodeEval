'''
CHALLENGE DESCRIPTION:
You are given a piece of text. Your job is to write a program that sets the case of text characters according to the following rules:

The first letter of the line should be in uppercase.
The next letter should be in lowercase.
The next letter should be in uppercase, and so on.
Any characters, except for the letters, are ignored during determination of letter case.


CONSTRAINTS:
The length of each piece of text does not exceed 1000 characters.
'''
import sys, re

def doStuff(string):
    string = re.sub(r'\n','', string)
    chars = list(string)

    res = ""
    up = True
    for i in range(len(chars)):
        if(chars[i].isalpha() == True and up == True):
            up = False
            res += chars[i].upper()
        else:
            if chars[i].isalpha():
                up = True
            res += chars[i]

    print(res)

def main(file_name):
    fileName = open(file_name, 'r')
    for line in fileName.readlines():
        doStuff(line)

if __name__ == '__main__':
    main(sys.argv[1])


