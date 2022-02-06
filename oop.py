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


# class Account:
#     rate_usd = 0.013
#     rate_eur = 0.011
#     suffix = 'RUB'
#     suffix_usd = 'USD'
#     suffix_eur = 'EUR'
#
#     def __init__(self, surname, num, percent, value=0):
#         self.surname = surname
#         self.num = num  # номер счета
#         self.percent = percent
#         self.value = value  # сумма в рублях
#         print(f'Счет #{self.num} принадлежащий {self.surname} был открыт.')
#         print('*' * 50)
#
#     def __del__(self):
#         print('*' * 50)
#         print(f'Счет #{self.num} принадлежащий {self.surname} был закрыт.')
#
# @staticmethod
# def convert(value, rate):
#     return value * rate
#
# @classmethod
# def set_usd_rate(cls, rate):
#     cls.rate_usd = rate
#
# @classmethod
# def set_eur_rate(cls, rate):
#     cls.rate_eur = rate
#
# def convert_to_usd(self):
#     print(f'Состояние счета: {Account.convert(self.value, Account.rate_usd)} {Account.suffix_usd}')

#     def convert_to_eur(self):
#         print(f'Состояние счета: {Account.convert(self.value, Account.rate_eur)} {Account.suffix_eur}')
#
#     def edit_owner(self, surname):
#         self.surname = surname
#
#     def add_precents(self):
#         self.value += self.value * self.percent
#         print("Проценты были успешно начислены!")
#         self.print_balance()
#
#     def withdraw_money(self, val):
#         if val > self.value:
#             print(f'К сожалению у вас нет {val} {Account.suffix}')
#         else:
#             self.value -= val
#             print(f'{val} {Account.suffix} было успешно снято!')
#         self.print_balance()
#
#     def add_money(self, val):
#         self.value += val
#         print(f'{val} {Account.suffix} были успешно начислены!')
#         self.print_balance()
#
#     def print_balance(self):
#         print(f'Текущий баланс: {self.value} {Account.suffix}')
#
#     def print_info(self):
#         print("Информация о счете:")
#         print("-" * 20)
#         print(f'Номер счета: #{self.num}')
#         print(f"Владелец: {self.surname}")
#         self.print_balance()
#         print(f"Проценты: {self.percent:.0%}")
#         print("-" * 20)
#
#
# acc = Account('Долгих', '12345', 0.03, 1000)
# # acc.print_balance()
# acc.print_info()
# acc.convert_to_usd()
# acc.convert_to_eur()
# print()
# Account.set_usd_rate(2)
# Account.set_eur_rate(3)
# acc.convert_to_usd()
# acc.convert_to_eur()
# print()
# acc.edit_owner('Дюма')
# acc.print_info()
# acc.add_precents()
# acc.withdraw_money(3000)
# acc.withdraw_money(100)
# acc.add_money(5000)
# acc.withdraw_money(3000)
# import re
#
#
# class UserData:
#     def __init__(self, fio, old, ps, weight):
#         self.fio = fio
#         self.old = old
#         self.password = ps
#         self.weight = weight
#
#     @classmethod
#     def verify_fio(cls, fio):
#         if not isinstance(fio, str):
#             raise TypeError("ФИО должно быть строкой")
#         f = fio.split()
#         # print(f)  # ['Волков', 'Игорь', 'Николаевич']
#         if len(f) != 3:
#             raise TypeError("Неверный формат ФИО")
#         letters = "".join(re.findall(r'[a-zа-яё-]', fio, flags=re.IGNORECASE))
#         # print(letters)  # ВолковИгорьНиколаевич
#         for s in f:
#             if len(s.strip(letters)) != 0:
#                 raise TypeError("В ФИО можно использовать только буквы и дефис")
#
#     @classmethod
#     def verify_old(cls, old):
#         if not isinstance(old, int) or old < 14 or old > 100:
#             raise TypeError("Возраст должен быть числом в диапазоне от 14 до 100 лет")
#
#     @classmethod
#     def verify_weight(cls, w):
#         if not isinstance(w, (int, float)) or w < 20:
#             raise TypeError("Вес должен быть числом от 20 кг и выше")
#
#     @classmethod
#     def verify_ps(cls, ps):
#         if not isinstance(ps, str):
#             raise TypeError("Паспор должен быть строкой")
#         s = ps.split()
#         if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
#             raise TypeError("Неверный формат паспорта")
#
#     @property
#     def old(self):
#         return self.__old
#
#     @old.setter
#     def old(self, year):
#         self.verify_old(year)
#         self.__old = year
#
#     @property
#     def fio(self):
#         return self.__fio
#
#     @fio.setter
#     def fio(self, fio):
#         self.verify_fio(fio)
#         self.__fio = fio.split()
#
#     @property
#     def weight(self):
#         return self.__weight
#
#     @weight.setter
#     def weight(self, weight):
#         self.verify_weight(weight)
#         self.__weight = weight
#
#     @property
#     def password(self):
#         return self.__password
#
#     @password.setter
#     def password(self, ps):
#         self.verify_ps(ps)
#         self.__password = ps
#
#
# p1 = UserData("Волков Игорь Николаевич", 36, "1234 567890", 70.2)
# print(p1.__dict__)
# p1.fio = "Волков Николай Николаевич"
# p1.old = 40
# p1.password = "4567 789456"
# p1.weight = 60
# print(p1.__dict__)
# print(p1.old)

# class Point:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f"({self.x}, {self.y})"
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
#         print("Инициализатор базового класса Prop")
#         self._sp = sp
#         self._ep = ep
#         self.__color = color
#         self.__width = width
#
#     def get_width(self):
#         return self.__width
#
#     @property
#     def color(self):
#         return self.__color
#
#
# class Line(Prop):
#     def __init__(self, *args):
#         print("Переопределенный инициализатор класса Line")
#         super().__init__(*args)
#
#     def draw_line(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self.color}, {self.get_width()}")
#
#
# class Rect(Prop):
#     def draw_rect(self):
#         print(f"Рисование прямоугольник: {self._sp}, {self._ep}, {self.color}, {self.get_width()}")
#
#
# line = Line(Point(1, 2), Point(10, 20))
# line.draw_line()
# rect = Rect(Point(30, 40), Point(70, 80))
# rect.draw_rect()

