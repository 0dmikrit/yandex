a = int(input())
b = int(input())
c = int(input())
b = [a + b > c, a + c > b, b + c > a]
if False in b:
    print('NO')
else:
    print('YES')