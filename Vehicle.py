class Vehicle:
    def __init__(self, name):
        self.name = name

    def move(self):
        return f"{self.name} is moving!"

class Car(Vehicle):
    def move(self):
        return f"{self.name} is driving! 🚗"

class Plane(Vehicle):
    def move(self):
        return f"{self.name} is flying! ✈️"

# Example usage
car = Car("Toyota")
plane = Plane("Boeing")

print(car.move())   # Toyota is driving! 🚗
print(plane.move()) # Boeing is flying! ✈️