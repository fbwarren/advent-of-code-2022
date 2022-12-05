output = 0
scores = {
    "A X": 4, "A Y": 8, "A Z": 3,
    "B X": 1, "B Y": 5, "B Z": 9,
    "C X": 7, "C Y": 2, "C Z": 6
}

with open("input.txt") as input:
    line = input.readline()
    while line:
        output += scores[line[:-1]]
        line = input.readline()

print(output)
