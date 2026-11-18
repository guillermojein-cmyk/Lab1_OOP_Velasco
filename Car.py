class Car:
    wheels = 4

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        

    def __str__(self):
        return f"{self.brand} {self.model} {self.year} - Wheels: {self.wheels}"

car1 = Car("Honda", "Civic", 1972)
car2 = Car("Honda", "City", 2026)
car3 = Car("Honda", "Hatchback", 2016)

print(car1)
print(car2)
print(car3)