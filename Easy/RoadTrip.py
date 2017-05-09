import sys, re

def doStuff(string):
    pairs = string.split(";")
    D = []
    for p in pairs:
        p = p.strip()
        if len(p) != 0:
            D.append(int(p.split(",")[1]))

    D = sorted(D)
    res = [D[0]]
    prev = D[0]
    for v in D[1:]:
        res.append(v-prev)
        prev = v
    print(",".join(str(x) for x in res))

def main(file_name):
    fileName = open(file_name, 'r')
    for line in fileName.readlines():
        line = re.sub(r'\n','', line)
        doStuff(line)

if __name__ == '__main__':
    main(sys.argv[1])
