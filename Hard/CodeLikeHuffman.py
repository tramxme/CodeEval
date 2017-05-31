import sys, re, queue
res = None

class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

    def __eq__(self, other):
        if self is None:
            return other is None
        else:
            if other is None:
                return False
            return self.value == other.value and self.left == other.left and self.right == other.right

    #If 2 Nodes have same priority then sorting should be done in an alphabetical order.
    def __lt__(self, other):
        if self == None:
            return other != None
        else:
            if other == None:
                return False
            if self.value == other.value:
                if self.left == other.left:
                    return self.right < other.right
                else:
                    return self.left < other.left
            else:
                return self.value < other.value

    def __gt__(self, other):
        if self == None:
            return other != None
        else:
            if other == None:
                return True
            if self.value == other.value:
                if self.left == other.left:
                    return self.right > other.right
                else:
                    return self.left > other.left
            else:
                return self.value > other.value

def getLeafValue(head, s):
    global res
    if head == None: return
    if head.left == None and head.right == None:
        res[head.value] = s
        return
    getLeafValue(head.left, s+"0")
    getLeafValue(head.right, s+"1")

def doStuff(line):
    global res

    chars = {}
    for c in line:
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1

    nodes = queue.PriorityQueue()
    for c in chars:
        nodes.put((chars[c], c, Node(c, None, None)))

    #When building a binary tree, if the priority of items is the same, the sorting should be done in an alphabetical order
    #If the priority of items is the same then Node has higher priority than symbol.
    #If 2 Nodes have same priority then sorting should be done in an alphabetical order.
    tree = None
    while nodes.qsize() >= 2:
        n1 = nodes.get()
        n2 = nodes.get()
        if n1[0] <= n2[0]:
            nodes.put((n1[0] + n2[0], "*", Node("*", n1[2], n2[2])))
        else:
            nodes.put((n1[0] + n2[0], "*", Node("*", n2[2], n1[2])))


    tree = nodes.get()[2]

    #Now traverse the tree and print out the characters and its value
    getLeafValue(tree, "")
    temp = sorted(res.items())
    s = ""
    for p in temp:
        s += p[0] + ": " + p[1] + "; "
    print(s.rstrip(" "))

def main(file_name):
    fileName = open(file_name, 'r')
    global res
    for line in fileName.readlines():
        line = re.sub(r'\n','', line)
        res = dict()
        doStuff(line)

if __name__ == '__main__':
    main(sys.argv[1])
