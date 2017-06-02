import sys, re, math

def doStuff(string):
    #Get the grid
    arr = string.split(" | ")
    grid = []
    for s in arr:
        grid.append(list(s))

    #Keep track of the number of times you can make the word
    #using a 2x2 submatrix
    count = 0

    #Checking every 2x2 submatrix in the grid
    for row in range(len(grid)-1):
        for col in range(len(grid[0])-1):
            submatrix = [grid[row][col], grid[row][col+1], grid[row+1][col], grid[row+1][col+1]]
            if sorted(submatrix) == sorted("code"):
                count+=1

    return count


def main(file_name):
    fileName = open(file_name, 'r')
    for line in fileName.readlines():
        line = re.sub(r'\n','', line)
        print(doStuff(line))

if __name__ == '__main__':
    main(sys.argv[1])
