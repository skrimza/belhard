# 1.Writing a Class 'Car'. Constructor of Class 
# accepting attrybutes: color: str, 
# count_passenger_seats: int, is_baby_seat: bool
# is_busy: bool
# 1.1 Writing a magic method __str__ outputing
# a format string with information about auto

class Car:

    def __init__(self, color: str, count_passenger_seats: int, is_baby: bool, is_busy: bool) -> None:
        self.color = color
        self.seats = count_passenger_seats
        self.baby = is_baby
        self.busy = is_busy
    def __str__(self) -> str:
        return f'{self.color}, {self.seats}, {self.baby}, {self.busy}'
    
Car.name = 'Bmw'
information = Car('Blue', 5, True, False)

print(f'{Car.name} = {information}')