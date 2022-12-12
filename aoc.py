from collections import deque

def bfs(start, end, neighbors):
    parent = set()
    queue = deque([start])

    while queue:
        curr = queue.popleft()
        if curr == end:
            break

        for n in neighbors[curr]:
            if n in parent:
                continue
            parent[n] = curr
            queue.append(n)

    if end not in parent:
        return None

    pos = end
    path = []
    while pos != start:
        path.append(pos)
        pos = parent[pos]
    path.append(start)
    path.reverse()
    return path