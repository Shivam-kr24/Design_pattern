from abc import ABC, abstractmethod

# Product
class Meal:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def show_items(self):
        for item in self.items:
            print(item)

# Builder Interface
class MealBuilder(ABC):
    @abstractmethod
    def build_burger(self):
        pass

    @abstractmethod
    def build_drink(self):
        pass

# Concrete Builders
class VegMealBuilder(MealBuilder):
    def __init__(self):
        self.meal = Meal()

    def build_burger(self):
        self.meal.add_item("Veg Burger")

    def build_drink(self):
        self.meal.add_item("Coke")

    def get_meal(self):
        return self.meal

# Director
class Waiter:
    def construct(self, builder):
        builder.build_burger()
        builder.build_drink()

# Usage
veg_builder = VegMealBuilder()
waiter = Waiter()
waiter.construct(veg_builder)
meal = veg_builder.get_meal()
meal.show_items()
