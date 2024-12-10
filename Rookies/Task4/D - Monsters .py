from collections import deque

def escape_labyrinth(n, m, grid):
    directions = [(0, 1, 'R'), (0, -1, 'L'), (1, 0, 'D'), (-1, 0, 'U')]
    
    time = [[[float('inf')] * 2 for _ in range(m)] for _ in range(n)]  
    parent = [[None] * m for _ in range(n)]
    
    monster_queue = deque()
    player_queue = deque()
    start = None
    
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'M':
                monster_queue.append((i, j))
                time[i][j][1] = 0  
            if grid[i][j] == 'A':
                start = (i, j)
                player_queue.append((i, j))
                time[i][j][0] = 0  
    
    if not start:
        return "NO"  
    
    while monster_queue:
        x, y = monster_queue.popleft()
        for dx, dy, _ in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == '.' and time[nx][ny][1] == float('inf'):
                time[nx][ny][1] = time[x][y][1] + 1
                monster_queue.append((nx, ny))
    
    while player_queue:
        x, y = player_queue.popleft()
        
        if x == 0 or x == n-1 or y == 0 or y == m-1:
            path = []
            while parent[x][y]:
                px, py, move = parent[x][y]
                path.append(move)
                x, y = px, py
            return f"YES\n{len(path)}\n{''.join(reversed(path))}"
        
        for dx, dy, move in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == '.' and time[nx][ny][0] == float('inf'):
                if time[x][y][0] + 1 < time[nx][ny][1]:
                    time[nx][ny][0] = time[x][y][0] + 1
                    parent[nx][ny] = (x, y, move)
                    player_queue.append((nx, ny))
    
    return "NO"

n, m = map(int, input().split())
grid = [input().strip() for _ in range(n)]

print(escape_labyrinth(n, m, grid))
