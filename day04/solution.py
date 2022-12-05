def silver(pairs):
    output = 0

    for pair in pairs:
        if pair[0][0] <= pair[1][0] and pair[0][1] >= pair[1][1]:
            output += 1
        elif pair[1][0] <= pair[0][0] and pair[1][1] >= pair[0][1]:
            output += 1

    return output

def gold(pairs):
    output = 0

    for pair in pairs:
        if pair[0][0] <= pair[1][0] and pair[0][1] >= pair[1][0]:
            output += 1
        elif pair[1][0] <= pair[0][0] and pair[1][1] >= pair[0][0]:
            output += 1

    return output

pairs = []
with open("input.txt") as input:
    pair = input.readline()
    while pair:
        pair = pair.split(',')
        first = ''.join(pair[0]).split('-')
        second = ''.join(pair[1]).split('-')
        first = [int(first[0]), int(first[1])]
        second = [int(second[0]), int(second[1])]
        pairs.append([first, second])
        pair = input.readline()

print(f"{silver(pairs)}, {gold(pairs)}")
