s = sorted([*[int(i) for i in input()], *[int(i) for i in input()]])
print(s[-1], str(sum(s[1:-1]))[-1], s[0], sep='')