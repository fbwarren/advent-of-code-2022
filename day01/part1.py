output = 0
curr = 0

with open("input.txt") as input:
    line = input.readline()
    while line:
        if line != '\n':
            curr += int(line)
        else:
            output = max(curr, output)
            curr = 0
        line = input.readline()

print(output)