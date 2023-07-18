def num(s):
    res = []
    i = 0
    while i < len(s):
        if s[i].isdigit():
            res.append(int(s[i]))
        if s[i] == '-':
            res.append(-1 * int(s[i+1]))
            i += 1
        i += 1
    return tuple(res)


print(num('1 -2 3 -6 8 13 0 -2'))
