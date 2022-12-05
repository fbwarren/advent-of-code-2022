alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
dict = {c: i+1 for i, c in enumerate(alphabet)}
output = 0

with open("input.txt") as input:
    sacks = [set(input.readline()[:-1]) for i in range(3)]
    while sacks[2]:
        repeat = (sacks[0] & sacks[1] & sacks[2]).pop()
        output += dict[repeat]
        sacks = [set(input.readline()[:-1]) for i in range(3)]

print(output)
