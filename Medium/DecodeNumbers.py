import sys, re

'''
Definition: D[i] = The total number of ways to decode numbers including num[i]
Formula: D[i] = D[i-1] if the number @ i combined with number @ (i-1) is within the range
10-26 then we need to add D[i-2] because it's another mutation
Base case: D[0] = 1
Solution: D[n]
'''
def doStuff(line):
    #Using 2D array and place the digits in the top row for easy visual
    D = [[0] * (len(line)+1) for i in range(2)]

    D[1][0] = 1 #Set dummy column at 0 and
    D[1][1] = 1 #There's 1 way to decode if there's only 1 digit

    i = 1
    for c in list(line):
        D[0][i] = c
        i += 1

    for i in range(2, len(line)+1):
        n = int(D[0][i-1] + D[0][i])
        D[1][i] = D[1][i-1]
        if n >= 10 and n <= 26:
            D[1][i] += D[1][i-2]

    return(D[1][len(line)])


def main(file_name):
    fileName = open(file_name, 'r')
    for line in fileName.readlines():
        line = re.sub(r'\n','', line)
        print(doStuff(line))

if __name__ == '__main__':
    main(sys.argv[1])
