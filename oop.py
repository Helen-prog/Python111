# class Point3D:
#     pass


# class Point:
#     # x = 1
#     # y = 1
#
#     def set_coords(self, x, y):
#         self.x = x
#         self.y = y
#         self.z = self.x + self.y
#         print(self.z)
#
#     def print_info(self):
#         print(f"Координата x: {self.x}, координата y: {self.y}, cумма: {self.z}")
#
#
# p1 = Point()

# p1.x = 5
# p1.y = 10
# p1.set_coords(5, 10)
# p1.print_info()
# Point.set_coords(p1)
# print(type(p1))
# print(type(p1) == Point)
# print(isinstance(p1, Point))
# print(isinstance(p1, Point3D))
# p1.z = 7
# print(p1.z)
# print(getattr(p1, "x"))
# print(getattr(p1, "z", "False"))
# print(hasattr(p1, "z"))
# print(hasattr(p1, "y"))
# setattr(p1, "z", 17)
# delattr(p1, "z")
# print(p1.x, p1.y)
# Point.x = 100
# p1.x = 5
# p1.y = 10
# print(p1.x, p1.y)
# print(id(p1))
# print(id(Point))
# print(p1.x, Point.x)
# print("p1:", p1.__dict__)
#
# p2 = Point()
# p2.x = 20
# p2.y = 30
# p2.set_coords()
# print(p2.x, p2.y)
# print("p2:", p2.__dict__)

# print(Point.__doc__)
# print(Point.__name__)
# print(dir(Point))


# class Human:
#     name = "name"
#     birthday = "00.00.0000"
#     phone = "00-00-00"
#     country = "country"
#     city = "city"
#     address = "street, house"
#
#     def print_info(self):
#         print(" Персональные данные ".center(40, "*"))
#         print(f"Имя: {self.name}\nДата рождения: {self.birthday}\n"
#               f"Номер телефона: {self.phone}\nСтрана: {self.country}\n"
#               f"Город: {self.city}\nДомашний адрес: {self.address}")
#         print("=" * 40)
#
#     def input_info(self, name, date, phone, country, city, address):
#         self.name = name
#         self.birthday = date
#         self.phone = phone
#         self.country = country
#         self.city = city
#         self.address = address
#
#     def set_name(self, name):  # установить имя
#         self.name = name
#
#     def get_name(self):  # получить имя
#         return self.name
#
#     def set_birthday(self, birthday):
#         self.birthday = birthday
#
#     def get_birthday(self):
#         return self.birthday
#
#     def set_phone(self, phone):
#         self.phone = phone
#
#     def get_phone(self):
#         return self.phone
#
#     def set_country(self, c):
#         self.country = c
#
#     def get_country(self):
#         return self.country
#
#     def set_city(self, city):
#         self.city = city
#
#     def get_city(self):
#         return self.city
#
#     def set_address(self, a):
#         self.address = a
#
#     def get_address(self):
#         return self.address
#
#
# h1 = Human()
# h1.print_info()
# # h1.input_info("Юля", "23.05.1986", "45-46-98", "Россия", "Москва", "Чистопрудный будьвар, 1А")
# # h1.print_info()
# h1.set_name("Марина")
# #
# # print(f"Имя: {h1.get_name()}")
# h1.set_birthday("25.05.2007")
# # print(h1.get_birthday())
# h1.set_phone("89-78-45")
# print(h1.get_phone())
# h1.set_country("Белорусь")
# print(h1.get_country())
# h1.print_info()


# class Person:
#     skill = 10
#
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     def print_info(self):
#         print("Данные сотрудника:", self.name, self.surname)
#
#     def add_skill(self, k):
#         self.skill += k
#         print("Квалификация сотрудника:", self.skill)
#
#
# p1 = Person("Viktor", "Reznik")
# p1.print_info()
# p1.add_skill(3)
# p2 = Person("Anna", "Dolgih")
# p2.print_info()
# p2.add_skill(2)

# class Point:
#     # def __new__(cls, *args, **kwargs):
#     #     print("Конструктор")
#     #     return super().__new__(cls)
#
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     def __del__(self):
#         print("Удаление экземпляра: " + self.__class__.__name__)
#
#
# p1 = Point(5, 10)
# print(p1.__dict__)
# del p1
# p2 = Point()
# print(p2.__dict__)
# p3 = Point(y=2)
# print(p3.__dict__)

# print(p1.x)

