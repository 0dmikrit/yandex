count = 0
while (x := float(input())) != 0:
    if x >= 500:
        count += (x / 100 * 90)
    else:
        count += x
print(round(count, 1))