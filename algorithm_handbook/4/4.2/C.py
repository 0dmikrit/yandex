def add(line1, line2, n):
    count = 0
    res = ''
    while count < n:
        res += line1[count] + line2[count]
        count += 1
    return res


n = int(input())
line1 = input()
line2 = input()
print(add(line1, line2, n))