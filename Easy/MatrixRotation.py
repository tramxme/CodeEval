import sys, re, math

def doStuff(string):
    chars = string.split()
    size = int(math.sqrt(len(chars)))
    matrix = []
    idx = 0
    for i in range(size):
        temp = []
        for j in range(size):
            temp.append(chars[idx])
            idx += 1
        matrix.append(temp)

    #Do the swapping
    new_matrix = []
    for i in range(size):
        temp = []
        for j in range(size):
            temp.append(matrix[size-1-j][i])
            idx += 1
        new_matrix.append(temp)

    #Print the result
    res = ""
    for i in range(size):
        for j in range(size):
            res += new_matrix[i][j] + " "

    print(res)

def main(file_name):
    fileName = open(file_name, 'r')
    for line in fileName.readlines():
        line = re.sub(r'\n','', line)
        doStuff(line)

if __name__ == '__main__':
    main(sys.argv[1])



