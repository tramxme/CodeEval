import sys, re, math
digits = [["-**--", "*--*-", "*--*-", "*--*-", "-**--", "-----"],\
        ["--*--", "-**--", "--*--", "--*--", "-***-", "-----"],\
        ["***--", "---*-", "-**--", "*----", "****-", "-----"],\
        ["***--", "---*-", "-**--", "---*-", "***--", "-----"],\
        ["-*---", "*--*-", "****-", "---*-", "---*-", "-----"],\
        ["****-", "*----", "***--", "---*-", "***--", "-----"],\
        ["-**--", "*----", "***--", "*--*-", "-**--", "-----"],\
        ["****-", "---*-", "--*--", "-*---", "-*---", "-----"],\
        ["-**--", "*--*-", "-**--", "*--*-", "-**--", "-----"],\
        ["-**--", "*--*-", "-***-", "---*-", "-**--", "-----"]]

def doStuff(string):
    string = re.sub(r"[\D+]", "", string)
    res = [""] * 6
    for char in list(string):
        for i in range(6):
            res[i] += digits[int(char)][i]

    return "\n".join(res)

def main(file_name):
    fileName = open(file_name, 'r')
    for line in fileName.readlines():
        line = re.sub(r'\n','', line)
        print(doStuff(line))

if __name__ == '__main__':
    main(sys.argv[1])

