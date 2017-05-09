import sys, re

def doStuff(string):
    res = ""
    cur = string[0]
    for c in string[1:]:
        if c != cur:
            res += cur
            cur = c
    res += cur
    print(res)


def main(file_name):
    fileName = open(file_name, 'r')
    for line in fileName.readlines():
        line = re.sub(r'\n','', line)
        doStuff(line)

if __name__ == '__main__':
    main(sys.argv[1])



