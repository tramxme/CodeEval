import sys, re
alphabet = "abcdefghijklmnopqrstuvwxyz"

def getVal(string):
    string = re.sub(r'\n', '', string)
    string = string.lower()
    total = 0
    string_dict = {}
    for char in string:
        if char in alphabet:
            if char not in string_dict.keys():
                string_dict.setdefault(char, 1)
            else:
                string_dict[char] += 1
    values = sorted(string_dict.values(), reverse=True)
    i = 26
    for v in values:
        total += i * v
        i -= 1

    print(total)


def main(file_name):
    fileName = open(file_name, 'r')
    for line in fileName.readlines():
        getVal(line)

if __name__ == '__main__':
    main(sys.argv[1])
