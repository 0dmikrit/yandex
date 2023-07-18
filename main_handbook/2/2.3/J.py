cord = [0, 0]
while (s := input()) != 'СТОП':
    match s:
        case 'СЕВЕР':
            cord[0] += int(input())
        case 'ЮГ':
            cord[0] -= int(input())
        case 'ЗАПАД':
            cord[1] -= int(input())
        case 'ВОСТОК':
            cord[1] += int(input())
print(*cord, sep='\n')