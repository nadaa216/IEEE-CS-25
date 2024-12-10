from collections import deque

def find_path(n, m, grid):
    start, end = None, None
    directions = [(0, 1, 'R'), (0, -1, 'L'), (1, 0, 'D'), (-1, 0, 'U')]
    
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'A':
                start = (i, j)
            if grid[i][j] == 'B':
                end = (i, j)
    
    queue = deque([start])
    visited = [[False] * m for _ in range(n)]
    parent = [[None] * m for _ in range(n)]
    
    visited[start[0]][start[1]] = True
    
    while queue:
        x, y = queue.popleft()
        if (x, y) == end:
            break
        for dx, dy, move in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and grid[nx][ny] != '#':
                visited[nx][ny] = True
                parent[nx][ny] = (x, y, move)
                queue.append((nx, ny))
    
    if not visited[end[0]][end[1]]:
        return "NO"
    
    path = []
    cx, cy = end
    while (cx, cy) != start:
        px, py, move = parent[cx][cy]
        path.append(move)
        cx, cy = px, py
    
    return f"YES\n{len(path)}\n{''.join(reversed(path))}"

n, m = map(int, input().split())
grid = [input().strip() for _ in range(n)]

print(find_path(n, m, grid))
