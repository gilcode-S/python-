
class Shape:
    def __init__(self, color, filled):
        self.color = color
        self.filled = filled


class Circle(Shape):
    def __init__(self, radius, color, filled):
        super().__init__(color, filled)
        self.radius = radius

    def describe(self):
        print(f"It is {self.color} and its filled")


class Square(Shape):
    def __init__(self,  height, color, filled):
        super().__init__(color, filled)
        self.height = height


class Triangle(Shape):
    def __init__(self, width, height, color, filled):
        super().__init__(color, filled)
        self.width = width
        self.height = height


# construct object
circle = Circle(color="yellow", filled=True, radius=5)

print(circle.radius)

