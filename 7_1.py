# 1.Writing a Class 'Car'. Constructor of Class 
# accepting attrybutes: color: str, 
# count_passenger_seats: int, is_baby_seat: bool
# is_busy: bool
# 1.1 Writing a magic method __str__ outputing
# a format string with information about auto

# 2. writing a class Taxi 
# Constructor of class accepting attrybutes:
# cars: list[Car] (list of examples )
# 2.1 Реализовать метод find_car
# На вход метода поступают атрибуты: count_passengers, is_baby (количество пассажиров,
# наличие ребенка, примечание: количество пассажиров с учетом ребенка если он есть)
# На основании данных, вернуть объект Car из атрибута cars подходящий по параметрам и
# свободный (is_busy = False), у автомобиля сменить атрибут is_busy на значение True, если
# подходящего автомобиля нет, метод должен возвращать None

class Car:
    # создание класса Car и его инициализация
    def __init__(self, 
                 color: str, 
                 count_passenger_seats: int, 
                 is_baby: bool, is_busy: bool) -> None:
        self.color = color
        self.seats = count_passenger_seats
        self.baby = is_baby
        self.busy = is_busy
        # передача магического метода str для вывода форматированной строки
    def __str__(self) -> str:
        # возврат форматированноый строки
        return f'{self.color}, {self.seats}, {self.baby}, {self.busy}'


class Taxi:
    # создание класса Taxi и инициализация его
    def __init__(self, cars: list[Car]):# передаем параметр cars 
        self.cars = cars
        
    def find_car(self, count_passenger: int, is_baby: bool): #реализуем метод Find_car передаем необходимые атрибуты
        for car in self.cars: # разделяем параметр cars на несколько car
            if count_passenger <= car.seats and not car.busy: # условие: если требуемое число мест меньше или равно свободным местам в машине и машина не занята
                if is_baby and car.baby: # 2-е условие: если нужно детское сидение и в машине оно есть
                    car.busy = True # занятость машина меняем False на True
                    return car # возвращаем обьект car подходящий условиям
           
car = [Car('blue', 4, False, False), 
       Car('red', 5, False, False), 
       Car('blue', 3, False, False),
       Car('yellow', 4, True, False)] # сам список обьектов класса Car

free_car = Taxi(car) # присваиваем переменной free_car класс Taxi с параметром car
print(free_car.find_car(4, True))

class Category:
    categories = []

    def __init__(self) -> None:
        pass

    @classmethod
    def add(cls, name):
        if name.lower() not in cls.categories:
            cls.categories.append(name.lower())
            return cls.categories.index(name)
        else:
            raise ValueError('Valueerror Ильюха')
    
    @classmethod
    def get(cls, index):
        if 0 <= index < (len(cls.categories)):
            return cls.categories[index]
        else:
            raise IndexError('indexerror Ильюха')
        
    @classmethod
    def delete(cls, index):
        if 0 <= index < (len(cls.categories)):
            del cls.categories[index]

    @classmethod
    def update(cls, index, new_name):
        if index < len(cls.categories):
            if new_name.lower() not in cls.categories:
                cls.categories[index] = new_name.lower()
            else:
                raise ValueError('ValueError Ильюха')
        else:
            cls.categories.append(new_name.lower())

add = Category.add('china')
add = Category.add('russia')
print('Список: ', Category.categories)
print('элемент под индексом :', Category.get(0))

Category.delete(1)
print('Категория удалена: ', Category.categories)

Category.update(0, 'belarus')
print('категории обновлены: ', Category.categories)

