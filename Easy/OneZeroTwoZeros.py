import sys, re, math
def countZeros(num):
    n = 1
    count = 0
    while n < num:
        if (n & num) == 0:
            count += 1
        n = n << 1
    return count

def doStuff(string):
    n, k = list(map(int, string.split(" ")))
    start = 1
    count = 0

    while start <= k:
        if countZeros(start) == n:
            count+=1
        start+=1
    return count

def main(file_name):
    fileName = open(file_name, 'r')
    for line in fileName.readlines():
        print(doStuff(line))

if __name__ == '__main__':
    main(sys.argv[1])


