import sys, re

def doStuff(string):
    nums = list(map(int, string.split()))
    for i in range(len(nums)):
        if nums[i] in nums[i+1:]:
            return nums[i:(i + nums[i+1:].index(nums[i])+1)]

def main(file_name):
    fileName = open(file_name, 'r')
    for line in fileName.readlines():
        line = re.sub(r'\n','', line)
        L = doStuff(line)
        print(" ".join(str(x) for x in L))

if __name__ == '__main__':
    main(sys.argv[1])
