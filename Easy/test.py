import sys, re, math

def doStuff(string):
    string = re.sub(r'\n','', string)

    total = int(string)

    count = 0

    while total > 0:
        if total >= 5:
            count += total//5
            total -= (total//5)*5
        elif total >= 3:
            count += total//3
            total -= (total//3)*3
        else:
            count += total
            total = 0

    print(count)


def main(file_name):
    fileName = open(file_name, 'r')
    for line in fileName.readlines():
        doStuff(line)

if __name__ == '__main__':
    main(sys.argv[1])

