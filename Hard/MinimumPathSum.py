import sys, re, math

def doStuff(matrix):
    '''
    Definition: MP[i][j] = the minimum path sum at cell (i,j)
    Formula: MP[i][j] = min{MP[i-1][j], MP[i][j-1]} + v[i][j]
    Base case: MP[0][j] = 0, MP[i][0] = 0
    Solution: MP[n-1][n-1]
    '''
    n = len(matrix[0])
    MP = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            if i - 1 < 0 and j - 1 >= 0:
                MP[i][j] = MP[i][j-1] + matrix[i][j]
            elif i - 1 >= 0 and j - 1 < 0:
                MP[i][j] = MP[i-1][j] + matrix[i][j]
            else:
                MP[i][j] = min(MP[i-1][j],MP[i][j-1]) + matrix[i][j]


    print(MP[n-1][n-1])


def main(file_name):
    fileName = open(file_name, 'r')
    matrix = []
    for line in fileName.readlines():
        line = re.sub(r'\n','', line)
        if "," in line:
            n = list(map(int, line.split(",")))
            matrix.append(n)
        else:
            if len(matrix) != 0:
                doStuff(matrix)
                matrix = []
    doStuff(matrix)

if __name__ == '__main__':
    main(sys.argv[1])
