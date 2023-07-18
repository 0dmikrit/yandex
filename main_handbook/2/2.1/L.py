x = input()
y = input()
x = '0' * (3 - len(x)) + x
y = '0' * (3 - len(y)) + y
a = str(int(x[0]) + int(y[0]))[-1]
b = str(int(x[1]) + int(y[1]))[-1]
c = str(int(x[2]) + int(y[2]))[-1]
print(int(a + b + c))