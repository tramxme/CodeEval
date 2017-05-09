import sys, re

def doStuff(string):
    x, y, x_dest, y_dest = list(map(int, string.split()))
    res = ""
    if x == x_dest and y == y_dest:
        res = "here"
    elif x == x_dest:
        if y_dest > y:
            res = "N"
        else:
            res = "S"
    elif y == y_dest:
        if x_dest > x:
            res = "E"
        else:
            res = "W"
    else:
        if x_dest > x and y_dest > y:
            res = "NE"
        elif x_dest > x and y_dest < y:
            res = "SE"
        elif x_dest < x and y_dest > y:
            res = "NW"
        elif x_dest < x and y_dest < y:
            res = "SW"

    print(res)

def main(file_name):
    fileName = open(file_name, 'r')
    for line in fileName.readlines():
        line = re.sub(r'\n','', line)
        doStuff(line)

if __name__ == '__main__':
    main(sys.argv[1])


