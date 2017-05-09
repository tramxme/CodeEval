import sys, re, math

def doStuff(string):
    string = re.sub(r'\n','', string)

    values = string.split(",")
    s1 = values[0]
    s2 = values[1]

    '''
    Definition: S[i][j] = 1 if the character is the same and 0 if not
    Formula: S[i][j] = 0 if s1[j] != s2[i]
    Base Case:
    Solution:
    '''

    S = [[0] * len(s1) for i in range(len(s2))]
    for i in range(len(s2)):
        if s2[i] == "*":
            if i - 1 >= 0 and s2[i-1] == "\\":
                for j in range(len(s1)):
                    if s2[i] == s1[j]:
                        S[i][j] = 1
            else:
                for j in range(len(s1)):
                    S[i][j] = 1
        else:
            for j in range(len(s1)):
                if s2[i] == s1[j]:
                    S[i][j] = 1

    print(S)

def main(file_name):
    fileName = open(file_name, 'r')
    for line in fileName.readlines():
        doStuff(line)

if __name__ == '__main__':
    main(sys.argv[1])


