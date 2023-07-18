class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, *other):
        self.x += other[0]
        self.y += other[1]

    def length(self, other):
        h = self.y - other.y
        c = self.x - other.x
        res = (c ** 2 + h ** 2) ** (1/2)
        return round(res, 2)
