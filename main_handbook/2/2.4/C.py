arr = [k for k in range(1, (int(input()) + 1))]
for i in range(len(arr)):
    c = 1
    while arr:
        print(*arr[:c])
        arr = arr[c:]
        c += 1