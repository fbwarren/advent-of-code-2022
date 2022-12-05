output = [0, 0, 0]
curr = 0

with open("input.txt") as input:
    line = input.readline()
    while line:
        if line != '\n':
            curr += int(line)
        else:
            if curr > output[0]:
                output = [curr, output[0], output[1]]
            elif curr > output[1]:
                output = [output[0], curr, output[1]]
            elif curr > output[2]:
                output = [output[0], output[1], curr]
            curr = 0
        line = input.readline()

print(sum(output))