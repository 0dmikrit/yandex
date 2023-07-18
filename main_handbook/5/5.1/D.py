class Programmer:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        self.salary = {"Junior": 10,
                       "Middle": 15,
                       "Senior": 20}
        self.money = 0
        self.time = 0

    def work(self, time):
        self.money += self.salary[self.grade] * time
        self.time += time

    def rise(self):
        match self.grade:
            case "Junior":
                self.grade = "Middle"
            case "Middle":
                self.grade = "Senior"
            case "Senior":
                self.salary["Senior"] += 1

    def info(self):
        return f"{self.name} {self.time}ч. {self.money}тгр."
