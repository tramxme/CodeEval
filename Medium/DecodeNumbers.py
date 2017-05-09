import sys, re

def count(string):
    if len(string) == 1 || len(string) == 0:
        return 1


def main(file_name):
    fileName = open(file_name, 'r')
    for line in fileName.readlines():
        line = re.sub(r'\n','', line)
        doStuff(line)

if __name__ == '__main__':
    main(sys.argv[1])
