def max_books(n, t, a):
    
    left = 0  
    current_time = 0  
    max_books = 0 

    for right in range(n):
        current_time += a[right]  
        
        
        while current_time > t:
            current_time -= a[left]
            left += 1
        
        max_books = max(max_books, right - left + 1)
    
    return max_books


def main():
   
    n, t = map(int, input().split())
    a = list(map(int, input().split()))
    
   
    print(max_books(n, t, a))
if __name__ == "__main__":
    main()
