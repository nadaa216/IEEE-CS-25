def total_lines(v, k):
    total = 0
    while v > 0:
        total += v
        v //= k
    return total

def find_minimum_v(n, k):
    left, right = 1, n  
    
    while left < right:
        mid = (left + right) // 2
        if total_lines(mid, k) >= n:
            right = mid  
        else:
            left = mid + 1  
    
    return left
n, k = map(int, input().split())
print(find_minimum_v(n, k))
