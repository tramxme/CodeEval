import sys, re

def doStuff(line):
    nums = list(map(int, line.split()))
    n = nums[0]
    values = []
    values.extend(range(1,n))
    nums = nums[1:]
    for i in range(1, n):
        diff = abs(nums[i] - nums[i-1])
        if diff in values:
            values.remove(diff)
        else:
            return "Not jolly"
    return "Jolly"

def main(file_name):
    fileName = open(file_name, 'r')
    for line in fileName.readlines():
        line = re.sub(r'\n','', line)
        print(doStuff(line))

if __name__ == '__main__':
    main(sys.argv[1])

