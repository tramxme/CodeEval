import sys, re

def doStuff(num):
    seq = [0,1]
    while(num > len(seq)):
        addSeq = seq[len(seq)//2:]
        for n in seq[:len(seq)//2]:
            if n == 0: addSeq.append(1)
            elif n == 1: addSeq.append(2)
            elif n == 2: addSeq.append(0)
        seq.extend(addSeq)
    print(seq[num])
    return

def main(file_name):
    fileName = open(file_name, 'r')
    for line in fileName.readlines():
        line = re.sub(r'\n','', line)
        doStuff(int(line))

if __name__ == '__main__':
    main(sys.argv[1])

