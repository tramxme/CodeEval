'''
The problem is as follows: choose a number, reverse its digits and add it to the original. If the sum is not a palindrome (which means, it is not the same number from left to right and right to left), repeat this procedure.

For Example:
    195 (initial number) + 591 (reverse of initial number) = 786

    786 + 687 = 1473

    1473 + 3741 = 5214

    5214 + 4125 = 9339 (palindrome)
'''

import sys, re, math

def isPalindrome(string):
    length = len(string)
    for i in range(length//2):
        if string[i] != string[length-1-i]:
            return False
    return True

def reverse(string):
    num = ""
    for i in range(-1, -len(string) - 1, -1):
        num += string[i]
    return num

def add(string):
    return int(string) + int(reverse(string))

def doStuff(string):
    time = 0
    while isPalindrome(string) != True:
        time += 1
        string = str(add(string))
    print(str(time) + " " + string)


def main(file_name):
    fileName = open(file_name, 'r')
    for line in fileName.readlines():
        doStuff(re.sub("\n", "",line))

if __name__ == '__main__':
    main(sys.argv[1])