# class Figure:
#     def __init__(self, color):
#         self.__color = color
#
#     @property
#     def color(self):
#         return self.__color
#
#     @color.setter
#     def color(self, c):
#         self.__color = c
#
#
# class Rectangle(Figure):
#     def __init__(self, width, height, color):
#         super().__init__(color)
#         self.__width = width
#         self.__height = height
#
#     @property
#     def width(self):
#         return self.__width
#
#     @width.setter
#     def width(self, w):
#         if w > 0:
#             self.__width = w
#         else:
#             raise ValueError("Ширина должна быть положительной")
#
#     @property
#     def height(self):
#         return self.__height
#
#     @height.setter
#     def height(self, h):
#         if h > 0:
#             self.__height = h
#         else:
#             raise ValueError
#
#     def area(self):
#         return self.__width * self.__height, self.color
#
#
# rect = Rectangle(10, 20, "green")
# rect.width = 2
# print(rect.width)
# print(rect.height)
# print(rect.color)
# print(rect.area())

# class Liquid:
#     def __init__(self, name, density):
#         self.name = name
#         self.density = density  # плотность
#
#     def edit_density(self, val):  # изменение плотности
#         self.density = val
#
#     def calc_v(self, m):  # вычисление объема жидкости, соответствующего заданной массе
#         v = round(m / self.density, 2)
#         print(f"Объем {m} кг {self.name} равен {v} m^3.")
#         return v
#
#     def calc_m(self, v):  # вычисление массы жидкости, соответствующей заданному объему
#         m = v * self.density
#         print(f"Вес {v} m^3 {self.name} составляет {m} кг.")
#         return m
#
#     def print_info(self):  # вывод информации о жидкости
#         print(f'Жидкость {self.name} (плотность = {self.density} kg/m^3).')
#
#
# class Alcohol(Liquid):  # спирт
#     def __init__(self, name, density, strength):
#         super().__init__(name, density)
#         self.strength = strength  # крепость
#
#     def edit_strength(self, val):  # изменение крепости
#         self.strength = val
#
#     def calc_v(self, m):
#         v = super().calc_v(m)
#         v_alc = v * self.strength
#         print(f"Объем алкоголя в {m} кг {self.name} составляет {v_alc} m^3.")
#         return v, v_alc
#
#     def calc_m(self, v):
#         m = super().calc_m(v)
#         m_alc = m * self.strength
#         print(f"Вес алкоголя {v} m^3 {self.name} составляет {m_alc} кг.")
#         return m, m_alc
#
#     def print_info(self):
#         print(f'Жидкость {self.name} (плотность = {self.density} kg/m^3), крепость = {self.strength:.0%}')
#
#
# a = Alcohol('Wine', 1064.2, 14)
# a.print_info()
# a.edit_density(1000)
# a.print_info()
# print()
# a.calc_m(0.5)
# a.calc_v(300)
# print()
# print(a.strength)
# a.edit_strength(20)
# print(a.strength)

# class Point:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f"({self.x}, {self.y})"
#
#     def is_digit(self):
#         if isinstance(self.x, (int, float)) and isinstance(self.y, (int, float)):
#             return True
#         return False
#
#     def is_int(self):
#         if isinstance(self.x, int) and isinstance(self.y, int):
#             return True
#         return False
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
#         print("Инициализатор базового класса Prop")
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     def set_coords(self, sp, ep):
#         if sp.is_digit() and ep.is_digit():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print("Координаты должны быть числами")
#
#
# class Line(Prop):
#
#     def draw_line(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#     def set_coords(self, sp, ep):
#         if sp.is_int() and ep.is_int():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print("Координаты должны быть числами")
#
#
# line = Line(Point(1, 2), Point(10, 20))
# line.draw_line()
# line.set_coords(Point(10, 20), Point(100, 200))
# line.draw_line()


# class Rect:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def show_rect(self):
#         print(f"Прямоугольник:\nШирина: {self.width}\nВысота: {self.height}")
#
#
# class RectFon(Rect):
#     def __init__(self, width, height, background):
#         self.fon = background
#         super().__init__(width, height)
#
#     def show_rect(self):
#         super().show_rect()
#         print(f"Фон: {self.fon}")
#
#
# class RectBorder(Rect):
#     def __init__(self, width, height, border):
#         super().__init__(width, height)
#         self.border = border
#
#     def show_rect(self):
#         super().show_rect()
#         print(f"Рамка: {self.border}")
#
#
# shape1 = RectFon(400, 200, "yellow")
# shape1.show_rect()
# print()
# shape2 = RectBorder(600, 300, "1px solid red")
# shape2.show_rect()


# class Point:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f"({self.x}, {self.y})"
#
#     def is_digit(self):
#         if isinstance(self.x, (int, float)) and isinstance(self.y, (int, float)):
#             return True
#         return False
#
#     def is_int(self):
#         if isinstance(self.x, int) and isinstance(self.y, int):
#             return True
#         return False
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     def set_coords(self, sp, ep):
#         if sp.is_digit() and ep.is_digit():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print("Координаты должны быть числами")
#
#
# class Line(Prop):
#
#     def draw_line(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#     def __set_one_coords(self,sp):
#         if sp.is_int():
#             self._sp = sp
#         else:
#             print("Координаты должны быть числами")
#
#     def __set_two_coords(self, sp, ep):
#         if sp.is_int() and ep.is_int():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print("Координаты должны быть числами")
#
#     def set_coords(self, sp, ep=None):
#         if ep is None:
#             self.__set_one_coords(sp)
#         else:
#             self.__set_two_coords(sp, ep)
#
#
# line = Line(Point(1, 2), Point(10, 20))
# line.draw_line()
# line.set_coords(Point(10, 20), Point(100, 200))
# line.draw_line()
# line.set_coords(Point(-10, -20))
# line.draw_line()


# class Point:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f"({self.x}, {self.y})"
#
#     def is_digit(self):
#         if isinstance(self.x, (int, float)) and isinstance(self.y, (int, float)):
#             return True
#         return False
#
#     def is_int(self):
#         if isinstance(self.x, int) and isinstance(self.y, int):
#             return True
#         return False
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     def set_coords(self, sp, ep):
#         if sp.is_digit() and ep.is_digit():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print("Координаты должны быть числами")
#
#     def draw(self):  # абстрактный метод
#         raise NotImplementedError("В дочернем классе должен быть определен метод Draw")
#
#
# class Line(Prop):
#
#     def draw(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# class Rect(Prop):
#
#     def draw(self):
#         print(f"Рисование прямоугольника: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# class Ellipse(Prop):
#
#     def draw(self):
#         print(f"Рисование эллипса: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# figs = list()
# figs.append(Line(Point(0, 0), Point(10, 10)))
# figs.append(Line(Point(10, 10), Point(10, 10)))
# figs.append(Rect(Point(50, 50), Point(100, 100)))
# figs.append(Ellipse(Point(-10, -10), Point(10, 10)))
#
# for f in figs:
#     f.draw()
#
# from abc import ABC, abstractmethod
#
#
# class Chess(ABC):
#     def draw(self):
#         print("Нарисовал шахматную доску")
#
#     @abstractmethod
#     def move(self):
#         print("Метод move() в базовом классе")
#
#
# class Queen(Chess):
#
#     def move(self):
#         super().move()
#         print("Ферзь перемещен на e2e4")
#
#
# q = Queen()
# q.draw()
# q.move()

