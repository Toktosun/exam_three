class Rectangle:
    a = 3
    b = 7

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return self.a*self.b

    def perimeter(self):
        return self.a + self.b * 2

    @property
    def _width(self):
        return self.b

    @property
    def _height(self):
        return self.a

    @_width.setter
    def width(self, width):
        self.b = width

    @_height.setter
    def height(self, height):
        self.a = height

    def getStatus(self):
        return " Width: %s \n Height: %s \n Area: %s \n Perimeter: %s" % (self.b, self.a, self.area(), self.perimeter())


R = Rectangle(3, 7)
# print(R.area())
# print(R.perimeter())
print(R.getStatus())
