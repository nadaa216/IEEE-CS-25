import bisect

def minimal_r(n, m, cities, towers):
    max_distance = 0
    
    for city in cities:
        pos = bisect.bisect_left(towers, city)

        dist = float('inf')
        if pos < len(towers):  
            dist = min(dist, abs(city - towers[pos]))
        if pos > 0:  
            dist = min(dist, abs(city - towers[pos - 1]))
        max_distance = max(max_distance, dist)
    
    return max_distance

n, m = map(int, input().split())
cities = list(map(int, input().split()))
towers = list(map(int, input().split()))
print(minimal_r(n, m, cities, towers))