# class Point:
#     count = 0  # статическая переменная
#
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#         Point.count += 1
#
#     # def increment(self):
#     #     self.count += 1
#     #     return self.count
#
#
# p1 = Point(5, 10)
# p2 = Point(2, 3)
# print(p2.count)
# p3 = Point(1, 4)
# print(Point.count)

# class Robot:
#     k = 0
#
#     def __init__(self, name):
#         self.name = name
#         print("Инициализация робота:", self.name)
#         Robot.k += 1
#
#     def __del__(self):
#         print(self.name, "выключается!")
#         Robot.k -= 1
#
#         if Robot.k == 0:
#             print(self.name, "был последним")
#         else:
#             print("Работающих роботов осталось:", Robot.k)
#
#     def say_hi(self):
#         print("Приветствую! Меня зовут:", self.name)
#
#
# droid1 = Robot('R2-D2')
# droid1.say_hi()
# print("Численность роботов:", Robot.k)
# print()
# droid2 = Robot('C-3PO')
# droid2.say_hi()
# print("Численность роботов:", Robot.k)
# print()
# droid3 = Robot('DD-D4')
# droid3.say_hi()
# print("Численность роботов:", Robot.k)
#
# print("\nЗдесь роботы могут проделать каую-то работу\n")
#
# print("Роботы закончили свою работу. Давайте их выключим")
# del droid1
# del droid2
# del droid3
# print("Численность роботов:", Robot.k)


# class Point:
#
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#
#     def get_coords(self):
#         return self.__x, self.__y
#
#     def __check_value(z):
#         if isinstance(z, int) or isinstance(z, float):
#             return True
#         return False
#
#     def set_coords(self, x, y):
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#         else:
#             print("Координаты должны быть числами")
#
#     def set_coords_x(self, x):
#         if Point.__check_value(x):
#             self.__x = x
#         else:
#             print("Координаты должны быть числами")
#
#     def set_coords_y(self, y):
#         if Point.__check_value(y):
#             self.__y = y
#         else:
#             print("Координаты должны быть числами")
#
#     def get_coords_x(self):
#         return self.__x
#
#     def get_coords_y(self):
#         return self.__y
#
#
# p1 = Point(5, 10)
# print(p1.get_coords())
# p1.set_coords(2.3, 2)
# print(p1.get_coords())
# p1.set_coords_x(20)
# print(p1.get_coords())
# p1.set_coords_y(40)
# print(p1.get_coords())
# print(p1.get_coords_x())
# print(p1.get_coords_y())
#
# print(p1.__dict__)
# print(p1._Point__x)
# p1._Point__x = "111"
# print(p1.__dict__)
# import math
#
#
# class Rectangle:
#     def __init__(self, length=1, width=1):
#         self.__length = length
#         self.__width = width
#
#     def __check_value(z):
#         if isinstance(z, int) or isinstance(z, float):
#             return True
#         return False
#
#     # Setters
#     def set_width(self, width):
#         if Rectangle.__check_value(width):
#             self.__width = width
#         else:
#             print("Координата ширины должна быть числомом")
#
#     def set_length(self, length):
#         if Rectangle.__check_value(length):
#             self.__length = length
#         else:
#             raise ValueError("Длина должна быть числом")
#
#     # Getters
#     def get_width(self):
#         return self.__width
#
#     def get_length(self):
#         return self.__length
#
#     # площадь
#     def get_area(self):
#         return self.__length * self.__width
#
#     # периметр
#     def get_perimetr(self):
#         return 2 * (self.__length + self.__width)
#
#     # диагональ
#     def get_hypotenuse(self):
#         return round(math.sqrt(self.__length**2 + self.__width**2), 2)
#
#     def get_draw(self):
#         print(("*" * self.__width + "\n") * self.__length)
#
#
# a = Rectangle(4, 12)
# # a.set_length(10)
# # a.set_width(20)
# print(a.get_length())
# print(a.get_width())
# print("Площадь прямоугольника:", a.get_area())
# print("Периметр прямоугольника:", a.get_perimetr())
# print("Гипотенуза прямоугольника:", a.get_hypotenuse())
# a.get_draw()

# class Point:
#     WIDTH = 50
#     __slots__ = ["__x", "__y", "z"]
#
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y

# def __getattr__(self, item):
#     return f"В классе {__class__.__name__} отсутствует атрибут {item}"

# def __getattribute__(self, item):
#     if item == "_Point__x":
#         return "Закрытая переменная"
#     else:
#         return object.__getattribute__(self, item)

