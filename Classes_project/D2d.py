class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)

    def perimeter(self):
        return 2 * 3.14 * self.radius

    def display_info(self):
        print(f"Circle: Radius = {self.radius}, Area = {self.area()}, Perimeter = {self.perimeter()}")
        return self.area(), self.perimeter()

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def display_info(self):
        print(f"Rectangle: Length = {self.length}, Width = {self.width}, Area = {self.area()}, Perimeter = {self.perimeter()}")
        return self.area(), self.perimeter()

class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

    def perimeter(self):
        return self.base + 2 * ((self.base ** 2 + self.height ** 2) ** 0.5)

    def display_info(self):
        print(f"Triangle: Base = {self.base}, Height = {self.height}, Area = {self.area()}, Perimeter = {self.perimeter()}")
        return self.area(), self.perimeter()