class Car:
    def __init__(self, manufacturer: str, brand: str, fuel_usage: float, year: int = 2020):
        self.year = year
        self.manufacturer = manufacturer
        self.brand = brand
        self.distance = 0
        self.fuel_usage = fuel_usage

    def __str__(self):
        return f'brand is {self.brand}, manufacturer is {self.manufacturer}, year is {self.year}, fuel usage is {self.fuel_usage}'

    __repr__ = __str__


car1 = Car("toyota", "numero uno", 10.5, 2023)
car2 = Car("ferrari", "some brand", 5.234)
print(car1)
print(car2)
