def minimum_seconds_to_lineup(n, heights):
    # Find the position of the tallest and shortest soldiers
    max_height = max(heights)
    min_height = min(heights)
    
    # Position of the tallest soldier (from the beginning)
    max_pos = heights.index(max_height)
    
    # Position of the shortest soldier (from the end)
    min_pos = len(heights) - 1 - heights[::-1].index(min_height)
    
    # Calculate swaps
    if max_pos < min_pos:
        return max_pos + (n - 1 - min_pos)
    else:
        return max_pos + (n - 1 - min_pos) - 1

# Input
n = int(input())
heights = list(map(int, input().split()))

# Output
print(minimum_seconds_to_lineup(n, heights))
