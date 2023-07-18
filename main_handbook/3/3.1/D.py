res = []
while line := input():
    if line[:2] == "##":
        if not line[-3:] == "@@@":
            res.append(line[2:])
    elif line[-3:] == "@@@":
        pass
    else:
        res.append(line)
[print(i) for i in res]