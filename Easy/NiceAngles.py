import sys, re

def doStuff(string):
    values = string.split(".")
    res = values[0] + "."
    values = str((int(values[1])/(10 ** len(values[1]))*60)).split(".")
    if len(values[0])< 2:
        res += "0" + values[0] + "'"
    else:
        res += values[0][:2] + "'"
    values = str((int(values[1])/(10 ** len(values[1]))*60)).split(".")

    if len(values[0])< 2:
        res += "0" + values[0] + "\""
    else:
        res += values[0][:2] + "\""
    print(res)


def main(file_name):
    fileName = open(file_name, 'r')
    for line in fileName.readlines():
        line = re.sub(r'\n','', line)
        doStuff(line)

if __name__ == '__main__':
    main(sys.argv[1])

