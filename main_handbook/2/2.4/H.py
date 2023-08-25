n = int(input())
val = {}
while n > 0:
    name = input()
    val[sum([int(i) for i in input()])] = name
    n -= 1
print(val.get(max(val.keys())))