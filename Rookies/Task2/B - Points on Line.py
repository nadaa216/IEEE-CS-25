def binary_search(points, left, target):
    """Find the largest index `j` such that points[j] <= target."""
    low, high = left, len(points) - 1
    while low <= high:
        mid = (low + high) // 2
        if points[mid] <= target:
            low = mid + 1
        else:
            high = mid - 1
    return high

n, d = map(int, input().split())
x = list(map(int, input().split()))

count = 0

for i in range(n):
    j = binary_search(x, i, x[i] + d)
    k = j - i
    if k >= 2:
        count += k * (k - 1) // 2  
print(count)
