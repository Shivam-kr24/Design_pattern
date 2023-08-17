from abc import ABC, abstractmethod

# Abstract Product Interfaces
class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

class Color(ABC):
    @abstractmethod
    def fill(self):
        pass

# Concrete Product Classes
class Circle(Shape):
    def draw(self):
        return "Draw a Circle"

class Square(Shape):
    def draw(self):
        return "Draw a Square"

class Red(Color):
    def fill(self):
        return "Fill with Red color"

class Blue(Color):
    def fill(self):
        return "Fill with Blue color"

# Abstract Factory Interface
class AbstractFactory(ABC):
    @abstractmethod
    def create_shape(self):
        pass

    @abstractmethod
    def create_color(self):
        pass

# Concrete Factory Classes
class ShapeColorFactory(AbstractFactory):
    def create_shape(self):
        return Circle()

    def create_color(self):
        return Red()

# Client Code
def create_and_fill(factory):
    shape = factory.create_shape()
    color = factory.create_color()
    return f"{shape.draw()} and {color.fill()}"

# Usage
factory = ShapeColorFactory()
result = create_and_fill(factory)
print(result)  # Outputs: Draw a Circle and Fill with Red color
