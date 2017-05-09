import sys, re

def doStuff(line):
    res = ""
    line = line.split(",")
    str1 = line[0].strip()
    str2 = line[1].strip()
    for c in str1:
        if c not in str2:
            res += c
    print(res)


def main(file_name):
    fileName = open(file_name, 'r')
    for line in fileName.readlines():
        line = re.sub(r'\n','', line)
        doStuff(line)

if __name__ == '__main__':
    main(sys.argv[1])