# from abc import ABC, abstractmethod
#
#
# class Currency(ABC):
#     suffix = 'RUB'
#
#     def __init__(self, value):
#         self.value = value
#
#     @abstractmethod
#     def convert_to_rub(self):
#         pass
#
#     def print_value(self):
#         print(self.value, end=" ")
#
#
# class Dollar(Currency):
#     rate_to_rub = 74.16
#     suffix = 'USD'
#
#     def convert_to_rub(self):
#         rub = self.value * Dollar.rate_to_rub
#         return rub
#
#     def print_value(self):
#         super().print_value()
#         print(Dollar.suffix, end=" ")
#
#
# class Euro(Currency):
#     rate_to_rub = 90.14
#     suffix = "USD"
#
#     def convert_to_rub(self):
#         rub = self.value * Euro.rate_to_rub
#         return rub
#
#     def print_value(self):
#         super().print_value()
#         print(Euro.suffix, end=" ")
#
#
# d = [Dollar(5), Dollar(10), Dollar(50), Dollar(100)]
# e = [Euro(5), Euro(10), Euro(50), Euro(100)]
# print("*" * 50)
# for elem in d:
#     elem.print_value()
#     print(f"= {elem.convert_to_rub():.2f} {Currency.suffix}")
#
# print("*" * 50)
# for elem in e:
#     elem.print_value()
#     print(f"= {elem.convert_to_rub():.2f} {Currency.suffix}")
import cmath
from math import pi

# class Table:
#     def __init__(self, width=None, length=None, radius=None):
#         if radius is None:
#             # self._width = width
#             # self._length = length
#             # self.set_sides(width, length)
#             if length is None:
#                 self._width = self._length = width
#             else:
#                 self._width = width
#                 self._length = length
#         else:
#             self._radius = radius
#
#     # def set_sides(self, width=None, length=None):
#     #     if length is None:
#     #         self._width = self._length = width
#     #     else:
#     #         self._width = width
#     #         self._length = length
#
#     def calc_area(self):
#         raise NotImplementedError("В дочернем классе должен быть определен метод calc_area()")
#
#
# class Sq_table(Table):
#     def calc_area(self):
#         return self._width * self._length
#
#
# class Round_table(Table):
#     def calc_area(self):
#         return round(pi * self._radius ** 2, 2)
#
#
# t = Sq_table(20, 10)
# print(t.__dict__)
# print(t.calc_area())
#
# t2 = Sq_table(20)
# print(t2.__dict__)
# print(t2.calc_area())
#
# t1 = Round_table(radius=20)
# print(t1.__dict__)
# print(t1.calc_area())


# from abc import ABC, abstractmethod
#
#
# class IFather(ABC):
#     @abstractmethod
#     def display1(self):
#         pass
#
#     @abstractmethod
#     def display2(self):
#         pass
#
#
# class Child(IFather):
#     def display1(self):
#         print("Child Class")
#
#
# class Grandchild(Child):
#     def display2(self):
#         print("Grandchild Class")
#
#
# gc = Grandchild()
# gc.display1()
# gc.display2()

# class MyOuter:
#     age = 18
#
#     def __init__(self, name):
#         self.name = name
#
#     @classmethod
#     def outer_class_method(cls):
#         print("Я - метод внешнего класса")
#
#     class MyInner:
#         def __init__(self, inner_name):
#             self.inner_name = inner_name
#
#         def inner_method(self):
#             print("Я - метод внутреннего класса")
#             MyOuter.outer_class_method()
#             print(MyOuter.age)
#             # print(self.name)
#
#
#
# out = MyOuter('внешний')
# inner = out.MyInner('внутренний')
# print(inner.inner_name)
# inner.inner_method()


# class Color:
#
#     def __init__(self):
#         self.name = 'Green'
#         self.lg = self.LightGreen()
#
#     def show(self):
#         print("Name:", self.name)
#         self.lg.display()
#
#     class LightGreen:
#         def __init__(self):
#             self.name = "Light Green"
#             self.code = '024avc'
#
#         def display(self):
#             print("Name:", self.name)
#             print("Code:", self.code)
#
#
# outer = Color()
# outer.show()
# g = outer.lg
# g.display()

#
# class Employee:
#     def __init__(self):
#         self.name = "Employee"
#         self.intern = self.Intern()
#         self.head = self.Head()
#
#     def show(self):
#         print("Employee List")
#         print("Name", self.name)
#
#     class Intern:
#         def __init__(self):
#             self.name = "Smith"
#             self.id = "657"
#
#         def display(self):
#             print("Name", self.name)
#             print("Id", self.id)
#
#     class Head:
#         def __init__(self):
#             self.name = "Albina"
#             self.id = "007"
#
#         def display(self):
#             print("Name", self.name)
#             print("Degree", self.id)
#
#
# outer = Employee()
# outer.show()
# d1 = outer.intern
# d1.display()
# d2 = outer.head
# d2.display()

# class Geeks:
#     def __init__(self):
#         self.inner = self.Inner()
#
#     def show(self):
#         print('Outer Class')
#
#     class Inner:
#         def __init__(self):
#             self.inner_inner = self.InnerClass()
#
#         def show(self):
#             print("Inner Class")
#
#         class InnerClass:
#             def show(self):
#                 print("Inner Class of Inner Class")
#
#
# outer = Geeks()
# outer.show()
#
# # inner1 = outer.inner
# # inner1.show()
#
# inner2 = outer.inner.inner_inner
# inner2.show()

# class Computer:
#     def __init__(self):
#         self.name = "PC001"
#         self.os = self.OS()
#         self.cpu = self.CPU()
#
#     class OS:
#         def system(self):
#             return "Windows 10"
#
#     class CPU:
#         def make(self):
#             return "Intel"
#
#         def model(self):
#             return "Core-i7"
#
#
# cp = Computer()
# print(cp.os.system())
# print(cp.cpu.make())
# print(cp.cpu.model())

# class Base:
#     # def __init__(self):
#     #     self.db = self.Inner()
#
#     def display(self):
#         print("Base Class")
#
#     class Inner:
#         def display1(self):
#             print("Inner Of Base Class")
#
#
# class SubClass(Base):
#     def __init__(self):
#         print("SubClass")
#         super().__init__()
#
#     class Inner(Base.Inner):
#         def display2(self):
#             print("Inner Of SubClass")
#
#
# a = SubClass()
# a.display()
# print()
# # b = a.db
# b = SubClass.Inner()
# b.display1()
# print()
# b.display2()

