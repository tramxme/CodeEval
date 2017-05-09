import sys, re

def doStuff(string):
    L = string.split()
    new_L = []
    for t in L:
        new_L.append(int("".join(t.split(":"))))
    new_L = sorted(new_L, reverse=True)
    new_L = list(map(str, new_L))
    ret = []
    for t in new_L:
        while len(t) < 6:
            t = "0" + t
        res = t[0:2]+":"+t[2:4]+":"+t[4:6]
        ret.append(res)
    print(" ".join(ret))

def main(file_name):
    fileName = open(file_name, 'r')
    for line in fileName.readlines():
        line = re.sub(r'\n','', line)
        doStuff(line)

if __name__ == '__main__':
    main(sys.argv[1])
