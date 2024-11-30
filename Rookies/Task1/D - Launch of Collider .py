def first_collision(n, directions, positions):
    min_time = float('inf')

    for i in range(n - 1):
        if directions[i] == 'R' and directions[i + 1] == 'L':
            
            collision_time = (positions[i + 1] - positions[i]) // 2
            min_time = min(min_time, collision_time)
    
    return min_time if min_time != float('inf') else -1

# Input
n = int(input())
directions = input().strip()
positions = list(map(int, input().split()))

# Output
print(first_collision(n, directions, positions))
