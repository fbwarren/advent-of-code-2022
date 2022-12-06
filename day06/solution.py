from collections import deque

with open("input.txt") as input:
    msg = input.readline()
    found = False

    for i in range(len(msg)):
        if len(set(msg[i:i+4])) == 4 and not found:
            print('four: {}'.format(i+4))
            found = True
        if len(set(msg[i:i+14])) == 14:
            print('fourteen: {}'.format(i+14))
            break
