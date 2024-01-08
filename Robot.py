class Robot:
    def __init__(self, name, color, weight):
        self.name = name
        self.weight = weight
        self.color = color

    def introduce_self(self):
        print("My name is " + self.name)

r1 = Robot("Teddy", "blue", 50)
r1.introduce_self()

r2 = Robot("Suzy", "red", 30)
r2.introduce_self()