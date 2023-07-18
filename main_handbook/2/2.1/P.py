x = int(input())
y = int(input())
z = int(input())
a = (y - x) / z
h = len(str(a)[str(a).index('.') + 1:])
if h >= 2:
    print(round(a, 2))
else:
    print(str(a) + '0')