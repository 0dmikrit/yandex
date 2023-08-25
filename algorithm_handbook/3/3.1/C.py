from math import comb


n, m = map(int, input().split(" "))
if (0 < n < 5) and (0 < m < 5):
    count = comb(n + m - 1, m)
    print(count)
