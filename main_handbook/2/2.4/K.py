n = int(input())
arr = []
while n > 0:
    num = int(input())
    if num == 2:
        arr.append(1)
    if num != 1:
        flag = False
        for i in range(2, num):
            if num % i == 0:
                flag = False
                break
            else:
                flag = True
        if flag:
            arr.append(1)
    n -= 1
print(len(arr))
