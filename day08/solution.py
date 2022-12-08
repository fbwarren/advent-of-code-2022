input = open("input.txt")
lines = input.read().splitlines()
grid = [[int(char) for char in line] for line in lines] 
ROWS, COLS = len(grid), len(grid[0])

def is_visible(x, y):
    if x == 0 or y == 0 or x+1 == ROWS or y+1 == COLS:
        return True
    tree = grid[y][x]
    if all(t < tree for t in grid[y][:x]): #check left
        return True
    elif all(t < tree for t in grid[y][x+1:]): #check right
        return True
    elif all(tree_row[x] < tree for tree_row in grid[:y]): #check up
        return True
    elif all(tree_row[x] < tree for tree_row in grid[y+1:]): #check down
        return True
    else:
        return False

def scenic_score(x, y):
    if x == 0 or y == 0 or x+1 == ROWS or y+1 == COLS:
        return 0
    score = 1
    tree = grid[y][x]

    count = 0
    for i in range(x-1, -1, -1):
        count += 1
        if tree <= grid[y][i]:
            break
    score *= max(count, 1)

    count = 0
    for i in range(x+1, COLS):
        count += 1
        if tree <= grid[y][i]:
            break
    score *= max(count, 1)

    count = 0
    for i in range(y-1, -1, -1):
        count += 1
        if tree <= grid[i][x]:
            break
    score *= max(count, 1)

    count = 0
    for i in range(y+1, ROWS):
        count += 1
        if tree <= grid[i][x]:
            break
    score *= max(count, 1)

    return score

silver = sum(is_visible(x, y) for x in range(ROWS) for y in range(COLS))
gold = max((scenic_score(x, y)) for x in range(ROWS) for y in range(COLS))

print(f'silver: {silver}\ngold: {gold}')