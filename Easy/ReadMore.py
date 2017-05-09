import sys, re

def doStuff(line):
    res = ""
    size = len(line)
    if size <= 55:
        res = line
    else:
        res = line[:40]
        #If there are spaces ‘ ’ in the resulting string,
        #trim it once again to the last space (the space should be trimmed too).
        if res.rfind(" ") != -1:
            res = res[:res.rfind(" ")]
        res += "... <Read More>"

    print(res)


def main(file_name):
    fileName = open(file_name, 'r')
    for line in fileName.readlines():
        line = re.sub(r'\n','', line)
        doStuff(line)

if __name__ == '__main__':
    main(sys.argv[1])
