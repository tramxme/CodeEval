import sys, re, math

def doStuff(stairs):
    S = [1,2]
    for i in range(2, stairs):
        S.append(S[i-2] + S[i-1])
    print(S[stairs-1])

def main(file_name):
    fileName = open(file_name, 'r')
    for line in fileName.readlines():
        line = re.sub(r'\n','', line)
        doStuff(int(line))

if __name__ == '__main__':
    main(sys.argv[1])