# class Creature:
#     def __init__(self, name):
#         self.name = name
#
#
# class Animal(Creature):
#     def sleep(self):
#         print(self.name + " is sleeping")
#
#
# class Pet(Creature):
#     def play(self):
#         print(self.name + " is playing")
#
#
# class Dog(Animal, Pet):
#     def bark(self):
#         print(self.name + " is barking")
#
#
# d = Dog("Buddy")
# d.sleep()
# d.play()
# d.bark()

# class A(object):
#     # def __init__(self):
#     #     print("Инициализатор класса А")
#
#     def hi(self):
#         print("A")
#
#
# # class AA(object):
# #     def __init__(self):
# #         print("Инициализатор класса А")
#
#
# class B(A):
#     # def __init__(self):
#     #     print("Инициализатор класса B")
#         # super().__init__()
#     # def hi(self):
#     #     print("B")
#     pass
#
#
# class C(A):
#     # def __init__(self):
#     #     print("Инициализатор класса C")
#         # super().__init__()
#     def hi(self):
#         print("C")
#
#
# class D(B, C):
#     # def __init__(self):
#     #     print("Инициализатор класса D")
#     #     C.__init__(self)
#     # def hi(self):
#     #     print("D")
#     pass
#
#
# d = D()
# d.hi()
# print(D.__mro__)

# class Point:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f"({self.x}, {self.y})"
#
#
# class Styles:
#     def __init__(self):
#         print("Инициализатор Styles")
#         super().__init__()
#
#
# class Pos:
#     def __init__(self):
#         print("Инициализатор класса Pos")
#         super().__init__()
#
#
# class Line(Styles, Pos):
#     def __init__(self, sp: Point, ep: Point, color="red", width=1):
#         self.color = color
#         self.width = width
#         self.sp = sp
#         self.ep = ep
#         super().__init__()
#
#     def draw(self):
#         print(f"Рисование линии: {self.sp}, {self.ep}, {self.color}, {self.width}")
#
#
# l1 = Line(Point(10, 10), Point(100, 100), "green", 5)
# l1.draw()

# class Displayer:
#     @staticmethod
#     def display(message):
#         print(message)
#
#
# class LoggerMixin:
#     def log(self, message, filename="logfile.txt"):
#         with open(filename, 'a') as fh:
#             fh.write(message)
#
#     def display(self, message):
#         Displayer.display(message)
#         self.log(message)
#
#
# class MySubClass(LoggerMixin, Displayer):
#     def log(self, message, filename=""):
#         super().log(message, filename="subclass.txt")
#
#
# s = MySubClass()
# s.display("Эта строка будет печататься и сохраняться в файл")


# class Goods(object):
#     def __init__(self, name, weight, price):
#         super().__init__()
#         print("Init Goods")
#         self.name = name
#         self.weight = weight
#         self.price = price
#
#     def print_info(self):
#         print(f"{self.name}, {self.weight}, {self.price}")
#
#
# class MixinLog:
#     ID = 0
#
#     def __init__(self):
#         print("Init MixinLog")
#         self.ID += 1
#         self.id = self.ID
#
#     def save_sell_log(self):
#         print(f"{self.id}: товар был продан в 20:35 минут")
#
#
# class NoteBook(Goods, MixinLog):
#     pass
#
#
# n = NoteBook("HP", 1.5, 35000)
# m = Goods("HP", 1.5, 35000)
# print(type(n))
# # n.print_info()
# # n.save_sell_log()
# # print(NoteBook.__mro__)
#
# a = 5
# print(type(a))
# 00:02:30  => 00:2:30

# class Clock:
#     __DAY = 86400  # 24*60*60 - число секунд в одном дне
#
#     def __init__(self, secs: int):
#         if not isinstance(secs, int):
#             raise ValueError("Секунды должны быть целым числом")
#         self.secs = secs % self.__DAY
#
#     def get_format_time(self):
#         s = self.secs % 60  # секунды
#         m = (self.secs // 60) % 60  # минуты
#         h = (self.secs // 3600) % 24  # часы
#         return f"{Clock.__get_form(h)}:{Clock.__get_form(m)}:{Clock.__get_form(s)}"
#
#     @staticmethod
#     def __get_form(x):
#         return str(x) if x > 9 else "0" + str(x)
#
#     def __add__(self, other):
#         if not isinstance(other, Clock):
#             raise AttributeError("Правый операнд должен быть типом данных Clock")
#         return Clock(self.secs + other.secs)
#
#     def __eq__(self, other):
#         return self.secs == other.secs
#         # if self.secs == other.secs:
#         #     return True
#         # return False
#
#     def __ne__(self, other):
#         # return self.secs != other.secs
#         return not self.__eq__(other)
#
#     def __le__(self, other):
#         return self.secs <= other.secs
#
#     def __lt__(self, other):
#         return self.secs < other.secs
#
#     def __gt__(self, other):
#         return self.secs > other.secs
#
#     def __ge__(self, other):
#         return self.secs >= other.secs
#
#     def __getitem__(self, item):
#         if not isinstance(item, str):
#             raise ValueError("Ключ должен быть строкой")
#         if item == "hour":
#             return (self.secs // 3600) % 24
#         elif item == "min":
#             return (self.secs // 60) % 60
#         elif item == "sec":
#             return self.secs % 60
#         return "Неверный ключ"
#
#     def __setitem__(self, key, value):
#         if not isinstance(key, str):
#             raise ValueError("Ключ должен быть строкой")
#         if not isinstance(value, int):
#             raise ValueError("Значение должно быть целым числом ")
#         s = self.secs % 60  # секунды
#         m = (self.secs // 60) % 60  # минуты
#         h = (self.secs // 3600) % 24  # часы
#         if key == "hour":
#             self.secs = s + 60 * m + value * 3600
#         elif key == "min":
#             self.secs = s + 60 * value + h * 3600
#         elif key == "sec":
#             self.secs = value + 60 * m + h * 3600
#
#
# c1 = Clock(80000)
# # print(c1.get_format_time())  # 22:13:20
# c1["hour"] = 10
# print(c1["hour"], c1["min"], c1["sec"])  # 10 13 20

# c1 = Clock(100)
# c2 = Clock(100)
# c3 = Clock(300)
# print(c1.get_format_time())
# print(c2.get_format_time())
# print(c3.get_format_time())
#
# if c1 == c2:
#     print("Время равно")
# if c1 != c3:
#     print("Время не равно")
#
# print("c3 <= c1", c3 <= c1)
# print("c3 < c1", c3 < c1)
# print("c3 >= c1", c3 >= c1)
# print("c3 > c1", c3 > c1)


# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = list(marks)
#
#     def __getitem__(self, item):
#         if 0 <= item < len(self.marks):
#             return self.marks[item]
#         else:
#             raise IndexError("Неверный индекс")
#
#     def __setitem__(self, key, value):
#         if not isinstance(key, int) or key < 0:
#             raise TypeError("Индекс должен быть целым неотрицательным числом")
#
#         if key >= len(self.marks):
#             off = key + 1 - len(self.marks)
#             self.marks.extend([None] * off)
#
#         self.marks[key] = value
#
#     def __delitem__(self, key):
#         if not isinstance(key, int):
#             raise TypeError("Индекс должен быть целым числом")
#
#         self.marks[key] = None
#
#
# s1 = Student("Игорь", [5, 5, 3, 4, 5])
# print(s1[2])
# s1[10] = 4
# print(s1[2])
# del s1[2]
# print(s1.marks)

# class Point3D:
#     CH = "Координата должна быть числом"
#     RIGHT = "Правый операнд должен быть типом Point3D"
#
#     def __init__(self, x=0, y=0, z=0):
#         self.x = x
#         self.y = y
#         self.z = z
#
#     @staticmethod
#     def __check_value(v):
#         return isinstance(v, (int, float))
#
#     @staticmethod
#     def __check0(ex):
#         if ex.x == 0 or ex.y == 0 or ex.z == 0:
#             raise ZeroDivisionError("Ни одна из координат второго операнда не должна быть равна 0")
#
#     def __str__(self):
#         return f"{self.x}, {self.y}, {self.z}"
#
#     @property
#     def x(self):
#         return self.__x
#
#     @x.setter
#     def x(self, value):
#         if self.__check_value(value):
#             self.__x = value
#         else:
#             print(self.CH)
#
#     @property
#     def y(self):
#         return self.__y
#
#     @y.setter
#     def y(self, value):
#         if self.__check_value(value):
#             self.__y = value
#         else:
#             print(self.CH)
#
#     @property
#     def z(self):
#         return self.__z
#
#     @z.setter
#     def z(self, value):
#         if self.__check_value(value):
#             self.__z = value
#         else:
#             print(self.CH)
#
#     def __add__(self, other):
#         if not isinstance(other, Point3D):
#             raise ValueError(self.RIGHT)
#         else:
#             return Point3D(self.__x + other.x, self.__y + other.y, self.__z + other.z)
#
#     def __sub__(self, other):
#         if not isinstance(other, Point3D):
#             raise ValueError(self.RIGHT)
#         else:
#             return Point3D(self.__x - other.x, self.__y - other.y, self.__z - other.z)
#
#     def __mul__(self, other):
#         if not isinstance(other, Point3D):
#             raise ValueError(self.RIGHT)
#         else:
#             return Point3D(self.__x * other.__x, self.__y * other.__y, self.__z * other.__z)
#
#     def __truediv__(self, other):
#         if not isinstance(other, Point3D):
#             raise ValueError(self.RIGHT)
#         self.__check0(other)
#         return Point3D(self.__x / other.__x, self.__y / other.__y, self.__z / other.__z)
#
#     def __eq__(self, other):
#         if not isinstance(other, Point3D):
#             raise ValueError(self.RIGHT)
#         return self.__x == other.__x, self.__y == other.__y, self.__z == other.__z
#
#     def __getitem__(self, item):
#         if not isinstance(item, str):
#             raise ValueError("Ключ должен быть строкой")
#         elif item == "x":
#             return self.__x
#         elif item == "y":
#             return self.__y
#         elif item == "z":
#             return self.__z
#         else:
#             print("Неверное значение ключа")
#
#     def __setitem__(self, key, value):
#         if not isinstance(key, str):
#             raise ValueError("Ключ должен быть строкой")
#         if self.__check_value(value):
#             if key == "x":
#                 self.__x = value
#             elif key == "y":
#                 self.__y = value
#             elif key == "z":
#                 self.__z = value
#         else:
#             print("Координаты должны быть числами")
#
#
# pt = Point3D(12, 15, 18)
# # pt2 = Point3D(12, 15, 18)
# pt2 = Point3D(6, 3, 9)
# print(f"Координата 1-й точки: {pt}")
# print(f"Координата 2-й точки: {pt2}")
#
# pt3 = pt + pt2
# print(f"Сложение координат: ({pt3})")
#
# pt4 = pt - pt2
# print(f"Вычитание координат: ({pt4})")
#
# pt5 = pt * pt2
# print(f"Умножение координат: ({pt5})")
#
# pt6 = pt / pt2
# print(f"Деление координат: ({pt6})")
#
# print(f"Равенство координат: {pt == pt2}")
#
# print("x =", pt['x'], "x1 =", pt2['x'])
# print("y =", pt['y'], "y1 =", pt2['y'])
# print("z =", pt['z'], "z1 =", pt2['z'])
#
# pt['x'] = 20
# print(pt['x'])

# Полиморфизм

# class Rectangle:
#     def __init__(self, w, h):
#         self.w = w
#         self.h = h
#
#     def get_perimetr(self):
#         return 2 * (self.w + self.h)
#
#
# class Square:
#     def __init__(self, a):
#         self.a = a
#
#     def get_perimetr(self):
#         return 4 * self.a
#
#
# r1 = Rectangle(1, 2)
# r2 = Rectangle(3, 4)
# s1 = Square(10)
# s2 = Square(20)
#
# shape = [r1, r2, s1, s2]
# for g in shape:
#     print(g.get_perimetr())

# class Number:
#     def __init__(self, value):
#         self.value = value
#
#     def total(self, a):
#         return self.value + int(a)
#
#
# class Text:
#     def __init__(self, value):
#         self.value = value
#
#     def total(self, a):
#         return len(self.value + str(a))
#
#
# t1 = Number(10)
# t2 = Text("Python")
#
# print(t1.total(35))
# print(t2.total(35))

# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def info(self):
#         print(f"Я кот. Меня зовут {self.name}. Мой возраст {self.age}.")
#
#     @staticmethod
#     def make_sound():
#         print("Пушок мяукает")
#
#
# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def info(self):
#         print(f"Я собака. Меня зовут {self.name}. Мой возраст {self.age}.")
#
#     @staticmethod
#     def make_sound():
#         print("Мухтар гавкает")
#
#
# s1 = Cat("Пушок", 2.5)
# s2 = Dog("Мухтар", 4)
#
# s = [s1, s2]
#
# for i in s:
#     i.info()
#     i.make_sound()

