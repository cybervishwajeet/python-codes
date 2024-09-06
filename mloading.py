class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def area(self, length, width):
        return length * width

class Circle(Shape):
    def area(self, radius):
        return 3.14 * radius * radius

# Method Overloading
rectangle = Rectangle()
circle = Circle()

print(rectangle.area(5, 4))  # Output: 20
print(circle.area(3))  # Output: 28.26

# Method Overriding
class Square(Rectangle):
    def area(self, side):
        return side * side

class mysquare(Square):
    def area(self, side):
        return side * side

square = Square()
print(square.area(5))  # Output: 25
mysquare_obj = mysquare()
print(mysquare_obj.area(4))  # Output: 16