arr = input().split()
[print(*arr[:i]) for i in range(1, len(arr) + 1)]