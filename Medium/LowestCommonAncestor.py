import sys, re
class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

#Create the tree
head = Node(30, Node(8, Node(3, None, None), Node(20, Node(10, None, None), Node(29, None, None))),\
        Node(52, None, None))

def doStuff(tree, v1, v2):


def main(file_name):
    fileName = open(file_name, 'r')
    for line in fileName.readlines():
        line = re.sub(r'\n','', line)
        v1, v2 = list(map(int, line.split()))
        doStuff(head, v1, v2)

if __name__ == '__main__':
    main(sys.argv[1])

