import sys, re

def doStuff(line):
    v = line.split()
    seq = v[:-1]
    num = int(v[-1])
    if num <= len(seq):
        print(seq[-num])

def main(file_name):
    fileName = open(file_name, 'r')
    for line in fileName.readlines():
        line = re.sub(r'\n','', line)
        doStuff(line)

if __name__ == '__main__':
    main(sys.argv[1])
