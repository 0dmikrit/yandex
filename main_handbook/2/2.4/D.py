from functools import reduce


n = int(input())
val = ''
while n > 0:
    val += input()
    n -= 1
k = reduce(lambda x, y: x + y, map(int, val))
print(k)