def gcd(*numbers):
    for i in range(min(numbers), 0, -1):
        if len(numbers) == len([j for j in numbers if j % i == 0]):
            return i
