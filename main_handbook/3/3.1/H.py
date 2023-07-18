n = int(input())
res = []
while n > 0:
    line = input()
    res.append(line.find("зайка") + 1 if "зайка" in line else "Заек нет =(")
    n -= 1
[print(i) for i in res]