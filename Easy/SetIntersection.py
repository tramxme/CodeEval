'''
CHALLENGE DESCRIPTION
You are given two sorted list of numbers (ascending order). The lists themselves are comma delimited and the two lists are semicolon delimited. Print out the intersection of these two sets.
'''

import sys, re, math

def doStuff(string):
    string = re.sub(r'\n','', string)
    set1 = string.split(";")[0].split(",")
    set1 = [int(x) for x in set1]

    set2 = string.split(";")[1].split(",")
    set2 = [int(x) for x in set2]

    res = sorted(set(set1).intersection(set(set2)))
    res = [str(x) for x in res]

    res = ",".join(res)
    print(res.rstrip(","))

def main(file_name):
    fileName = open(file_name, 'r')
    for line in fileName.readlines():
        doStuff(line)

if __name__ == '__main__':
    main(sys.argv[1])
