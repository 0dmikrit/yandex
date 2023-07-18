res = []
while line := input():
    res.append(line[:line.find("#")]) if "#" in line else res.append(line)
[print(i) for i in res if i]