DISK_SPACE = 70000000
NEEDED_SPACE = 30000000

class Node:
    def __init__(self, parent, children, size):
        self.parent = parent
        self.children = children
        self.size = size

def dfs(node, silver, gold, goldSize):
    for child in node.children.values():
        node.size += dfs(child, silver, gold, goldSize)
    if node.size <= 100000:
        silver[0] += node.size
    if node.size >= 1072511:
        gold[0] = min(gold[0], node.size)
    return node.size

root = Node(None, {}, 0)
input = open("input.txt")
line = input.readline()
line = input.readline()
curr = root

while line:
    line = line.split()
    if line[0] == '$':
        if line[1] == 'cd':
            if line[2] == '..':
                curr = curr.parent
            else:
                curr = curr.children[line[2]]
    elif line[0] == 'dir':
        if line[1] not in curr.children:
            curr.children[line[1]] = Node(curr, {}, 0)
    else:
        curr.size += int(line[0])
    line = input.readline()

silver, gold = [0], [float('inf')]
dfs(root, silver, gold, NEEDED_SPACE - DISK_SPACE + root.size)
print(f"silver: {silver}\ngold: {gold}\n")