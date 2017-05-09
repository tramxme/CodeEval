import sys, re

def doStuff(line):
    v = line.split("|")
    col,row = list(map(int, v[0].split("x")))
    x,y = list(map(int, v[1].split()))
    matrix = [[0] * col for i in range(row)]
    matrix[0][0] = 1
    #Populate the matrix

    #Result
    print(matrix[-y][x-1])


def main(file_name):
    fileName = open(file_name, 'r')
    for line in fileName.readlines():
        line = re.sub(r'\n','', line)
        doStuff(line)

if __name__ == '__main__':
    main(sys.argv[1])
