import sys, re

def beats(locks):
    for i in range(1, len(locks), 2):
        locks[i] = True
    for i in range(2, len(locks), 3):
        locks[i] = not locks[i]
    return locks

def doStuff(line):
    nums, iteration = list(map(int, line.split()))
    locks = [False] * nums #False for unlocked and True for locked
    i = 0
    while i < iteration-1:
        locks = beats(locks)
        i+=1

    #last iteration, the security guard just changes the state of the last door in a row
    locks[-1] = not locks[-1]

    count = 0
    for l in locks:
        if l == False:
            count += 1
    print(count)

def main(file_name):
    fileName = open(file_name, 'r')
    for line in fileName.readlines():
        line = re.sub(r'\n','', line)
        doStuff(line)

if __name__ == '__main__':
    main(sys.argv[1])
