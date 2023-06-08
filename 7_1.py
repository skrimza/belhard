# 1.Writing a Class 'Car'. Constructor of Class 
# accepting attrybutes: color: str, 
# count_passenger_seats: int, is_baby_seat: bool
# is_busy: bool
# 1.1 Writing a magic method __str__ outputing
# a format string with information about auto

class Car:

    def __init__(self, 
                 color: str, 
                 count_passenger_seats: int, 
                 is_baby: bool, is_busy: bool) -> None:
        self.color = color
        self.seats = count_passenger_seats
        self.baby = is_baby
        self.busy = is_busy
    def __str__(self) -> str:
        return f'{self.color}, {self.seats}, {self.baby}, {self.busy}'


class Taxi:

    def __init__(self, cars: list[Car]):
        self.cars = cars
        
    def find_car(self, count_passenger: int, is_baby: bool):
        for car in self.cars:
            if count_passenger <= car.seats and not car.busy:
                if is_baby and car.baby:
                    car.busy = True
                    return car

            
car = [Car('blue', 5, False, False), 
       Car('blue', 4, True, False), 
       Car('blue', 5, False, False), 
       Car('blue', 3, False, False),]

free_car = Taxi(car)
print(free_car.find_car(4, True))


