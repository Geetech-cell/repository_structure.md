class Superhero:
    def __init__(self, name, power_level, city):
        self._name = name  # Encapsulation with protected attribute
        self._power_level = power_level
        self.city = city

    def use_power(self):
        return f"{self._name} uses their power at level {self._power_level}!"

    def get_name(self):  # Getter for encapsulation
        return self._name


class FlyingHero(Superhero):  # Inheritance
    def __init__(self, name, power_level, city, flight_speed):
        super().__init__(name, power_level, city)
        self.flight_speed = flight_speed

    def use_power(self):  # Polymorphism
        return f"{self._name} soars through {self.city} at {self.flight_speed} mph!"


# Example usage
hero = Superhero("Thunderbolt", 80, "Metropolis")
flyer = FlyingHero("Skyblazer", 95, "Star City", 300)

print(hero.use_power())  # Thunderbolt uses their power at level 80!
print(flyer.use_power())  # Skyblazer soars through Star City at 300 mph!
print(flyer.get_name())  # Skyblazer