# def __setattr__(self, key, value):
#     if key == "WIDTH":
#         raise AttributeError("Значение константы WIDTH изменять нельзя")
#     else:
#         self.__dict__[key] = value

#     def get_coords(self):
#         return self.__x, self.__y
#
#     def __check_value(z):
#         if isinstance(z, int) or isinstance(z, float):
#             return True
#         return False
#
#     def set_coords(self, x, y):
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#         else:
#             print("Координаты должны быть числами")
#
#     def set_coords_x(self, x):
#         if Point.__check_value(x):
#             self.__x = x
#         else:
#             print("Координаты должны быть числами")
#
#     def set_coords_y(self, y):
#         if Point.__check_value(y):
#             self.__y = y
#         else:
#             print("Координаты должны быть числами")
#
#     def get_coords_x(self):
#         return self.__x
#
#     def get_coords_y(self):
#         return self.__y
#
#
# p1 = Point(5, 10)
# # print(p1.zzz)
# p1.z = 12
# # print(p1.__dict__)
# print(p1.z)


# class Point:
#
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#
#     @property   # геттер
#     def coords_x(self):
#         print("Вызов get_coords_x")
#         return self.__x
#
#     @coords_x.setter
#     def coords_x(self, x):
#         print("Вызов set_coords_x")
#         self.__x = x
#
#     @coords_x.deleter
#     def coords_x(self):
#         print("Удаление свойства")
#         del self.__x
#
#     # coordsX = property(__get_coords_x, __set_coords_x, __del_coords_x)
#
#
# p1 = Point(5, 10)
# print(p1.__dict__)
# p1.coords_x = 100
# print(p1.__dict__)
# print(p1.coords_x)
# del p1.coords_x
# p1.coords_x = 4
# print(p1.coords_x)

# class Kgfunt:
#
#     def __init__(self, kg):
#         self.__kg = kg
#
#     @property
#     def kg_funt(self):
#         return self.__kg
#
#     @kg_funt.setter
#     def kg_funt(self, kg):
#         if isinstance(kg, (int, float)):
#             self.__kg = kg
#         else:
#             print("Килограммы задаются только числами")
#
#     def to_pound(self):
#         return self.__kg * 2.205
#
#
# p1 = Kgfunt(12)
# print(p1.to_pound())
# p1.kg_funt = 41
# print(p1.to_pound())
# p1.kg_funt = 2
# print(p1.to_pound())

# class Point:
#     __count = 0
#
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#         Point.__count += 1
#
#     # @staticmethod
#     def get_count():
#         return Point.__count
#
#     get_count = staticmethod(get_count)
#
#
# p1 = Point()
# p2 = Point()
# p3 = Point()
#
# print(Point.get_count())
# print(p1.get_count())

# class Person:
#     def __init__(self, name, old):
#         self.__name = name
#         self.__old = old
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, n):
#         self.__name = n
#
#     @name.deleter
#     def name(self):
#         del self.__name
#
#     @property
#     def old(self):
#         return self.__old
#
#     @old.setter
#     def old(self, year):
#         self.__old = year
#
#     @old.deleter
#     def old(self):
#         del self.__old
#
#
# p1 = Person("Irina", 26)
# print(p1.name)
# del p1.name
# p1.name = "Igor"
# print(p1.old)
# p1.old = 31
# del p1.old
# # p1.old = 0
# print(p1.__dict__)

# class Change:
#     @staticmethod
#     def inc(x):
#         return x + 1
#
#     @staticmethod
#     def dec(x):
#         return x - 1
#
#
# a = 10
# print(Change.inc(a), Change.dec(a))
# ch = Change()
# print(ch.inc(a), ch.dec(a))
# import math
#
#
# class Area:
#     count = 0
#
#     # def __init__(self):
#     #     Area.count += 1
#
#     @staticmethod
#     def triangle_aria(a, b, c):
#         p = (a + b + c) / 2
#         Area.count += 1
#         return math.sqrt(p * (p - a) * (p - b) * (p - c))
#
#     @staticmethod
#     def triangle_aria_2(a, h):
#         Area.count += 1
#         return 0.5 * a * h
#
#     @staticmethod
#     def square_area(a):
#         Area.count += 1
#         return a ** 2
#
#     @staticmethod
#     def rect_area(a, b):
#         Area.count += 1
#         return a * b
#
#     @staticmethod
#     def get_count():
#         return Area.count
#
#
# print("Площадь треугольника по формуле Герона:", Area.triangle_aria(3, 4, 5))
# print("Площадь треугольника через основание и высоту:", Area.triangle_aria_2(6, 7))
# print("Площадь квадрата", Area.square_area(7))
# print("Площадь прямоугольника", Area.rect_area(2, 6))
# pl = Area()
# print("Площадь треугольника по формуле Герона:", pl.triangle_aria(3, 4, 5))
# print("Площадь треугольника через основание и высоту:", pl.triangle_aria_2(6, 7))
# print("Количество подсчетов площадей:", Area.get_count())

