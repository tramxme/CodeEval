import sys, re, math

'''
Definition: W[i][j] = the maximum number of ways to make change for i (cent) from the first j values
Formula: W[i][j] = W[i-1][j]+W[i][i-num]
Base Case: W[i][0] = 1 - There's always 1 way to change 0 cents
Solution: W[i][j]
'''
def doStuff(string):
    changes = [1,5,10,25,50]
    num = int(string)
    W = [[0] * (num+1) for i in range(len(changes)+1)]

    for i in range(len(changes)+1):
        W[i][0] = 1

    for i in range(1, num+1):
        W[0][i] = 0

    for row in range(1,len(changes)+1):
        for col in range(1,num+1):
            if col - changes[row-1] < 0:
                W[row][col] = W[row-1][col]
            else:
                W[row][col] = W[row-1][col] + W[row][col-changes[row-1]]

    return W[len(changes)][num]

def main(file_name):
    fileName = open(file_name, 'r')
    for line in fileName.readlines():
        line = re.sub(r'\n','', line)
        print(doStuff(line))

if __name__ == '__main__':
    main(sys.argv[1])

