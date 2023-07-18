start = int(input())
end = int(input())
for i in range(start, end, 1 if start < end else -1):
    print(i, end=' ')
print(end)