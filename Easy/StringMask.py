import sys, re, math

def bin2dec(string):
    total = 0
    i = 0
    for j in range(-1, -len(string) - 1, -1):
        total += (int(string[j]) * (2**i))
        i += 1

    return total

def doStuff(string):
    string = re.sub(r'\n','', string)

    values = string.split()
    num = ""

    for i in range(len(values)):
        if (i%2 == 0):
            flag = values[i]
        else:
            if flag == "0":
                num += values[i]
            elif flag == "00":
                num += "1" * len(values[i])

    res = bin2dec(num)

    print(res)


def main(file_name):
    fileName = open(file_name, 'r')
    for line in fileName.readlines():
        doStuff(line)

if __name__ == '__main__':
    main(sys.argv[1])



