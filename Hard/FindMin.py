import sys, re, math

def doStuff(string):
    n,k,a,b,c,r = list(map(int, string.split(",")))

    '''
    Array M containing all the known numbers until k
    '''
    M = [a]
    for i in range(1, k):
        v = (b * M[i-1] + c) % r
        M.append(v)

    '''
    for each index i, where k <= i < n, m is the minimum non-negative integer
    which is not contained in the previous k values of m
    '''
    while len(M) < n:
        v = 0
        while v in M[len(M)-k:len(M)]:
            v += 1
        M.append(v)

    print(M[n-1])



def main(file_name):
    fileName = open(file_name, 'r')
    for line in fileName.readlines():
        line = re.sub(r'\n','', line)
        doStuff(line)

if __name__ == '__main__':
    main(sys.argv[1])


