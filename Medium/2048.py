import sys, re, math

def merge(arr, direction):
    newArr = []
    add = False

    #Left and UP merge
    if direction == -1:
        i = 0
        while i < len(arr):
            if arr[i] != 0:
                if len(newArr) > 0 and newArr[-1] == arr[i] and (not add):
                    newArr[-1] *= 2
                    add = True
                else:
                    newArr.append(arr[i])
                    add = False

            i+=1

    #Right and Down merge
    elif direction == 1:
        i = len(arr)-1
        while i >= 0:
            if arr[i] != 0:
                if len(newArr) > 0 and newArr[0] == arr[i] and (not add):
                    newArr[0] *= 2
                    add = True
                else:
                    newArr.insert(0, arr[i])
                    add = False

            i-=1

    return newArr

def addZeros(arr, size, direction):
    for i in range(size - len(arr)):
        if direction == -1:
            arr.append(0)
        elif direction == 1:
            arr.insert(0,0)

    return arr

move = {"UP": -1, "DOWN": 1, "RIGHT": 1, "LEFT": -1}

def playGame(direction, gridSize, rows):

    if direction == "RIGHT" or direction == "LEFT":
        for i in range(gridSize):
            row = merge(rows[i], move[direction])
            rows[i] = addZeros(row, gridSize, move[direction])

    elif direction == "UP" or direction == "DOWN":
        for col in range(gridSize):
            arr = []
            for row in range(gridSize):
                arr.append(rows[row][col])
            arr = merge(arr, move[direction])
            arr = addZeros(arr, gridSize, move[direction])
            for row in range(gridSize):
                rows[row][col] = arr[row]

    ret = ""
    for row in rows:
        ret += " ".join(str(x) for x in row) + "|"
    return ret.rstrip("|")


def main(file_name):
    fileName = open(file_name, 'r')
    for line in fileName.readlines():
        line = re.sub(r'\n','', line)
        cmds = line.split(";")
        direction = cmds[0]
        gridSize = int(cmds[1])
        rows = []
        config = cmds[2].split("|")
        for r in config:
            rows.append(list(map(int, r.strip().split(" "))))
        print(playGame(direction, gridSize, rows))

if __name__ == '__main__':
    main(sys.argv[1])
