import sys, re, math

def doStuff(string):
    string = re.sub(r'\n','', string)

    values = string.split()
    res = ""
    count = 1
    num  = values[0]
    for i in range(1,len(values)):
        if values[i] == num:
            count += 1
        else:
            res += str(count) + " " + num + " "
            count = 1
            num = values[i]
    res += str(count) + " " + num
    print(res)

def main(file_name):
    fileName = open(file_name, 'r')
    for line in fileName.readlines():
        doStuff(line)

if __name__ == '__main__':
    main(sys.argv[1])


