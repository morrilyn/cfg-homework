import abc

class Shape(object):
    __metaclass__ = abc.ABCMeta
    
    @abc.abstractmethod
    def calc_perimeter(self, input):
        """Method documentation"""
        return

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def calc_perimeter(self):
        perim = self.a + self.b + self.c
        # print("Consider me implemented", perim)
        return perim

class Rectangle(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calc_perimeter(self):
        perim = self.a * 2 + self.b * 2
        # print("Consider me implemented", perim)
        return perim
    
class Square(Rectangle):
    def __init__(self, a):
        self.a = a
    
    def calc_perimeter(self):
        perim = self.a * 4
        return perim
        
        
        
# Create an instance of Triangle with sides of length 3, 4, and 5
triangle = Triangle(3, 4, 5)
# Print the perimeter of the triangle
print(f"The perimeter of the triangle is: {triangle.calc_perimeter()}")

# Create an instance of Rectangle with sides of length 4 and 6
rectangle = Rectangle(4, 7)
# Print the perimeter of the rectangle
print(f"The perimeter of the rectangle is: {rectangle.calc_perimeter()}")

# Create an instance of Square with all sides of length 5
square = Square(5)
# Print the perimeter of the square
print(f"The perimeter of the square is: {square.calc_perimeter()}")
