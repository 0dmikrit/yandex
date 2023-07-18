x = input()
a = int(x[0]) + int(x[1])
b = int(x[1]) + int(x[2])
if a > b:
    print(f'{a}{b}')
else:
    print(f'{b}{a}')