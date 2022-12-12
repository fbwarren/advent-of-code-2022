from queue import PriorityQueue
import heapq as heap

input = open('input.txt')
lines = input.readlines()
grid = []
starts = []

for row, r in enumerate(lines):
    line = []
    for col, c in enumerate(r):
        if c == 'S':
            start = (row, col)
        if c == 'E':
            end = (row, col)
        if c == 'a':
            starts.append((row, col))
        line.append(c)
    line.pop()
    grid.append(line)
grid[start[0]][start[1]] = 'a'
grid[end[0]][end[1]] = 'z'

def dijkstras(grid, start):
    dirs = (0, 1, 0, -1, 0)
    visited = set()
    distances, prev = {}, {}
    queue = []
    distances[start] = 0
    heap.heappush(queue, (0, start))

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            cell = (row, col)
            if cell != start:
                distances[cell] = float('inf')
                prev[cell] = None
                heap.heappush(queue, (distances[cell], cell))

    while queue:
        _, u = heap.heappop(queue)
        visited.add(u)

        for i in range(4):
            v = (u[0]+dirs[i], u[1]+dirs[i+1])
            if v in visited:
                continue
            if (0 <= v[0] < len(grid)) and (0 <= v[1] < len(grid[0])):
                if ord(grid[v[0]][v[1]]) - ord(grid[u[0]][u[1]]) <= 1:
                    dist = distances[u] + 1
                    if dist < distances[v]:
                        distances[v] = dist
                        prev[v] = u
                        heap.heappush(queue, (dist, v))

    return distances

print(f'silver: {dijkstras(grid, start)[end]}')

distances = []
for start in starts:
    distances.append(dijkstras(grid, start)[end])
print(f'gold: {min(distances)}')

