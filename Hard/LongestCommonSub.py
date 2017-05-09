import sys, re, math

def getMax(arr, row, col):
    res = ""
    for i in range(row):
        for j in range(col):
            v = arr[i][j]
            if len(v) > len(res):
                res = v
    return res

def doStuff(string):
    string = re.sub(r'\n','', string)

    values = string.split(";")
    s1 = values[0]
    s2 = values[1]

    '''
    Definition: LCS[i][j] = The maximum number of the longest common subsequence at i and j
    Formula: LCS[i][j] = max{LCS[m][n]} + 1 (where m < i and n < j)
    Base Case: LCS[i][0] = 0, LCS[0][j] = 0
    Solution: Trace back from the highest number
    '''

    LCS = [[""] * len(s1) for i in range(len(s2))]
    for i in range(len(s2)):
        for j in range(len(s1)):
            if s2[i] == s1[j]:
                if i == 0:
                    LCS[i][j] = s1[j]
                else:
                    Max = getMax(LCS, i, j)
                    LCS[i][j] = Max + s1[j]
    #print(LCS)
    print(getMax(LCS,len(s2), len(s1)))



def main(file_name):
    fileName = open(file_name, 'r')
    for line in fileName.readlines():
        doStuff(line)

if __name__ == '__main__':
    main(sys.argv[1])


