import sys, re, math

def doStuff(string):
    string = re.sub(r'\n','', string)

    res = word = ""
    size = 0
    for w in string.split():
        if len(w) > size:
            size = len(w)
            word = w

    i = 0
    for j in range(size):
        res += "*" * i + word[j] + " "
        i += 1

    print(res.strip())


def main(file_name):
    fileName = open(file_name, 'r')
    for line in fileName.readlines():
        doStuff(line)

if __name__ == '__main__':
    main(sys.argv[1])




