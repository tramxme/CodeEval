'''
CHALLENGE DESCRIPTION:

Long serious texts are boring. Write a program that will make texts more informal: replace every other end punctuation mark (period ‘.’, exclamation mark ‘!’, or question mark ‘?’) with one of the following slang phrases, selecting them one after another:

‘, yeah!’
‘, this is crazy, I tell ya.’
‘, can U believe this?’
‘, eh?’
‘, aw yea.’
‘, yo.’
‘? No way!’
‘. Awesome!’
The result should be funny.

CONSTRAINTS:

In the input text, end punctuation mark cannot come one after another (consequent).
Input text contains 40 lines.

'''
import sys, re, math

const = [", yeah!", ", this is crazy, I tell ya.", ", can U believe this?", ", eh?", ", aw yea.", ", yo.", "? No way!", ". Awesome!"]

idx = 0
count = 0

def doStuff(string):
    string = re.sub(r'\n','', string)
    global idx, count
    res = ""
    for char in string:
        if char in ".!?":
            if (count%2 != 0):
                res += const[idx]
                idx += 1
                idx %= len(const)
            else:
                res += char
            count += 1
        else:
            res += char
    print(res)

def main(file_name):
    fileName = open(file_name, 'r')
    for line in fileName.readlines():
        doStuff(line)

if __name__ == '__main__':
    main(sys.argv[1])
