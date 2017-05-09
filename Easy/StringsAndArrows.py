import sys, re, math

def doStuff(string):
    string = re.sub(r'\n','', string)

    count = 0
    arrow1 = "<--<<"
    arrow2 = ">>-->"

    for i in range(len(string) - 4):
        if string[i:i+5] == arrow1 or string[i:i+5] == arrow2:
            count += 1

    print(count)


def main(file_name):
    fileName = open(file_name, 'r')
    for line in fileName.readlines():
        doStuff(line)

if __name__ == '__main__':
    main(sys.argv[1])


