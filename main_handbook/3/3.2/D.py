n = int(input())
m = int(input())
good = set()
bad = set()
while n > 0:
    good.add(input())
    n -= 1
while m > 0:
    bad.add(input())
    m -= 1
print(len(good.intersection(bad)) if good & bad else "Таких нет")