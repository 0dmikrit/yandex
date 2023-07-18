x = int(input())
y = int(input())
for i in range(max(x, y), x * y + 1):
    if i % x == 0 and i % y == 0:
        break
print(i)