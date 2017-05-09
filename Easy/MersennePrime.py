import sys, re, math
def isPrime(num):
    n = 3
    if num % 2 == 0:
        return False
    else:
        while n <= math.sqrt(num):
            if num % n == 0:
                return False
            n += 2
        return True

#Mersenne Number = 2**p - 1 with p restricted to prime numbers
def doStuff(string):
    num = int(string)
    n = 3
    L = [3]
    while (2**n-1) < num:
        if isPrime(n) == True:
            L.append(2**n - 1)
        n += 2

    print(", ".join(str(x) for x in L))


def main(file_name):
    fileName = open(file_name, 'r')
    for line in fileName.readlines():
        line = re.sub(r'\n','', line)
        doStuff(line)

if __name__ == '__main__':
    main(sys.argv[1])
