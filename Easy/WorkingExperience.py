import sys, re
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul",\
        "Aug", "Sep", "Oct", "Nov", "Dec"]

def isConflict(L,time):
    start_M, start_Y = start.split()
    end_M, end_Y = end.split()
    time_M, time_Y = time.split()
    return time_Y >= start_Y and time_Y <= end_Y:

def doStuff(string):
    periods = string.split(";")
    time = 0
    L = []
    for p in periods:
        values = p.split("-")
        pair = [values[0], values[1]]


    print(time//12)



def main(file_name):
    fileName = open(file_name, 'r')
    for line in fileName.readlines():
        line = re.sub(r'\n','', line)
        doStuff(line)

if __name__ == '__main__':
    main(sys.argv[1])