# class Human:
#     def __init__(self, name, surname, age):
#         self.name = name
#         self.surname = surname
#         self.age = age
#
#     def info(self):
#         print(f"{self.name} {self.surname} {self.age}")
#
#
# class Student(Human):
#     def __init__(self, speciality, group, rating, name, surname, age):
#         super().__init__(name, surname, age)
#         self.speciality = speciality
#         self.group = group
#         self.rating = rating
#
#     def info(self):
#         print(f"{self.speciality} {self.group} {self.rating}", end=" ")
#         super().info()
#
#
# class Teacher(Human):
#     def __init__(self, speciality, experience, name, surname, age):
#         super().__init__(name, surname, age)
#         self.speciality = speciality
#         self.experience = experience
#
#     def info(self):
#         print(f"{self.speciality} {self.experience}", end=" ")
#         super().info()
#
#
# class Graduate(Student):
#     def __init__(self, topic, speciality, group, rating, name, surname, age):
#         super().__init__(speciality, group, rating, name, surname, age)
#         self.topic = topic
#
#     def info(self):
#         print(f"{self.topic}", end=" ")
#         super().info()
#
#
# groups = [
#     Student("Батодалаев", "Даши", 16, "ГК", "Web_011", 5),
#     Student("Загидуллин", "Линар", 32, "РПО", "PD_011", 5),
#     Graduate("Шугани", "Сергей", 15, "РПО", "PD_011", 5, "Защита персональных данных"),
#     Teacher("Башкиров", "Алексей", 45, "Разработка приложений", 20)
# ]
#
# for i in groups:
#     i.info()

# class Cat:
#     def __init__(self, name):
#         self.name = name
#
#     def __repr__(self):
#         return f"{self.__class__}: {self.name}"
#
#     def __str__(self):
#         return f"{self.name}"
#
#
# cat = Cat("Пушок")
# print(cat)

# class Point:
#     def __init__(self, *args):
#         self.coords = args
#         print(self.coords)
#
#     def __len__(self):
#         return len(self.coords)
#
#     def __abs__(self):
#         return list(map(abs, self.coords))
#
#
# p = Point(1, -8, 9)
# print(len(p))
# print(abs(p))
# import math
#
#
# class Point:
#     __slots__ = ('x', 'y', '__length')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.length = math.sqrt(x * x + y * y)
#
#     @property
#     def length(self):
#         return self.__length
#
#     @length.setter
#     def length(self, value):
#         self.__length = value
#
#
# pt = Point(1, 2)
# print(pt.length)
# pt.z = 10
# print(pt.__dict__)

# class Point:
#     __slots__ = ('x', 'y')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y


# class Point2D:
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# pt = Point(1, 2)
# pt2 = Point2D(1, 2)
# print("pt =", pt.__sizeof__())
# print("pt2 =", pt2.__sizeof__() + pt2.__dict__.__sizeof__())

# class Point:
#     __slots__ = ('x', 'y')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# class Point3D(Point):
#     __slots__ = 'z',
#
#     def __init__(self, x, y, z):
#         super().__init__(x, y)
#         self.z = z
#
#
# pt3 = Point3D(10, 20, 40)
# pt3.x = 30
# print(pt3.x, pt3.y, pt3.z)
# print(pt3.__dict__)

# class MyDecorator:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, a, b):
#         # print("перед вызовом функции")
#         res = self.func(a, b) ** 2
#         # print("после вызова функции")
#         return res
#
# @MyDecorator
# def function(a, b):
#     return a * b
#
#
# print(function(2, 3))

# class Counter:
#     def __init__(self):
#         self.counter = 0
#
#     def __call__(self, *args, **kwargs):
#         self.counter += 1
#         print(self.counter)
#
#
# c1 = Counter()
# c1()
# c1()
# c1()
# c2 = Counter()
# c2()
# c2()

# class StripChars:
#     def __init__(self, chars):
#         self.chars = chars
#
#     def __call__(self, string):
#         if not isinstance(string, str):
#             raise ValueError("Аргумент должен быть строкой")
#
#         return string.strip(self.chars)
#
# # Функтор
# s1 = StripChars("?:!.; ")
# print(s1("   ?  Hello. world  !      "))
# print(s1("world  : ;      "))
#
#
# def string_strip(chars):
#     def wrap(string):
#         if not isinstance(string, str):
#             raise ValueError("Аргумент должен быть строкой")
#         return string.strip(chars)
#     return wrap
#
#
# s1 = string_strip("?:!.; ")
# print(s1("   ?  Hello. world  !      "))


# class MyDecorator:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, *args, **kwargs):
#         print("перед вызовом функции")
#         res = self.func(*args, **kwargs)
#         print("после вызова функции")
#         return res
#
#
# @MyDecorator
# def function(a, b):
#     return a * b
#
#
# @MyDecorator
# def function1(a, b, c):
#     return a * b * c
#
#
# @MyDecorator
# def function3(a, b, c, d):
#     return a * b * c * d
#
#
# print(function(2, 3))
# print(function1(2, 3, 2))
# print(function3(2, 3, 2, 5))

# class MyDecorator:
#     def __init__(self, arg):
#         self.name = arg
#
#     def __call__(self, func):
#         def wrap(*args, **kwargs):
#             print("перед вызовом функции")
#             print(self.name)
#             func(*args, **kwargs)
#             print("после вызова функции")
#
#         return wrap
#
#
# @MyDecorator("test2")
# def function(a, b):
#     print(a, b)
#
#
# function(2, 5)

# class Power:
#     def __init__(self, arg):
#         self.name = arg
#
#     def __call__(self, func):
#         def wrap(*args, **kwargs):
#             res = func(*args, **kwargs)
#             return res ** self.name
#
#         return wrap
#
#
# @Power(5)
# def function(a, b):
#     return a * b
#
#
# print(function(2, 2))

# def dec(fn):
#     def wrap(*args, **kwargs):
#         print("*" * 20)
#         fn(*args, **kwargs)
#         print("*" * 20)
#
#     return wrap
#
#
# class Person:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     @dec
#     def info(self):
#         print(f"{self.name} {self.surname}")
#
#
# p1 = Person("Виталий", "Карасев")
# p1.info()
# def decorator(cls):
#     class Wrapper(cls):
#         def doubler(self, value):
#             return value * 2
#
#     return Wrapper
#
#
# @decorator
# class ActualClass:
#     def __init__(self):
#         print("Init class ActualClass")
#
#     def quad(self, value):
#         return value * 4
#
#
# obj = ActualClass()
#
# print(obj.quad(4))
# print(obj.doubler(4))


