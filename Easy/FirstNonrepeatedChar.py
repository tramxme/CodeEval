import sys, re, math

def doStuff(string):
    string = re.sub(r'\n','', string)

    chars = list(string)
    res = ""

    for i in range(len(chars)):
        if chars



def main(file_name):
    fileName = open(file_name, 'r')
    for line in fileName.readlines():
        doStuff(line)

if __name__ == '__main__':
    main(sys.argv[1])


