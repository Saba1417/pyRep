from datetime import date

class Car :
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def car_info(self):
        return f"{self.year} {self.make} {self.model}{self.age_of_car( date.today().year)}"
    
    def age_of_car(self, current_year):
        return current_year - self.year
    
    
class ElectricCar(Car):
    def __init__(self, make, model, year, battery_life):
        super().__init__(make, model, year)
        self.battery_life = battery_life
    
    def battery_info(self):
        return f"ამ მანქანის ბატარეის ხანგრძლივობა არის {self.battery_life} საათი"

Car.number_of_cars = 0

original_init = Car.__init__
def new_init(self, make, model, year):
    original_init(self, make, model, year)
    Car.number_of_cars += 1

Car.__init__ = new_init

def total_cars(self):
    return f"მანქანების მთლიანი რაოდენობა: {Car.number_of_cars}"

Car.total_cars = total_cars

if __name__ == "__main__":
    car1 = Car("Toyota", "Corolla", 2015)
    car2 = ElectricCar("Tesla", "Model S", 2020, 24)
    car3 = Car("Honda", "Civic", 2018)

    print(car1.car_info())
    print(car2.car_info())
    print(car2.battery_info())
    print(car3.car_info())
    print(Car.total_cars(car1))