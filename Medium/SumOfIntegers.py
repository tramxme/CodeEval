import sys, re

def doStuff(line):
    '''
    Definition: S[i] = the largest sum of contiguous integers including value at i
    Formula: S[i] = max(S[i-1] + a[i], a[i])
    Base case: S[0] = 0
    Solution: max of S
    '''
    nums = list(map(int, line.split(",")))
    S = [nums[0]]
    for i in range(1,len(nums)):
        S.append(max(S[i-1] + nums[i], nums[i]))
    print(max(S))

def main(file_name):
    fileName = open(file_name, 'r')
    for line in fileName.readlines():
        line = re.sub(r'\n','', line)
        doStuff(line)

if __name__ == '__main__':
    main(sys.argv[1])
