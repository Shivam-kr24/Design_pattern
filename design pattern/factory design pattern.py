from abc import ABC, abstractmethod

# Product Interface
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

# Concrete Products
class Dog(Animal):
    def speak(self):
        return "wolf!"

class Cat(Animal):
    def speak(self):
        return "cow!"

# Creator Interface
class AnimalFactory(ABC):
    @abstractmethod
    def create_animal(self):
        pass

# Concrete Creators
class DogFactory(AnimalFactory):
    def create_animal(self):
        return Dog()

class CatFactory(AnimalFactory):
    def create_animal(self):
        return Cat()

# Client Code
def make_animal_sound(factory):
    animal = factory.create_animal()
    return animal.speak()

# Usage
dog_factory = DogFactory()
cat_factory = CatFactory()

print(make_animal_sound(dog_factory))  # Outputs: Woof!
print(make_animal_sound(cat_factory))  # Outputs: Meow!
