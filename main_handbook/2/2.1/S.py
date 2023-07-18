name = input()
price = int(input())
weight = int(input())
money = int(input())
h = f'{weight}кг * {price}'
line = f'''================Чек================
Товар:{name.rjust(29)}
Цена:{h.rjust(24)}руб/кг
Итого:{str(price * weight).rjust(26)}руб
Внесено:{str(money).rjust(24)}руб
Сдача:{str(money - price * weight).rjust(26)}руб
==================================='''
print(line)