v_p = int(input())
v_v = int(input())
v_t = int(input())
members = {'Петя': v_p, 'Вася': v_v, 'Толя': v_t}
members = dict(sorted(members.items(), reverse=True, key=lambda item: item[1]))
for i, item in enumerate(members.keys()):
    print(f'{i+1}. {item}')