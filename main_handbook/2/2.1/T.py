n = int(input())
m = int(input())
k1 = int(input())
k2 = int(input())
for x in range(1000):
    if k2 * x + k1 * (n - x) == m * n:
        break
print(n - x, x)