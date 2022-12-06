line = open("input.txt").readline()

def solve(n):
    for i in range(len(line)):
        if len(set(line[i:i+n])) == n:
            return i+n

print("Silver: %s\nGold: %s" % (solve(4), solve(14)))

