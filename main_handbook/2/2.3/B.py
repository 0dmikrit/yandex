count = 0
x = input()
count += x.count('зайка')
while x != 'Приехали!':
    x = input()
    count += x.count('зайка')
print(count)