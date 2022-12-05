alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
dict = {c: i+1 for i, c in enumerate(alphabet)}
output = 0

with open("input.txt") as input:
    line = input.readline()
    while line:
        size = (len(line) - 1) // 2
        left, right = set(line[:size]), set(line[size:-1])
        repeat = (left & right).pop()
        output += dict[repeat]
        line = input.readline()

print(output)
