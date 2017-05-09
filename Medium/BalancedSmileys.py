import sys, re

def doStuff(string):
    chars = list(string)
    stack = []
    for c in chars:
        if c in ":()":
            stack.append(c)
    print(stack)


def main(file_name):
    fileName = open(file_name, 'r')
    for line in fileName.readlines():
        line = re.sub(r'\n','', line)
        doStuff(line)

if __name__ == '__main__':
    main(sys.argv[1])

