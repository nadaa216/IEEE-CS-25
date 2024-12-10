import sys
sys.setrecursionlimit(10**6)

def dfs(city, graph, visited, component):
    visited[city] = True
    component.append(city)
    for neighbor in graph[city]:
        if not visited[neighbor]:
            dfs(neighbor, graph, visited, component)

def solve(n, m, roads):
    # Step 1: Create graph representation
    graph = {i: [] for i in range(1, n + 1)}
    
    for a, b in roads:
        graph[a].append(b)
        graph[b].append(a)

    visited = [False] * (n + 1)  # To keep track of visited cities
    components = []

    # Step 2: Find connected components using DFS
    for i in range(1, n + 1):
        if not visited[i]:
            component = []
            dfs(i, graph, visited, component)
            components.append(component)

    # Step 3: Determine the roads to be added
    new_roads = []
    for i in range(1, len(components)):
        # Connect any city in the i-th component with any city in the 0-th component
        new_roads.append((components[0][0], components[i][0]))

    # Step 4: Output the result
    print(len(new_roads))
    for road in new_roads:
        print(road[0], road[1])

# Input handling
n, m = map(int, input().split())
roads = [tuple(map(int, input().split())) for _ in range(m)]

solve(n, m, roads)
