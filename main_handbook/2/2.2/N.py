from itertools import combinations


x = input()
y = [*combinations(x, 2), *combinations(x[::-1], 2)]
z = list(filter(lambda x: True if x > 9 else False, [int(i[0] + i[1]) for i in y]))
print(min(z), max(z))