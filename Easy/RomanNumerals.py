import sys, re
numbers = [1,5,10,50,100,500,1000]
letters = ["I", "V", "X", "L", "C", "D", "M"]

def convert(num):
    if num in numbers:
        return letters[numbers.index(num)]
    elif num <= 3:
        return "I" * num
    elif num == 4:
        return "IV"
    elif num > 4 and num < 9:
        return "V" + convert(num-5)
    elif num == 9:
        return "IX"
    elif num <= 30:
        return "X" * (num//10)
    elif num == 40:
        return "XL"
    elif num > 50 and num < 90:
        return "L" + convert(num-50)
    elif num == 90:
        return "XC"
    elif num <= 300:
        return "C" * (num//100)
    elif num == 400:
        return "CD"
    elif num > 400 and num < 900:
        return "D" + convert(num-500)
    elif num == 900:
        return "CM"
    elif num <= 3000:
        return "M" * (num//1000)


def doStuff(string):
    num = int(string)
    res = ""
    size = len(string)
    while size > 0:
        temp = num
        num = num%(10**(size-1))
        temp -= num
        res += convert(temp)
        size -= 1
    print(res)

def main(file_name):
    fileName = open(file_name, 'r')
    for line in fileName.readlines():
        line = re.sub(r'\n','', line)
        doStuff(line)

if __name__ == '__main__':
    main(sys.argv[1])
