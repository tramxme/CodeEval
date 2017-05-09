import sys, re, math

def isPrime(num):
    n = 3
    if num == 2:
        return True
    elif num % 2 == 0:
        return False
    else:
        while n <= math.sqrt(num):
            if num % n == 0:
                return False
            n += 2
    return True

def doStuff(string):
    string = re.sub(r'\n', '', string)
    N = int(string)

    res = [2]
    for i in range(3, N, 2):
        if isPrime(i) == True:
            res.append(i)

    print(",".join(str(x) for x in res))

def main(file_name):
    fileName = open(file_name, 'r')
    for line in fileName.readlines():
        doStuff(line)

if __name__ == '__main__':
    main(sys.argv[1])

