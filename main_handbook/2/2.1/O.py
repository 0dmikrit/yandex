x = int(input())
y = int(input())
z = int(input())
c = x * 60 + y + z
a, b = divmod(c, 60)
while a >= 24:
    a -= 24
print(f'{"0" + str(a) if a < 10 else a}:{"0" + str(b) if b < 10 else b}')