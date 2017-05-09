import sys, re

def doStuff(string):
    idx = 1
    temp = ""
    while idx < len(string):
        if string == (string[:idx] * (len(string)//idx)):
            return idx
        else:
            idx += 1
    return idx

def main(file_name):
    fileName = open(file_name, 'r')
    for line in fileName.readlines():
        line = re.sub(r'\n','', line)
        print(doStuff(line))

if __name__ == '__main__':
    main(sys.argv[1])
