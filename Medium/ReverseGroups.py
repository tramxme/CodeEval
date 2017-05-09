import sys, re
def reverse(L):
    res = []
    for i in range(-1, -len(L)-1,-1):
        res.append(L[i])
    return res

def doStuff(line):
    v = line.split(";")
    numList = v[0].split(",")
    size = int(v[1])
    res = []
    start = 0
    end = size
    for i in range(len(numList)//size):
        res.extend(reverse(numList[start:end]))
        start = end
        end += size
    res.extend(numList[start:])

    print(",".join(str(x) for x in res))


def main(file_name):
    fileName = open(file_name, 'r')
    for line in fileName.readlines():
        line = re.sub(r'\n','', line)
        doStuff(line)

if __name__ == '__main__':
    main(sys.argv[1])
