import sys, re, math

def isValid(num1, num2):
    s1 = str(num1)
    s2 = str(num2)

    v = 0
    for c in s1:
        v += int(c)

    for c in s2:
        v += int(c)

    return (v <= 19)

def main():
    res = 0
    M = []
    i = 0
    while True:
        j = 0
        arr = []
        while True:


    print(res)



if __name__ == '__main__':
    main()
