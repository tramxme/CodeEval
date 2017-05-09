import sys, re, math

hexDict = {"0":0, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7,\
        "8":8, "9":9, "a":10, "b":11, "c":12, "d":13, "e":14, "f":15}

def hex2dec(string):
    total = 0
    i = 0
    for j in range(-1, -len(string) - 1, -1):
        total += (hexDict[string[j]] * (16**i))
        i += 1

    return total

def bin2dec(string):
    total = 0
    i = 0
    for j in range(-1, -len(string) - 1, -1):
        total += (int(string[j]) * (2**i))
        i += 1

    return total

def doStuff(string):
    string = re.sub(r'\n','', string)
    values = string.split(" | ")

    hexNums = values[0].split()
    binNums = values[1].split()

    hexSum = binSum = 0
    for v in hexNums:
        hexSum += hex2dec(v)

    for v in binNums:
        binSum += bin2dec(v)

    print(binSum >= hexSum)

def main(file_name):
    fileName = open(file_name, 'r')
    for line in fileName.readlines():
        doStuff(line)

if __name__ == '__main__':
    main(sys.argv[1])


