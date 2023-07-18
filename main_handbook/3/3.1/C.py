size = int(input())
lst = []
n = int(input())
while n > 0:
    line = input()
    if len(line) > size:
        lst.append(f"{line[:size - 3]}...")
    else:
        lst.append(line)
    n -= 1
[print(i) for i in lst]
