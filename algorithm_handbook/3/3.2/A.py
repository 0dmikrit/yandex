table = []
n = int(input())
while n:
    i, j = map(int, input().split())
    table += {k for k in range(i, j + 1)}
    n -= 1
print(len([table[f] & table[f + 1] for f in range(len(table) - 1)]))