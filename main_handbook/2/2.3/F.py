num = [int(input()), int(input())]
count = 0
for i in range(1, max(num) + 1):
    if (min(num) % i == 0) and (max(num) % i == 0):
        count = i
print(count)