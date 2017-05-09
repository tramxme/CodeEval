import sys, re

def doStuff(arr):
    end = max(arr)
    start = min(arr)
    MD = []
    while start <= end:
        diff = 0
        for i in range(len(arr)):
            diff += abs(start - arr[i])
        MD.append(diff)
        start += 1
    print(min(MD))

def main(file_name):
    fileName = open(file_name, 'r')
    for line in fileName.readlines():
        line = re.sub(r'\n', '', line)
        nums = list(map(int, line.split()))
        doStuff(nums[1:])

if __name__ == '__main__':
    main(sys.argv[1])

