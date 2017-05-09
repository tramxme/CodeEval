import sys, re

def doStuff(line):
    v = line.split()
    num = int(v[0])
    v = v[1:]
    numL = []
    numL.extend(range(num+1))

    for i in range(len(v)):
        if v[i] == "Lower":
            numL = numL[:len(numL)//2]
        elif v[i] == "Higher":
            numL = numL[len(numL)//2+1:]
        elif v[i] == "Yay!":
            return numL[len(numL)//2]

def main(file_name):
    fileName = open(file_name, 'r')
    for line in fileName.readlines():
        line = re.sub(r'\n','', line)
        print(doStuff(line))

if __name__ == '__main__':
    main(sys.argv[1])
