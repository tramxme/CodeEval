import sys, re

def doStuff(line):
    s1,s2 = line.split(",")
    return (s1 in (s2+s2))


def main(file_name):
    fileName = open(file_name, 'r')
    for line in fileName.readlines():
        line = re.sub(r'\n','', line)
        print(doStuff(line))

if __name__ == '__main__':
    main(sys.argv[1])
