def count_pairs_with_sum(n, l, r, arr):
   
    arr.sort()
    count = 0
    
    for i in range(n):
       
        left = i + 1
        right = n - 1
        
       
        while left <= right:
            mid = (left + right) // 2
            if arr[i] + arr[mid] >= l:
                right = mid - 1
            else:
                left = mid + 1
        
        low = left 
        
        left = i + 1
        right = n - 1
        
     
        while left <= right:
            mid = (left + right) // 2
            if arr[i] + arr[mid] <= r:
                left = mid + 1
            else:
                right = mid - 1
        
        high = right  
        
        
        if low <= high:
            count += (high - low + 1)
    
    return count


def main():
    t = int(input())  
    results = []
    
    for _ in range(t):
      
        n, l, r = map(int, input().split())
        arr = list(map(int, input().split()))
        
       
        results.append(count_pairs_with_sum(n, l, r, arr))
    
  
    for result in results:
        print(result)


if __name__ == "__main__":
    main()
