arr = [int(input()) for k in range(int(input()))]
flags = []
for i in range(min(arr), 0, -1):
    for j in range(len(arr)):
        if arr[j] % i == 0:
            flags.append(1)
    if len(flags) == len(arr):
        print(i)
        break
    else:
        flags.clear()
