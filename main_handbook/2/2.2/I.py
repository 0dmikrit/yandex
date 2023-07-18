x = input()
y = input()
z = input()
mas = [x, y, z]
min = x
for i in mas:
    if i <= min:
        min = i
print(min)