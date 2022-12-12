directions = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}
input = open("input.txt")
line = input.readline()
visited = set([(0,0)])

def isTouching(head, tail):
    return abs(head[0] - tail[0]) <= 1 and abs(head[1] - tail[1]) <= 1


def move(dir, head, tail):
    prev = head
    newTail = tail
    newHead = (head[0] + directions[dir][0], head[1] + directions[dir][1])
    if not isTouching(newHead, tail):
        newTail = prev
        visited.add(newTail)
    return newHead, newTail

head, tail = (0, 0), (0, 0)
while line:
    line = line.split()
    for i in range(int(line[1])):
        head, tail = move(line[0], head, tail)
    line = input.readline()

print(len(visited))