# class Message:
#     _REGISTRY = {}
#
#     def __init__(self, text):
#         self.text = text
#
#     @classmethod
#     def register(cls, name):
#         def decorator(klass):
#             cls._REGISTRY[name] = klass
#             return klass
#
#         return decorator
#
#     @classmethod
#     def create(cls, message_type, text):
#         klass = cls._REGISTRY.get(message_type)
#         if klass is None:
#             raise ValueError("Такого мессенджера нет.")
#         print(text, end=" ")
#
#         return klass(text)
#
#
# @Message.register('Telegram')
# class TelegramMessage(Message):
#     def send(self):
#         print("(Telegram)")
#
#
# @Message.register('WhatsApp')
# class WhatsAppMessage(Message):
#     def send(self):
#         print("(WhatsApp)")
#
#
# @Message.register('Viber')
# class WhatsAppMessage(Message):
#     def send(self):
#         print("(Viber)")
#
#
# m1 = Message.create("Telegram", "text")
# m1.send()
# m2 = Message.create("WhatsApp", "new text")
# m2.send()
# m3 = Message.create("Viber", "text new text")
# m3.send()


# class Person:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, value):
#         self.__name = value
#
#     @property
#     def surname(self):
#         return self.__surname
#
#     @surname.setter
#     def surname(self, value):
#         self.__surname = value
#
#
# p = Person("Ivan", "Petrov")

# class String:
#     def __init__(self, value=None):
#         if value:
#             self.set(value)
#
#     def set(self, value):
#         self.__value = value
#
#     def get(self):
#         return self.__value
#
#
# class Person:
#     def __init__(self, name, surname):
#         self.name = String(name)
#         self.surname = String(surname)
#
#
# p = Person("Ivan", "Petrov")
# print(p.name.get())
# p.name.set("Viktor")
# print(p.name.get())


# Дескриптор
# __get__()
# __set__()
# __delete__()
# __set_name__()
# class ValidString:
#     def __set_name__(self, owner, name):
#         self.__name = name
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.__name]
#
#     def __set__(self, instance, value):
#         if not isinstance(value, str):
#             raise ValueError(f"{self.__name} должно быть строкой")
#         instance.__dict__[self.__name] = value
#
#
# class Person:
#     name = ValidString()
#     surname = ValidString()
#
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#
# p = Person("Ivan", "Petrov")
# print(p.name)
# print(p.surname)
# p.surname = "Birukov"
# print(p.surname)
# class NonNegative:
#     def __set_name__(self, owner, name):
#         self.name = name
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.name]
#
#     def __set__(self, instance, value):
#         if value < 0:
#             raise ValueError(f"Значение должно быть положительным")
#         instance.__dict__[self.name] = value
#
#
# class Order:
#     price = NonNegative()
#     quantity = NonNegative()
#
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#
#     def total(self):
#         return self.price * self.quantity
#
#
# apple = Order("apple", 5, 10)
# apple.price = 10
# apple.quantity = -20
# print(apple.total())

# class ReadIntX:
#     def __set_name__(self, owner, name):
#         self.name = "_x"
#
#     def __get__(self, instance, owner):
#         return getattr(instance, self.name)
#
#
# class Integer:
#     @classmethod
#     def verify_coord(cls, coord):
#         if not isinstance(coord, int) or coord < 0:
#             raise TypeError(f"Координата {coord} должна былжна быть целым положительным числом")
#
#     def __set_name__(self, owner, name):
#         self.name = "_" + name
#
#     def __get__(self, instance, owner):
#         return getattr(instance, self.name)  # return instance.__dict__[self.name]
#
#     def __set__(self, instance, value):
#         self.verify_coord(value)
#         setattr(instance, self.name, value)       # instance.__dict__[self.name] = value
#
#
# class Point3D:
#     x = Integer()
#     y = Integer()
#     z = Integer()
#     xr = ReadIntX()
#
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#
#
# p1 = Point3D(1, 2, 3)
# # print(p1.__dict__)
# # p1.y = 3
# # print(p1.__dict__)
# p1.__dict__["xr"] = 5
# p1.xr = -50
# print(p1.xr, p1.__dict__)


# Метаклассы

# a = 5
# print(type(a))
# print(type(int))

# class MyList(list):
#     def get_length(self):
#         return len(self)


# MyList = type(
#     'MyList',
#     (list,),
#     dict(get_length=lambda self: len(self))
# )
#
# lst = MyList()
# lst.append(8)
# lst.append(2)
# lst.append(4)
# lst[0] = 3
# print(lst, lst.get_length())


# class MyMetaclass(type):
#     def __new__(mcs, name, bases, attr):
#         print("Создание нового объекта", name)
#         return super(MyMetaclass, mcs).__new__(mcs, name, bases, attr)
#
#     def __init__(cls, name, bases, attr):
#         print("Инициализация класса", name)
#         super(MyMetaclass, cls).__init__(name, bases, attr)
#
#
# class Student(metaclass=MyMetaclass):
#     def __init__(self, name):
#         self.name = name
#
#     def get_name(self):
#         return self.name
#
#
# stud = Student("Анна")
# print(stud.get_name())
# print(type(stud))
# print(type(Student))
# ================================================================

# import math
#
# print(math.pi)
#
# from math import *
#
# print(pi)

# import geometry.rect
# import geometry.sq
# import geometry.trian
# from geometry import rect, sq, trian
# # import geometry
# # from geometry import *
#
#
# def main():
#     r1 = rect.Rectangle(1, 2)
#     r2 = rect.Rectangle(3, 4)
#
#     s1 = sq.Square(10)
#     s2 = sq.Square(20)
#
#     t1 = trian.Triangle(1, 2, 3)
#     t2 = trian.Triangle(5, 6, 7)
#
#     shape = [r1, r2, s1, s2, t1, t2]
#     for g in shape:
#         print(g.get_perimetr())
#
#
# if __name__ == "__main__":
#     main()


# from project.shapes import rectangle
# from project.shapes import circle
# from project.shapes import cylinder
#
# rect = [rectangle.Rectangle(3, 7), rectangle.Rectangle(2, 7), rectangle.Rectangle(19, 12)]
# circles = [circle.Circle(4), circle.Circle(2), circle.Circle(8)]
# cylinders = [cylinder.Cylinder(4, 7), cylinder.Cylinder(2, 5), cylinder.Cylinder(9, 3)]
#
# circle_max = max(circles, key=lambda c: c.get_circle_square())
#
# print("*" * 50)
# print(f"Окружность с наибольшей площадью: ", end=" ")
# circle_max.print_circle()
#
# rect_min = min(rect, key=lambda r: r.get_rect_perimetr())
# print("Прямоугольник с наименьшим периметром: ", end=" ")
# rect_min.print_rect()
#
# c_v = list(map(lambda c: c.get_volume(), cylinders))
# c_v_avg = sum(c_v) / len(c_v)
#
# print(f"Средний объем всех циландров: {c_v_avg:.2f}")

