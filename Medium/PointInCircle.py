import sys, re, math

def getX_Y(string):
    temp = string.split(":")[1]
    temp = re.sub(r"\(|\)", "", temp)
    X, Y = list(map(float, temp.split(",")))
    return X, Y

def doStuff(string):
    a,b,c = string.split(";")
    center_x, center_y = getX_Y(a)
    radius = float(b.split(":")[1])
    point_x, point_y = getX_Y(c)

    dist = math.sqrt(math.pow(point_x-center_x,2)+math.pow(point_y-center_y,2))
    if dist <= radius:
        return "true"
    return "false"

def main(file_name):
    fileName = open(file_name, 'r')
    for line in fileName.readlines():
        line = re.sub(r'\n','', line)
        print(doStuff(line))

if __name__ == '__main__':
    main(sys.argv[1])

