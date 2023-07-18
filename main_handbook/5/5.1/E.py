class Rectangle:
    def __init__(self, a_point, b_point):
        self.a_point = a_point
        self.b_point = b_point
        self.length = abs(a_point[0] - b_point[0])
        self.width = abs(a_point[1] - b_point[1])

    def perimeter(self):
        res = 2 * (self.length + self.width)
        return round(res, 2)

    def area(self):
        res = self.length * self.width
        return round(res, 2)
