n = int(input())
count = 0
flag = False
while n > 0:
    x = input()
    if x == "зайка" and not flag:
        count += 1
        flag = True
    if x == "ВСЁ":
        n -= 1
        flag = False
print(count)