# /*single and multi and heirachical*/
import math


class shapes:
    def __init__(self, sides):
        self.sides = sides

    def setSides(self):
        self.sides = int(input("Enter no. of sides:\n"))

    def printSides(self):
        print("No. of sides = ", self.sides)


class circle(shapes):
    def __init__(self, radius):
        self.r = radius

    def printPerimeter(self):
        print("Perimeter = ", round(2 * math.pi * self.r))

    def printArea(self):
        print("Area = ", round(math.pi * self.r * self.r))


class square(shapes):
    def __init__(self, length):
        self.length = length

    def setSides(self):
        self.sides = 4

    def printPerimeter(self):
        print("Perimeter = ", 4 * self.length)

    def printArea(self):
        print("Area = ", round(self.length * self.length))


class triangle(shapes):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def setSides(self):
        self.sides = 3

    def setLength(self):
        self.a = int(input())
        self.b = int(input())
        self.c = int(input())

    def getLength(self):
        return self.a, self.b, self.c

    def printPerimeter(self):
        print("Perimeter = ", self.a + self.b + self.c)


class equilateralTriangle(triangle):
    def __init__(self, a):
        self.a = a

    def setLength(self):
        self.a = int(input())

    def printPerimeter(self):
        print("Perimeter = ", self.a * 3)

    def getLength(self):
        return self.a, self.a, self.a


obj1 = equilateralTriangle(5)
obj1.setSides()
obj1.printSides()
obj1.printPerimeter()
print(obj1.getLength())
#     def sides(self):
#         self.sides=0
# c1=circle(2)
# c1.sides()
# c1.printSides()
# c1.printPerimeter()
# c1.printArea()