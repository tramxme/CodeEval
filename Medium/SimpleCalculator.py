import sys, re, math

'''
Create a simple calculator.
Input:
250*14.3
3^6 / 117
(2.16 - 48.34)^-1
(59 - 15 + 3*6)/21

Output:
3575
6.23077
−0.02165
2.95238
'''

'''
1   ()       Brackets
2   -        Unary minus
3   ^        Exponent
4   *, /     Multiply, Divide (left-to-right precedence)
5   +, -     Add, Subtract (left-to-right precedence)
'''
order = [["()"], ["-"], ["^"],["*", "/"],["+", "-"]]

def Do_Calculation(string):
    return 0


def main(file_name):
    fileName = open(file_name, 'r')
    for line in fileName.readlines():
        line = re.sub(r'\n','', line)
        print(Do_Calculation(line))

if __name__ == '__main__':
    main(sys.argv[1])
