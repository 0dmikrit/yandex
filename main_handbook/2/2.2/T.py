n = 0
res = []
while n < 3:
    s = input()
    if 'зайка' in s:
        res.append(s)
    n += 1
print(min(res), len(min(res).strip()))
