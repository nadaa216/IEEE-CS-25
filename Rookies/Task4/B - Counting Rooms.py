from collections import deque

def bfs(x, y, grid, visited, n, m):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    queue = deque([(x, y)])
    visited[x][y] = True

    while queue:
        cx, cy = queue.popleft()
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and grid[nx][ny] == '.':
                visited[nx][ny] = True
                queue.append((nx, ny))

def count_rooms(grid, n, m):
    visited = [[False] * m for _ in range(n)]
    room_count = 0

    for i in range(n):
        for j in range(m):
            if grid[i][j] == '.' and not visited[i][j]:
                bfs(i, j, grid, visited, n, m)
                room_count += 1

    return room_count

n, m = map(int, input().split())
grid = [input().strip() for _ in range(n)]

print(count_rooms(grid, n, m))
