def max_books(n, t, books):
    left = 0
    current_time = 0
    max_books_read = 0
    for right in range(n):
        current_time += books[right]
        while current_time > t:
            current_time -= books[left]
            left += 1
        max_books_read = max(max_books_read, right - left + 1)
    
    return max_books_read
n, t = map(int, input().split())
books = list(map(int, input().split()))

print(max_books(n, t, books))
