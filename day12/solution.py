from collections import deque

grid = [list(x) for x in open('input.txt').read().strip().split('\n')]
starts = []

for row in range(len(grid)):
    for col in range(len(grid[0])):
        if grid[row][col] == 'S':
            start = (row, col)
            grid[row][col] = 'a'
        elif grid[row][col] == 'E':
            end = (row, col)
            grid[row][col] = 'z'
        elif grid[row][col] == 'a':
            starts.append((row, col))

def bfs(start, end):
    dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
    parent = {}
    queue = deque([start])

    while queue:
        u = queue.popleft()
        if u == end:
            break
        for dir in dirs:
            v = (u[0] + dir[0], u[1] + dir[1])
            if v in parent:
                continue
            if (0 <= v[0] < len(grid)) and (0 <= v[1] < len(grid[0])):
                if ord(grid[v[0]][v[1]]) - ord(grid[u[0]][u[1]]) <= 1:
                    parent[v] = u
                    queue.append(v)

    if end not in parent:
        return float('inf')

    output = 0 
    while end != start:
        end = parent[end]
        output += 1

    return output

print(f'silver: {bfs(start, end)}')
print(f'gold: {min([bfs(start, end) for start in starts])}')