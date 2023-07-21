def can_eat(horse, other):
    x = abs(horse[0] - other[0])
    y = abs(horse[1] - other[1])
    if (x, y) in [(2, 1), (1, 2)]:
        return True
    return False
