n = int(input())
res = []
while n > 0:
    res.extend(input().split())
    n -= 1
[print(f"{i}") for i in set(res)]
