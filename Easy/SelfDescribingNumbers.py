'''
CHALLENGE DESCRIPTION:

A number is a self-describing number when (assuming digit positions are labeled 0 to N-1), the digit in each position is equal to the number of times that that digit appears in the number.

For the curious, here's how 2020 is a self-describing number: Position '0' has value 2 and there is two 0 in the number. Position '1' has value 0 because there are not 1's in the number. Position '2' has value 2 and there is two 2. And the position '3' has value 0 and there are zero 3's.

'''
import sys, re, math

def doStuff(string):
    string = re.sub(r'\n','', string)
    count = {}
    res = 1

    for c in string:
        num = int(c)
        if num in count.keys():
            count[num] += 1
        else:
            count.setdefault(num, 1)

    for i in range(len(string)):
        if (i in count.keys() and count[i] != int(string[i])) or (i not in count.keys() and int(string[i]) != 0):
            res = 0
            break


    print(res)

def main(file_name):
    fileName = open(file_name, 'r')
    for line in fileName.readlines():
        doStuff(line)

if __name__ == '__main__':
    main(sys.argv[1])

