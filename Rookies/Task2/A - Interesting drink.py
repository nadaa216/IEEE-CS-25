n = int(input())  
prices = list(map(int, input().split()))  
q = int(input())  
queries = [int(input()) for _ in range(q)]  
prices.sort()
results = []
for mi in queries:
    left, right = 0, n
    while left < right:
        mid = (left + right) // 2
        if prices[mid] <= mi:
            left = mid + 1  
        else:
            right = mid  
    results.append(left)  
print("\n".join(map(str, results)))

