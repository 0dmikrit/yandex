status = ["пик", "треф", "бубен", "червей"]
rang = ("валет", "дама", "король", "туз")
status.remove(input())
for i in range(2, 11):
    for j in status:
        print(i, j)
for i in rang:
    for j in status:
        print(i, j)