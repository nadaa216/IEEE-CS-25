from collections import deque

def knight_moves(start, destination):
    directions = [
        (2, 1), (2, -1), (-2, 1), (-2, -1),
        (1, 2), (1, -2), (-1, 2), (-1, -2)
    ]

    def pos_to_indices(pos):
        return ord(pos[0]) - ord('a'), int(pos[1]) - 1

    def is_within_bounds(x, y):
        return 0 <= x < 8 and 0 <= y < 8

    start_x, start_y = pos_to_indices(start)
    dest_x, dest_y = pos_to_indices(destination)

    if (start_x, start_y) == (dest_x, dest_y):
        return 0

    queue = deque([(start_x, start_y, 0)])
    visited = set()
    visited.add((start_x, start_y))

    while queue:
        x, y, moves = queue.popleft()

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (nx, ny) == (dest_x, dest_y):
                return moves + 1
            if is_within_bounds(nx, ny) and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny, moves + 1))

def solve_knight_problem(test_cases):
    results = []
    for start, destination in test_cases:
        results.append(knight_moves(start, destination))
    return results

t = int(input())
test_cases = [input().split() for _ in range(t)]
results = solve_knight_problem(test_cases)
print("\n".join(map(str, results)))
