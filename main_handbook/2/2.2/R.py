s = sorted([int(input()), int(input()), int(input())])
if s[-1] ** 2 > s[0] ** 2 + s[1] ** 2:
    print('велика')
elif s[-1] ** 2 < s[0] ** 2 + s[1] ** 2:
    print('крайне мала')
else:
    print('100%')