class NewCategory:
    categories = []

    def __init__(self) -> None:
        pass
    
    @classmethod
    def add(cls, name: str, is_published: bool):
        if name.lower() not in [category['name'] for category in cls.categories]:
            cls.categories.append({'name': name.lower(), 'is_published': is_published})
        else:
            raise ValueError('ValueError Ильюха')

    @classmethod
    def get(cls, index):
        if 0 <= index < (len(cls.categories)):
            return cls.categories[index]
        else:
            raise IndexError('indexerror Ильюха')

    @classmethod
    def delete(cls, index):
        if 0 <= index < (len(cls.categories)):
            del cls.categories[index]

    @classmethod
    def update(cls, index, new_name, new_is_published):
        if index < len(cls.categories):
            if new_name.lower() not in [category['name'] for category in cls.categories]:
                cls.categories[index] = dict(name=new_name.lower(), is_published=new_is_published)
            else:
                raise ValueError('ValueError Ильюха')
        else:
            cls.categories.append(dict(name=new_name.lower(), is_published=new_is_published))

    @classmethod
    def make_published(cls, index):
        if 0 <= index < len(cls.categories):
            if not cls.categories[index]['is_published']:
                cls.categories[index]['is_published'] = True
        else:
            raise IndexError('IndexError Ильюха')

    @classmethod
    def make_unpublished(cls, index):
        if 0 <= index < len(cls.categories):
            if cls.categories[index]['is_published']:
                cls.categories[index]['is_published'] = False
        else:
            raise IndexError('IndexError Ильюха')
        
new_category = NewCategory()    
new_add1 = NewCategory.add('russia', True)
new_add2 = NewCategory.add('china', False)

print('новые категории: ', new_category.categories)
print('элемент под индексом 0', new_category.categories)

NewCategory.delete(1)
print('список элементов после удаления', new_category.categories)

NewCategory.update(1, 'poland', False)
print('список после обновления', new_category.categories)
NewCategory.make_published(0)
NewCategory.make_unpublished(1)
print('Список обновлен', new_category.categories)
# class Book:

#     def __init__(self, title, author, year) -> None:
#         self.title = title
#         self.author = author
#         self.year = year
    
#     def get_info(self):
#         return f'Title: {self.title}, Author: {self.author}, Year: {self.year}'
    
# book1 = Book("The Catcher in the Rye", "J.D. Salinger", 1951)
# print(book1.get_info())

# class Library:

#     def __init__(self, books: list) -> None:
#         self.books = books

#     def add_book(self, book):
#         self.books.append(book)
    
#     def get_books_by_author(self, name):
#         author_books = []
#         for book in self.books:
#             if book.author == name:
#                 author_books.append(book)
#         return author_books
    
#     def get_book_titles(self):
#         return (book.title for book in self.books)
    
# library = Library()
# # Создание объектов класса Book и добавление их в библиотеку
# book1 = Book("The Catcher in the Rye", "J.D. Salinger", 1951)
# book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960)
# library.add_book(book1)
# library.add_book(book2)

# # Вывод названий всех книг в библиотеке
# print("Book Titles:", list(library.get_book_titles()))

# # Вывод книг автора "J.D. Salinger"
# salinger_books = library.get_books_by_author("J.D. Salinger")
# for book in salinger_books:
#     print(book.get_info())

# class BankAccount:

#     def __init__(self, account_number, balance) -> None:
#         self.number = account_number
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount
    
#     def withdraw(self, amount):
#         if amount > self.balance:
#             return 'недостаточно средств, сумма снятия привышает сумму вашего баланса'
#         else:
#             self.balance -= amount
#             return self.balance            
    
# account = BankAccount('5578397655413219', 1000)
# account.deposit(500)

# result1 = account.withdraw(700)
# result2 = account.withdraw(1250)
# print(result1)
# print(result2)
# print("current balance:", account.balance)

# class Rectangle:

#     def __init__(self, width, height) -> None:
#         self.width = width
#         self.height = height

#     def calculate_area(self):
#         return self.width * self.height
    
#     def calculate_perimeter(self):
#         return self.width*2 + self.height*2
    
# rectangle = Rectangle(5, 10)

# # Вычисление и вывод площади и периметра
# print("Area:", rectangle.calculate_area())
# print("Perimeter:", rectangle.calculate_perimeter())

