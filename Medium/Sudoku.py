import sys, re, math

def checkRowAndCol(board, size):
    #Check row
    for row in range(size):
        default = [False] * size
        for col in range(size):
            if default[board[row][col]-1] == True:
                return False
            else:
                default[board[row][col]-1] = True

    #Check column
    for col in range(size):
        default = [False] * size
        for row in range(size):
            if default[board[row][col]-1] == True:
                return False
            else:
                default[board[row][col]-1] = True
    return True

def checkSubGrid(board, size):
    default = [False] * size * size
    for row in range(size):
        for col in range(size):
            if default[board[row][col]-1] == True:
                return False
            else:
                default[board[row][col]-1] = True
    return True

def doStuff(line):
    values = line.split(";")
    N = int(values[0])
    nums = list(map(int, values[1].split(",")))
    board = []
    idx = 0
    for i in range(N):
        board.append(list(nums[idx:idx+N]))
        idx+=N

    #Check row and column
    if checkRowAndCol(board,N) == True:
        subN = int(math.sqrt(N))
        #check subgrids
        i = 0
        while i < len(nums)-N:
            if i!= 0 and i%N==0:
                i+=(N*(subN-1))
            else:
                newBoard = []
                idx = i
                for j in range(subN):
                    newBoard.append(list(nums[idx:idx+subN]))
                    idx += N
                if checkSubGrid(newBoard, subN) == False:
                    return False
                i+=subN
        return True

    else:
        return False


def main(file_name):
    fileName = open(file_name, 'r')
    for line in fileName.readlines():
        line = re.sub(r'\n','', line)
        print(doStuff(line))

if __name__ == '__main__':
    main(sys.argv[1])