# class Date:
#     def __init__(self, day=0, month=0, year=0):
#         self.day = day
#         self.month = month
#         self.year = year
#
#     @classmethod
#     def from_string(cls, string_date):
#         day, month, year = map(int, string_date.split("."))
#         date1 = cls(day, month, year)
#         return date1
#
#     @staticmethod
#     def is_date_validate(date_as_string):
#         if date_as_string.count('.') == 2:
#             day, month, year = map(int, date_as_string.split("."))
#             return day <= 31 and month <= 12 and year <= 3999
#
#     def string_to_db(self):
#         return f'{self.year}-{self.month}-{self.day}'
#
#
# dates = [
#     '30.12.2000',
#     '30-12-2020',
#     '01.01.2021',
#     '12.31.2020'
# ]
#
# for d in dates:
#     if Date.is_date_validate(d):
#         date = Date.from_string(d)
#         st = date.string_to_db()
#         print(st)
#     else:
#         print("Неправильная дата или формат строки с датой")

# string_date = '23.10.2021'
# day, month, year = map(int, string_date.split("."))
# print(day, month, year)
# d1 = Date.from_string('333.10.1')
# print(d1)
# print(d1.string_to_db())
# d2 = Date.from_string('21.11.2020')
# print(d2.string_to_db())
# date = Date(day, month, year)
# print(date.string_to_db())


class Account:
    rate_usd = 0.013
    rate_eur = 0.011
    suffix = 'RUB'
    suffix_usd = 'USD'
    suffix_eur = 'EUR'

    def __init__(self, surname, num, percent, value=0):
        self.surname = surname
        self.num = num  # номер счета
        self.percent = percent
        self.value = value  # сумма в рублях
        print(f'Счет #{self.num} принадлежащий {self.surname} был открыт.')
        print('*' * 50)

    def __del__(self):
        print('*' * 50)
        print(f'Счет #{self.num} принадлежащий {self.surname} был закрыт.')

    @staticmethod
    def convert(value, rate):
        return value * rate

    @classmethod
    def set_usd_rate(cls, rate):
        cls.rate_usd = rate

    @classmethod
    def set_eur_rate(cls, rate):
        cls.rate_eur = rate

    def convert_to_usd(self):
        print(f'Состояние счета: {Account.convert(self.value, Account.rate_usd)} {Account.suffix_usd}')

    def convert_to_eur(self):
        print(f'Состояние счета: {Account.convert(self.value, Account.rate_eur)} {Account.suffix_eur}')

    def edit_owner(self, surname):
        self.surname = surname

    def add_precents(self):
        self.value += self.value * self.percent
        print("Проценты были успешно начислены!")
        self.print_balance()

    def withdraw_money(self, val):
        if val > self.value:
            print(f'К сожалению у вас нет {val} {Account.suffix}')
        else:
            self.value -= val
            print(f'{val} {Account.suffix} было успешно снято!')
        self.print_balance()

    def add_money(self, val):
        self.value += val
        print(f'{val} {Account.suffix} были успешно начислены!')
        self.print_balance()

    def print_balance(self):
        print(f'Текущий баланс: {self.value} {Account.suffix}')

    def print_info(self):
        print("Информация о счете:")
        print("-" * 20)
        print(f'Номер счета: #{self.num}')
        print(f"Владелец: {self.surname}")
        self.print_balance()
        print(f"Проценты: {self.percent:.0%}")
        print("-" * 20)


acc = Account('Долгих', '12345', 0.03, 1000)
# acc.print_balance()
acc.print_info()
acc.convert_to_usd()
acc.convert_to_eur()
print()
Account.set_usd_rate(2)
Account.set_eur_rate(3)
acc.convert_to_usd()
acc.convert_to_eur()
print()
acc.edit_owner('Дюма')
acc.print_info()
acc.add_precents()
acc.withdraw_money(3000)
acc.withdraw_money(100)
acc.add_money(5000)
acc.withdraw_money(3000)
