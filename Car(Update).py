class Car:
    wheels = 4

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = 0

    def drive(self, km):
        if km > 0:
            self.mileage += km
            print(f"Drove {km} km. Total: {self.mileage} km")
        else:
            print("Distance must be positive!")

    def age(self, current_year):
        return current_year - self.year
    
    def __str__(self):
        return f"{self.brand} {self.model} {self.year} - Wheels: {self.mileage} km"
    
if __name__ == "__main__":
    car1 = Car("Honda", "Civic", 1972)
    car2 = Car("Honda", "City", 2026)
    car3 = Car("Honda", "Hatchback", 2016)

    print(car1)
    car1.drive(50)
    car1.drive(-10)
    print(f"Age: {car1.age(1972)} years")

    print(car2)
    print(car3)