import pickle


# file_name = 'basket.txt'
# shop_list = {
#     "фрукты": ("яблоки", "манго"),
#     "овощи": ["морковь"],
#     "бюджет": 1000
# }
#
# with open(file_name, "wb") as fh:
#     pickle.dump(shop_list, fh)
#
# with open(file_name, "rb") as fh:
#     print(pickle.load(fh))

# class Test:
#     a_number = 35
#     a_string = "Привет"
#     a_list = [1, 2, 3]
#     a_dict = {'фрукты': ('яблоки', 'манго'), 'овощи': ['морковь'], 'бюджет': 1000}
#     a_tuple = (22, 35)
#
#     def __str__(self):
#         return f"Число: {Test.a_number}\n" \
#                f"Строка: {Test.a_string}\n" \
#                f"Список: {Test.a_list}\n" \
#                f"Словать: {Test.a_dict}\n" \
#                f"Кортеж: {Test.a_tuple}\n"
#
#
# obj = Test()
#
# my_obj = pickle.dumps(obj)
# print(f"Сериализация в строку:\n{my_obj}\n")
#
# l_obj = pickle.loads(my_obj)
# print(f"Десериализация из строки:\n{l_obj}\n")

# class Test2:
#     def __init__(self):
#         self.a = 35
#         self.b = "test"
#         self.c = lambda x: x * x
#
#     def __str__(self):
#         return f"{self.a} {self.b} {self.c(2)}"
#
#     def __getstate__(self):
#         attr = self.__dict__.copy()
#         del attr['c']
#         return attr
#
#     def __setstate__(self, state):
#         self.__dict__ = state
#         self.c = lambda x: x * x
#
#
# t1 = Test2()
# t2 = pickle.dumps(t1)
# t3 = pickle.loads(t2)
#
# print(t3.__dict__)
# print(t3)

# class TextReader:
#     def __init__(self, filename):
#         self.filename = filename
#         self.file = open(filename)
#         self.count = 0
#
#     def read_line(self):
#         self.count += 1
#         line = self.file.readline()
#         if not line:
#             return None
#         if line.endswith("\n"):
#             line = line[:-1]
#         return f"{self.count}: {line}"
#
#     def __getstate__(self):
#         state = self.__dict__.copy()
#         del state['file']
#         return state
#
#     def __setstate__(self, state):
#         self.__dict__.update(state)
#         file = open(self.filename)
#         for i in range(self.count):
#             file.readline()
#         self.file = file
#
#
# reader = TextReader("hello.txt")
# print(reader.read_line())
# print(reader.read_line())
#
# new_reader = pickle.loads(pickle.dumps(reader))
# print(new_reader.read_line())
# print(new_reader.read_line())


# data = {
#     'name': 'Olga',
#     'age': 26,
#     'hobbies': ('running', 'singing'),
#     'children': [
#         {
#             'name': "Alice",
#             'age': 6
#         },
#         {
#             'name': "Rick",
#             'age': 8
#         }
#     ]
# }

# with open("data_file.json", "w") as fw:
#     json.dump(data, fw, indent=4)
#
# with open("data_file.json", "r") as fw:
#     print(json.load(fw))

# json_string = json.dumps(data, sort_keys=True)
#
# print(json.loads(json_string))

# x = {"name": "Виктор"}
# y = {"name": "Виктор"}
# print(json.dumps(x))
# print(json.dumps(y, ensure_ascii=False))

# import json
# from random import choice
#
#
# def get_person():
#     name = ''
#     tel = ''
#
#     letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
#     num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
#
#     while len(name) != 7:
#         name += choice(letters)
#     # print(name)
#
#     while len(tel) != 10:
#         tel += choice(num)
#     # print(tel)
#
#     person = {
#         'name': name,
#         'tel': tel
#     }
#     return person
#
#
# def write_json(person_dict):
#     try:
#         data = json.load(open("persons.json"))
#     except FileNotFoundError:
#         data = []
#
#     data.append(person_dict)
#     with open('persons.json', 'w') as f:
#         json.dump(data, f, indent=2)
#
#
# for i in range(5):
#     write_json(get_person())
import json


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __str__(self):
        a = ''
        for i in self.marks:
            a += str(i) + ", "
        return f"Студент {self.name}: {a[:-2]}"

    def add_mark(self, mark):
        self.marks.append(mark)

    def delete_mark(self, index):
        self.marks.pop(index)

    def edit_makr(self, index, new_mark):
        self.marks[index] = new_mark

    def averange_mark(self):
        return round(sum(self.marks) / len(self.marks), 2)

    @classmethod
    def dump_to_json(cls, stud, filename):
        data = {"name": stud.name, "marks": stud.marks}
        with open(filename, "w") as f:
            json.dump(data, f, indent=2)

    @classmethod
    def load_from_file(cls, filename):
        with open(filename, "r") as f:
            print(json.load(f))


class Group:
    def __init__(self, students, group):
        self.students = students
        self.group = group

    def __str__(self):
        a = ''
        for i in self.students:
            a += str(i) + "\n"
        return f"Группа: {self.group}\n{a}"

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, index):
        return self.students.pop(index)

    @classmethod
    def change_group(cls, group1, group2, index):
        return group2.add_student(group1.remove_student(index))

    @classmethod
    def dump_group(cls, file, group):
        with open(file, 'w') as f:
            stud_list = []
            for i in group.students:
                stud_list.append([i.name, i.marks])
            tmp = {"Students": stud_list}
            json.dump(tmp["Students"], f)

    @classmethod
    def upload_jornal(cls, filename):
        with open(filename, "r") as f:
            print(json.load(f))



st1 = Student("Bodnya", [5, 4, 3, 4, 5, 3])
st2 = Student("Nikolaenko", [2, 3, 5, 4, 2])
st3 = Student("Birukov", [3, 5, 3, 2, 5, 4])
sts = [st1, st2]
my_group = Group(sts, "ГК Python")
print(my_group)
my_group.add_student(st3)
print(my_group)
my_group.remove_student(1)
print(my_group)
group22 = [st2]
my_group2 = Group(group22, "ГК Web")
print(my_group2)
Group.change_group(my_group, my_group2, 0)
print("*" * 20)
print(my_group)
print(my_group2)
Student.dump_to_json(st1, "student.json")
# Student.dump_to_json(st2, "student.json")
Student.load_from_file("student.json")

Group.dump_group("group.json", my_group2)
# Group.dump_group("group.json", my_group)
Group.upload_jornal("group.json")
