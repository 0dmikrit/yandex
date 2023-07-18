n = int(input())
flags = []
alph = ['А', 'а', 'Б', 'б', 'В', 'в']
while n > 0:
    word = input()
    flags.append(1) if word[0] in alph else flags.append(0)
    n -= 1
print('NO' if 0 in flags else 'YES')