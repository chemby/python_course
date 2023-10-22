class Car:
    def __init__(self, manufacturer: str, brand: str, fuel_usage: float, year: int = 2020):
        self.year = year
        self.manufacturer = manufacturer
        self.brand = brand
        self.distance = 0
        self.fuel_usage = fuel_usage

        with open("cars_list.csv", mode='a', encoding="utf-8") as file:
            file.write(f'{self.brand};{self.manufacturer}\n')

    def __str__(self):
        return f'brand is {self.brand}, manufacturer is {self.manufacturer}, year is {self.year}, fuel usage is {self.fuel_usage}'

    __repr__ = __str__


class Truck(Car):
    def __init__(self, manufacturer: str, brand: str, fuel_usage: float, capacity: int, year: int = 2020):
        super().__init__(manufacturer=manufacturer, brand=brand, fuel_usage=fuel_usage, year=year)
        self.capacity = capacity


class SportCar(Car):
    def __init__(self, manufacturer: str, brand: str, fuel_usage: float, max_speed: int, price: float, year: int = 2020):
        super().__init__(manufacturer=manufacturer, brand=brand, fuel_usage=fuel_usage, year=year)
        self.max_speed = max_speed
        self.price = price


car1 = Car("toyota", "numero uno", 10.5, 2023)
car2 = Car("ferrari", "some brand", 5.234)
truck1 = Truck("Volkswagen", "platinum", 20.1, 100, 2018)
sport_car1 = SportCar("Ferrari", "Formula 1", 15.77, 250, 123456.789)
