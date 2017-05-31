import sys, re, math

'''
Find Duplicated Entry
Input:
5;0,1,2,3,0
20;0,1,10,3,2,4,5,7,6,8,11,9,15,12,13,4,16,18,17,14

Output:
0
4
'''

def doStuff(string):
    N, arr = string.split(";")
    N = int(N)
    arr = list(map(int, arr.split(",")))
    check = [False]*(N-1)
    for num in arr:
        if check[num] == False:
            check[num] = True
        else:
            return num


def main(file_name):
    fileName = open(file_name, 'r')
    for line in fileName.readlines():
        line = re.sub(r'\n','', line)
        print(doStuff(line))

if __name__ == '__main__':
    main(sys.argv[1])
