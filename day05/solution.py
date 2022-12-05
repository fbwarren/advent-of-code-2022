from copy import deepcopy

stacks = [
    ['R','G','H','Q','S','B','T','N'],
    ['H','S','F','D','P','Z','J'],
    ['Z','H','V'],
    ['M','Z','J','F','G','H'],
    ['T','Z','C','D','L','M','S','R'],
    ['M','T','W','V','H','Z','J'],
    ['T','F','P','L','Z'],
    ['Q','V','W','S'],
    ['W','H','L','M','T','D','N','C']
]

stacks2 = deepcopy(stacks)

with open("input.txt") as input:
    for i in range(10):
        input.readline()

    move = input.readline()
    while move:
        move = move.split()
        num, src, dest = int(move[1]), int(move[3]), int(move[5])

        stacks2[dest-1] += stacks2[src-1][-num:]
        for _ in range(num):
            stacks[dest-1] += stacks[src-1][-1]
            stacks[src-1].pop()
            stacks2[src-1].pop()

        move = input.readline()

print(''.join([stack[-1] for stack in stacks]))
print(''.join([stack[-1] for stack in stacks2]))
