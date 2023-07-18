x = int(input())
y = int(input())
z = int(input())
if x == max(x, y, z):
    print('Петя')
elif y == max(x, y, z):
    print('Вася')
else:
    print('Толя')