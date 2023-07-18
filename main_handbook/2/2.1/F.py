name = input()
price = int(input())
weight = int(input())
sell = int(input())
print(f'''Чек
{name} - {weight}кг - {price}руб/кг
Итого: {weight * price}руб
Внесено: {sell}руб
Сдача: {sell - weight * price}руб''')