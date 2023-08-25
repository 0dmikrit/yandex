n = int(input())
print("А Б В")
for a in range(1, n - 1):
    for b in range(1, n - 1):
        for c in range(1, n - 1):
            if a + b + c == n:
                print(a, b, c)