# name = "Elena"
# age = 20
# print(name + str(age))  # строчный комментарий
# a = 1
# b = 2
# print("a:", a)
# print("b:", b)

# s1 = "Hello"
# s2 = "Python"
# s3 = s1 + ", " + s2 + "!\t\t"
# print(s3 * 5)

# a = 2.65445634546546746844654541
# print(a)
# print(type(a))

# print(6 / 3)
# print(7 / 3)
# print(6 // 3)
# print(7 // 3)

# num = 9876
# res = (num % 10) * 1000
# # print(res)
# num = num // 10
# # print(num)
# res += (num % 10) * 100
# # print(res)
# num = num // 10
# # print(num)
# res += (num % 10) * 10
# # print(res)
# num = num // 10
# # print(num)
# res += num % 10
# print(res)

# num1 = "2"
# num2 = 3
# res = int(num1) + num2
# print(res)

# print(int(3.8))  # 3
# print(round(3.8))  # 4
# print(round(3.894, 2))  # 4
# print(round(5 / 3, 2))

# a = '5.2'
# b = 10
# c = float(a) + b
# print(c)

# a = 1
# b = 2
# a, b = b, a
# print(a, b)

# name = "Igor"
# age = 25
# grade = 9.2
# print("It's %s, %d. Level: %.2f" % (name, age, grade))
#
# print("This is a {0}. It's {1}".format("ball", "red"))


# Число 5 в степени 2 равно: 25

# num = int(input("Введите число: "))
# power = int(input("Введите степень: "))
# res = num ** power
# print("Число", num, "в степени", power, "равно:", res)
# print("Результат: %.2f" % res)

# Boolean (bool)
# False = False, 0, пустая строка, None
# b1 = True
# b2 = False
# print(b1 + 5)
# print(b2 + 5)
# print(type(b1))
# print(bool("python"))
# print(bool(None))

# test = None
# print(test)
# print(test is None)
# test = 5
# print(test)
# print(test is None)
# print("привет" > "ПРИВЕТ")
# print(2 * 5 > 7 >= 5 + 3)
# a = 10
# b = 5
# c = a == b
# print(a, b, c)

# print(5 - 3 == 2 or 3 + 3 == 4)
# print(not 9 - 9)

# cnt = 5
# if cnt < 10:
#
#     cnt += 1  # cnt = cnt + 1
#
#     print(cnt)
# age = int(input("Введите свой возраст: "))
# if age >= 18:
#     print("Доступ на сайт разрешен")
# else:
#     print("Доступ запрещен")

# a = 15
# b = 5
# if a > b:
#     print("a > b")
# elif a < b:
#     print("b > a")
# else:
#     print("a == b")
# day = int(input("Введите день недели (цифрой): "))
# if 1 <= day <= 5:  # (day >= 1) and (day <= 5)
#     print("Рабочий день - ", end="")
#     if day == 1:
#         print("понедельник")
#     if day == 2:
#         print("вторник")
#     if day == 3:
#         print("среда")
#     if day == 4:
#         print("четверг")
#     if day == 5:
#         print("пятница")
# elif day == 6 or day == 7:
#     print("Выходной день - ", end="")
#     if day == 6:
#         print("суббота")
#     if day == 7:
#         print("воскресенье")
# else:
# #     print("Такого дня недели не существует!")
# m = int(input("Введите номер месяца: "))
# if 1 <= m <= 12:
#     if m == 1 or m == 2 or m == 12:
#         print("Зима")
#     if m == 3 or m == 4 or m == 5:
#         print("Весна")
# else:
#     print("Ошибка ввода данных")


# n = int(input("Введите количество ворон: Введите количество ворон: Введите количество ворон: Введите количество ворон: "
#               "Введите количество ворон: "))
# if 0 <= n <= 9:
#     if n == 1:
#         print("На ветке", n, "ворона")
#     elif 2 <= n <= 4:
#         print("На ветке", n, "вороны")
#     elif 5 <= n <= 9 or n == 0:
#         print("На ветке", n, "ворон")
# else:
#     print("Ошибка ввода")

# уловие ? TRUE : FALSE

# TRUE if условие else FALSE

# a, b = 20, 10
# print("a == b" if a == b else "a > b" if a > b else "b > a")

# try-except
# a = input('Введите значения a: ')
# b = input('Введите значения b: ')
# try:
#     a = int(a)
#     b = int(b)
# except ValueError:
#     a = str(a)
#     b = str(b)
# finally:
#     print(a + b)

# i = 1
# while i <= 20:
#     if i % 2 == 0:
#         print("i =", i)
#     i += 1

# a = int(input("Укажите количество символов: "))
# i = 0
# while i < a:
#     print("*")
#     i += 1
#
# zvezda = int(input("Введите количество звездочек:"))
#
# print("*" * zvezda)


# n = int(input("начало диапазона : "))
# m = int(input("конец диапазона : "))
# i = n
# sum1 = 0
# while i <= m:
#     if i % 2 != 0:
#         sum1 += i
#     i += 1
# print(sum1)

# n = input("Введите целое число: ")
# while type(n) != int:
#     try:
#         n = int(n)
#     except ValueError:
#         print("Число не целое!")
#         n = input("Введите целое число: ")
#
# if n % 2 == 0:
#     print("Четное")
# else:
#     print("Нечетное")


# i = 1
# while True:
#     n = int(input())
#     if n == 0:
#         print(i)
#         break
#     i *= n


# i = 0
# while i < 10:
#     if i == 5:
#         break
#     print(i)
#     i += 1
# else:
#     print("Цикл окончен, i =", i)

# i = 1
# while i <= 9:
#     j = 1
#     while j <= 9:
#         print(i, "*", j, "=", i*j, "\t\t", end="")
#         j += 1
#     print()
#     i += 1

# i = 1
# while i <= 5:
#     j = 1
#     while j <= 5:
#         print("+" if i == j else " ", end="")
#         j += 1
#     print()
#     i += 1

# i1 = 0
# while i1 < 5:
#     print(" " * i1 + "+")
#     i1 += 1
#
# i = 0
# while i < 5:
#     j = 0
#     while j < i:
#         print(" ", end="")
#         j += 1
#     print("+")
#     i += 1

# for i in collection:
#   print(i)

# for i in "Hello":
#     print(i)

# i = 1
# for color in "red", "orange", "yellow", "green", "blue", 1, 20, 0.3:
#     print("color:", color)
#     i += 1

# range(start, stop, step)

# for i in range(2, 10, 2):
#     print(i, end=" ")

# x = int(input("Введите число: "))
#
# for i in range(1, x):
#     if x % i == 0:
#         print(i, end=" ")

# for i in range(11, 100, 11):
#     print(i, end=" ")
# print()
# for x in range(10, 100):
#     if x % 11 == 0:
#         print(x, end=" ")
# print()
# for y in range(10, 100):
#     if y % 10 == y // 10:
#         print(y, end=" ")

# for i in range(3):
#     print(i)
#     if i == 1:
#         break
# else:
#     print("done")


# w = int(input("Введите длину прямоугольника: "))
# h = int(input("Введите высоту прямоугольника: "))
# for i in range(h):
#     for j in range(w):
#         if (i == 0 or i == h - 1) or (j == 0 or j == w - 1):
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()
# w = int(input("ширина "))
# h = int(input("длина "))
# for i in range(h):
#     for j in range(w):
#         print("+" if i == 0 or i == h - 1 or j == 0 or j == w - 1 else " ", end="")
#     print()

# w = int(input("Введите ширину: "))
# h = int(input("Введите высоту: "))
# for i in range(h):
#     if i == 0 or i == h - 1:
#         for j in range(w):
#             print('*', end=' ')
#     else:
#         print('*', end=' ')
#         for j in range(1, w - 1):
#             print(' ', end=' ')
#         print('*', end=' ')
#     print()

# print([i*2 for i in "Hello"])
# print([i for i in range(30) if i % 2 == 0])

# num = [8, 3, 9, 4, 1]
# print(num)
# print("Длина списка", len(num))
# print(id(num))
# print(num[0])
# print(num[-3])
# num[1] = 256
# print(num)
# num[3] += 100
# print(num)
# print(id(num))

# n = list(range(10, 2, -2))
# print(n)
# n2 = [10, 8, 6, 4]
# print(id(n))
# print(id(n2))
# if n == n2:
#     print("списки равны")
# else:
#     print("списки разные")
# n = 5
# print([i ** 2 for i in range(1, n + 1)])
# print([i * 3 for i in "list"])
# a = [1, 2, 3]
# b = [4, 5]
# c = a + b
# print(c)
# d = b * 3
# print(d)
# a = [0] * int(input("Введите количество элементов списка: "))
# print(a)
# for i in range(len(a)):
#     a[i] = int(input("-> "))
# print(a)
# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# a = [6, 4, 5, 7, 8]
# print(a)
# for i in range(len(a)):
#     print(a[i] * 2, end=" ")
#
# print()
# for i in a:
#     print(i * 2, end=" ")

# lst = [1, 2, 3, 4, 5]
# print(lst)
# print("*" * 16)
# for i in range(len(lst)):
#     lst[i] *= 5
# print(lst)
# print("*" * 16)
# lst1 = [1, 2, 3, 4, 5]
# print(lst1)
# print("*" * 16)
# for i in lst1:
#     i *= 5
# print(lst1)

# a = [int(input("-> ")) for i in range(int(input("n = ")))]

# a = list(range(21, 41))
# print(a)
# sum1 = 0
# cool = 0
# for i in range(len(a)):
#     if a[i] % 2 == 0:
#         cool += 1
#     else:
#         sum1 += a[i]
# print("summa ", sum1, "\nколичество", cool)

# a = [int(input("-> ")) for i in range(int(input("n ")))]
# sum1 = 0
# count = 0
# for i in range(len(a)):
#     sum1 += a[i]
#     if a[i] != 0:
#         count += 1
# print(sum1 / count)

# a = [7, 9, 2, 1, 17]
# a[0], a[1] = a[1], a[0]
# print(a)

# срезы [start:stop:step]
# s = [1, 2, 3, 4, 5, 6, 7]
# # print(s)
# s.append('add')  # добавляет элемент в конец списка
# # print(s)
# s.extend([1, 2, 3])  # добавляет множество элементов из указанного объекта
# # print(s)
# s.extend('add')
# # print(s)
# s.insert(1, 100)
# print(s)

# s1 = []
# n = int(input("Количество элементов списка"))  # 5
# for num in range(n):
#     x = int(input("-> "))
#     s1.append(x)
# print(s1)
# a = []
# n = int(input("введите количество элементов "))
# for i in range(n):
#     x = int(input("-> "))
#     if x % 3 == 0:
#         a.append(x)
#     else:
#         print("число", x, "на 3 не делится")
#
# print(a)

# a = [1, 2, 3]
# b = [11, 22, 33]
# c = []
# for i in range(len(a)):
#     c.append(a[i])
#     c.append(b[i])
# print(c)

# s[7:] = []
# print(s)
# s.append(100)
# s.remove(100)
# print(s)
# last = s.pop()
# print(last)
# print(s)
# second = s.pop(-2)
# print(second)
# print(s)
# first = s.pop(0)
# print(first)
# print(s)
# s.clear()
# print(s)
# del s[:]
# # print(s)
# del s[2]
# print(s)
#
# s.extend([3, 1, 3, 20, 3, 4, 50, 3])
# print(s)
# num = s.count(3)
# print(num)
# ind = s.index(3, 2, -1)
# print(ind)
# s_copy = s.copy()
# print(s)
# print(s_copy)
# s.append(120)
# print(s)
# print(s_copy)
# s.reverse()
# print(s)
# s.sort(reverse=True)
# print(s)
# sorted_s = sorted(s, reverse=True)
# print(sorted_s)
# print(s)
#
# s2 = ["Виталий", "Сергей", "Александр", "Анна"]
# s2.sort(key=len, reverse=True)
# print(s2)

# Генарация случайных данных
import copy
import random as r

# print(r.randint(0, 9))
# print(r.randrange(1, 10, 2))
#
# cities = ["Москва", "Новосибирс", "Воронеж", "Сочи", "Екатеринбург"]
# r.shuffle(cities)
# print(cities)
# c = [2, 5, 6, 4, 7, 8, 9, 1]
# print(r.choices(c, k=4))
#
# print(r.uniform(10.5, 25.5))
# print(round(r.uniform(10.5, 25.5), 2))

# max1 = ["Москва", "Новосибирс", "Воронеж", "Сочи", "Екатеринбург"]
# print(max1)
# print("len =", len(max1))
# print("min =", min(max1))
# print("max =", max(max1))
# print("sum =", sum(max1))

# n = [r.randint(0, 100) for i in range(10)]
# print(n)
# maxim = max(n)
# n.remove(maxim)
# n.insert(0, maxim)
# print(maxim)
# print(n)


# n = [r.randint(0, 10) for i in range(10)]
# print(n)
# minim = min(n)
# print(minim)
# indexmin = n.index(minim)
# print(indexmin)
# # del n[0: indexmin]
# print(n[indexmin:])
#
# # print(n)

# x = list('1add26dfta6')
# print(x)
# print('a' not in x)
# print('e' not in x)
#
# lst = []
# if len(lst) == 0:
#     print("list is empty")

# user1 = ["Игорь", "Владимир", "Алла"]
# user2 = copy.deepcopy(user1)
# user2.append("Виктория")
# print(user1)
# print(user2)
# #  is
# print(user1 is user2)

# m = [
#     [1, 2, 3, 4],  # строка 0
#     [5, 6, 7, 8],  # строка 1
#     [9, 10, 11, 12]  # строка 2
# ]
# print(m)
# print(m[1][2])
# for row in range(len(m)):
#     for col in range(len(m[row])):
#         print(m[row][col], end="\t")
#     print()
# print()
# for row in m:
#     for x in row:
#         print(x, end="\t")
#     print()

# w, h = 5, 3
# matrix = [[x * y for x in range(1, w+1)] for y in range(1, h+1)]
# print(matrix)
# for row in matrix:
#     for x in row:
#         print(x, end="\t")
#     print()

# for x, y in [[1, 2], [3, 4], [5, 6], [7, 8]]:
#     print(x, '*', y, '=', x*y)

# w, h = 5, 4
# mas = [[r.randint(1, 30) for x in range(w)] for y in range(h)]
#
# for row in mas:
#     for x in row:
#         print(x, end="\t\t")
#     print()

# w, h = 6, 6
# mas = [[r.randint(0, 10) for x in range(w)] for y in range(h)]
#
# for row in mas:
#     for x in row:
#         print(x, end="\t\t")
#     print()

from math import *

# num1 = sqrt(2)
# num2 = ceil(3.2)
# num3 = floor(3.8)
#
#
# print(num1)
# print(num2)
# print(num3)

# radius = 2
# print("Площадь окружности: ", round(pi * (radius ** 2), 2))

# num = -5.24
# print("Модуль числа:", fabs(num))
#
# a = -14
# b = -8
# c = 2
# print("Наибольший общий делитель a и b: ", gcd(a, b, c))

# lst = [1, 5, 3, 3.8]
# print(fsum(lst))
#
# print(fsum([0.3, 0.3, 0.3]))
# print(sum([0.3, 0.3, 0.3]))
# decimal

# перевод из радиан в градусы
# print(degrees(3.14159))
# print(cos(radians(60)))
# print(sin(radians(90)))
# print(tan(radians(0)))

# tip = int(input("Выбор фигуры:\n1 - треугольник\n2 - прямоугольник\n3 - круг\n: "))
# if tip == 1:
#     a = float(input("Введите сторону a = "))
#     b = float(input("Введите сторону b = "))
#     c = float(input("Введите сторону c = "))
#
# elif tip == 2:
#     a = float(input("Введите сторону a = "))
#     b = float(input("Введите сторону b = "))
#
# elif tip == 3:
#     r = float(input("Введите радиус r = "))
#
# else:
#     print("Некорректное значение")

# import time
# import locale
#
# locale.setlocale(locale.LC_ALL, "ru")
# seconds = time.time()
# print("Секунды с начала эпохи:", seconds)
# local_time = time.ctime(seconds)
# print("Местное время:", local_time)
# res = time.localtime(seconds)
# print("Localtime", res)
# print("Год: ", res[1])
# print(time.strftime("Today is %B %d, %Y"))
# # print(time.strftime("Today is %B %d, %Y", time.localtime(45441514)))
# print(time.strftime("%m/%d/%Y, %H:%M:%S"))

# pause = 0.5
# print("Program started...")
# time.sleep(pause)
# print(str(pause) + " seconds.")

# text = input("Название напоминания: ")
# tm = float(input("Через сколько минут: "))
# tm = tm * 60
# time.sleep(tm)
# print(text)

# start = time.time()
# time.sleep(5)
# finish = time.time()
# res = finish - start
# print(res)

# start = time.monotonic()
# time.sleep(1)
# finish = time.monotonic()
# res = finish - start
# print(res)


# print("Сегодня:", time.strftime("%B %d, %Y"))
# print(time.strftime("Сегодня: %B %d, %Y"))
# from decimal import Decimal
#
# n = Decimal("0.1")
# n = n * 2
# print(n)  # 0.3


# def hello(a, b):
#     print(a + b)
#
#
# x = 1
# y = 7
# hello(x, y)
# hello(2, 5)
# hello("abc", "def")
# hello(2.5, 4.3)

# def symbol(count, a, b):
#     print()
#
#
# symbol(9, "+", "-")
# symbol(7, "X", "0")


# def get_sum(a, b):
#     if a < b:
#         return b
#     return a
#
#
# x = 1
# y = 7
# res = get_sum(x, y)
# print(res)

# def diff_find(x, y):
#     return x - y if x > y else x + y
#
#
# num1 = int(input("Введите первое число: "))
# num2 = int(input("Введите второе число: "))
#
# print(f"a = {num1}\nb = {num2}\nРезультат: {diff_find(num1, num2)}")


# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34

# def change(lst):
#     # lst[0], lst[-1] = lst[-1], lst[0]
#     start = lst.pop()
#     end = lst.pop(0)
#     lst.append(end)
#     lst.insert(0, start)
#     return lst
#
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(["с", "л", "о", "н"]))

# def get_sum(a, b, c=0, d=3):
#     return a + b + c + d
#
#
# print(get_sum(1, 5, 2, 7))
# print(get_sum(1, 5, 2))
# print(get_sum(1, 5))
# print(get_sum(1, 5, c=5, d=2))

# def set_params(n=20, s='-'):
#     print(s * n)
#
#
# set_params(10, "+")
# set_params(5, "*")
# set_params(15, "#")
# set_params(7)
# set_params()

# def check_password(username, password, min_length=8, check_username=True):
#     if len(password) < min_length:
#         print("Пароль слишком короткий")
#     elif check_username and username in password:
#         print("Пароль содержит имя пользователя")
#     else:
#         print("Пароль пользователя", username, "прошел все проверки")
#
#
# check_password('igor', '12345')
# check_password('igor', '12345igor')
# check_password('igor', '12345name')
# check_password('igor', '12345igor', check_username=False)
#
# lt1 = [1, 2, 3]
# # lt1[0] = 0
# # print(lt1)
# print(id(lt1))
# lt1 += lt1 + [4, 5]
# print(id(lt1))
# lt1 = lt1[:]
# print(lt1)
# print(id(lt1))
# # lt2 = [1, 2, 3]
# print(id(lt1))
# lt1.append(4)
# print(lt1)
# print(id(lt1))
# lt1.pop(1)
# print(lt1)
# print(id(lt1))
# lt1[1] = "Hello"
# print(lt1)
# print(id(lt1[1]))
# print(id(lt2))
# print(lt1 == lt2)
# print(lt1 is lt2)

# a = "hello"
# print(id(a))  # 1473720751600
# a = a[1:-1]
# print(a)  # helloworld
# print(id(a))  # 1473720753968

# b = 5
# print(id(b))
# b += 1
# print(b)
# print(id(b))

# def add_number(n):
#     print("Внутри функции: ", n, "=", id(n))
#     n = n + [4]  # n += [4]
#     print("После присвоения: ", n, "=", id(n))
#     # return n
#
#
# x = [1, 2, 3]
# print(x, "=", id(x))
# add_number(x)
# print(x, "=", id(x))

# Кортежи (tuple)
# lst = [1, 2, 3]
# tp = (1, 2, 3)
# print(lst.__sizeof__())
# print(tp.__sizeof__())

# a = tuple((1, 2, 3, 4, 5))
# print(a)
# print(a[3])
# print(a[1:3])

# s = tuple(int(input("-> ")) for i in range(5))
# print(s)
# s = input("Введите по порядку без пробелов элементы кортежа: ")
# a = tuple(s)
# print(a)

import random as r

# mas =
# b = tuple(mas)
# print(tuple(r.randint(0, 100) for i in range(10)))

# print(tuple(2**i for i in range(1, 13)))

# t1 = tuple('hello')
# t2 = tuple(' world')
# t3 = t1 + t2
# print(t3)
# for i in t3:
#     if i == ' ':
#         continue
#     print(i*3, end=" ")

# def ran(a, b):
#     return tuple(r.randint(a, b) for _ in range(10))
#
#
# tup1 = ran(0, 5)
# tup2 = ran(-5, 0)
# tup3 = tup1 + tup2
# print(tup1)
# print(tup2)
# print(tup3, f'\nКоличество нулей: {tup3.count(0)}')

# t = (10, 11, [1, 2, 3], [4, 5, 6], ["hello", "world"])
# print(t, id(t))
# t[4][0] = "new"
# t[4].append('hi')
# t[2].append('hi')
# print(t, id(t))

# def rond1(lst):
#     lstnew = []
#     lstr = lst[::-1]
#     for i in lstr:
#         if i not in lstnew:
#             lstnew.append(i)
#
#     return tuple(lstnew)
#
#
# print(rond1([1, 2, 3, 3, 2]))

# def unique_tuple(x):
#     i = []
#     [i.append(item) for item in reversed(x) if item not in i]
#     return tuple(i)
#
#
# print(unique_tuple([1, 2, 3, 3, 2]))

# Упаковка кортежа
# t = 1, 2, 3
# print(t)

# Распаковка кортежа
# t = (1, 2, 3)
# # x = t[0]
# # y = t[1]
# # z = t[2]
# x, y, z = t
# print(x, y, z)

# def get_user():
#     name = "tom"
#     age = 25
#     is_marrid = False
#     return name, age, is_marrid
#
#
# user = get_user()
# # print(user[0])
# # print(user[1])
# # print(user[2])
# a, b, c = user
# print(user)
# print(a, b, c)

# del user
# print(user)

# lst = [1, 2, 3, 4, 5]
# print(type(lst))
# print(lst)
# tpl = tuple(lst)
# print(type(tpl))
# print(tpl)

# lst = (1, 2, 3, 4, 5)
# print(type(lst))
# print(lst)
# tpl = list(lst)
# print(type(tpl))
# print(tpl)

# countries = (
#     ("Германия", 80.2, (("Берлин", 3.326), ("Гамбург", 1.718))),
#     ("Франция", 66, (("Париж", 2.2), ("Марсель", 1.6)))
# )
#
# print(countries)
# for country in countries:
#     countryName, countryPopylation, cities = country
#     print("\nСтрана:", countryName, "население =", countryPopylation)
#     for city in cities:
#         cityName, cityPopulation = city
#         print("\tГород:", cityName, "население =", cityPopulation)

# Множества (set)
# s = {"banana", "apple", "orange", "banana", "apple"}
# print(type(s))
# print(s)
# print(len(s))
#
# a = set("hello")
# print(a)
#
# c = {1, 52, 3, 74, 52, 3}
# col = set(c)
# print(col)

# print(list({i for i in c if i % 2 == 0}))
# for i in c:
#     print(i, end=" ")
#  res (if else) (for in) (if)

# r = ['ab_1', 'ac_2', 'bc_1', 'bc_2']
# a = {'A' + i[1:] if i[0] == 'a' else "B" + i[1:] for i in r if i[1] == 'c'}
# print(a)

# a = {"Tom", "Bob", "Alice", "Anna"}
# a.add(4)  # добавление элемента
# print(a)
# a.remove("Tom")  # удаление элемента (с генерацией исключения)
# print(a)
# user = 4
# if user in a:
#     a.remove(user)
# print(a)
# a.discard("Ann")  # удаление элемента (без генерацией исключения)
# print(a)
# a.pop()  # удаление первого элемента
# print(a)
# a.clear()  # полная очистка
# print(a)

# a = {0, 1, 2, 3}
# b = {4, 3, 2, 1}
# print("a =", a)
# print("b =", b)
# # c = a.union(b)
# c = a | b
# print(c)
# # a.update(b)
# a |= b
# print(a)
# c = a.intersection(b)
# c = a & b
# print(c)
# a &= b
# print(a)

# c = a.copy()
# c.add(5)
# print(c)
# print(a)
#
# a ^= b
# print(a)

# a = {0, 1, 2, 3, 4}
# b = {3, 2, 1}
# print("a =", a)
# print("b =", b)
# print(a >= b)

# draw = {'Marina', 'Jenya', "Sveta"}
# music = {'Kostya', 'Jenya', 'Ilya'}
# one = draw ^ music
# print(one)
# two = draw & music
# print(two)
# print(draw - two)

# s = frozenset([1, 2, 3, 4, 5, 6])
# print(s)
#
# a = frozenset({"hello", "world"})
# print(a)

# fs = frozenset({i**2 % 4 for i in range(10)})
# print(fs)
#
# r = set('ACDB')
# b = {frozenset({i + j for j in r.difference(i)}) for i in r}
# print(b)

# Словари  {} dict
# s = [1, 2, 3]
# print(dict(s))
# print(s[1])
# d = {'one': 1, 'two': 2, 'three': 3}
# print(d['two'])

# d = {}
# d = dict()
# print(d)
# print(type(d))

# d = dict.fromkeys(['a', 'b'])
# print(d)

# user = (
#     ('igor@gmail.com', 'Igor'),
#     ('irina@gmail.com', 'Irina'),
#     ('anna@gmail.com', 'Anna')
# )
#
# print(user)
# print(dict(user))

# d = {a: a ** 2 for a in range(1, 7)}
# print(d)
# d[2] = 15
# print(d)
# d[9] = 4**2
# print(d)

# d = {0: "text1", "one": 45, (1, 2.3): "кортеж", "42": [7, 1, 2, 3], True: 1}
# print(d["one1"])
# del d["one1"]
# try:
#     del d["one"]
# except KeyError:
#     print("Элемент в словаре отсутствует")
#
# print(d)

# if 'one' in d:
#     print("TRUE")

# if 'one' in d.keys():
#     print("TRUE")

# d = {'one': 1, 'two': 2, 'three': 3}
# for key in d:
#     print(key, d[key])

# d = {i: input("-> ") for i in range(1, 5)}
# # d = dict()
# # d[1] = input('-> ')
# # d[2] = input('-> ')
# # d[3] = input('-> ')
# # d[4] = input('-> ')
# print(d)
# dislike = int(input("Какой элемент исключить: "))
# del d[dislike]
# print(d)


# d = {'one': 1, 'two': 2, 'three': 3}
# print(len(d))

# capitals = dict()
# capitals['Россия'] = 'Москва'
# capitals['Италия'] = 'Рим'
# capitals['Испания'] = 'Мадрид'
#
# countries = ["Россия", "Италия", "Франция", "Испания"]
# for country in countries:
#     if country in capitals:
#         print("Столица страны " + country + ": " + capitals[country])
#     else:
#         print("В базе нет страны с названием " + country)


# goods = {"1": ['Core-i3-4330', 9, 4500],
#          "2": ['Core-i5-4670K', 3, 8500],
#          "3": ['AMD FX-6300', 6, 3700],
#          "4": ['Pentium G3220', 8, 2100],
#          "5": ['Core-i3-4350', 5, 6400]}
#
# for i in goods:
#     print(i, ") ", goods[i][0], " - ", goods[i][1], " шт. по ", goods[i][2], "руб", sep="")
#
# while True:
#     n = input('№: ')
#     if n != "0":
#         k = input('Количество: ')
#         goods[n][1] = k
#     else:
#         break
#
# for i in goods:
#     print(i, ") ", goods[i][0], " - ", goods[i][1], " шт. по ", goods[i][2], "руб", sep="")

# d = {'A': 1, 'B': 2, 'C': 3}
# x = iter(d)
# print(list(x))
# # d.clear()  # удаляет все элементы из словаря
# d2 = d.copy()  # создается копия словаря
# print("D =", d)
# print("D2 =", d2)
# d2["B"] = 5
# d["E"] = 7
# print("D =", d)
# print("D2 =", d2)

# value = d.get("A1", "False")  # значение по заданному ключу
# print(value)
# # print(d["Z"])
# print("D =", d)
# new = d.items()  # формируется список пар ключей и значений
# print(new)
#
# new1 = dict.items(d)
# print(new1)
#
# a = d.keys()
# print(a)
#
# iter = d.pop("F", None)  # удаление элемента по заданному ключу
# print(iter)
# print(d)

# iter = d.popitem()  # удаляет и возвращает произвольную пару ключа и значения
# print(iter)
# print(d)

# n = d.setdefault("C", 5)  # устанавливает значение по умолчанию
# print(n)
# print(d)

# d.update([('R', 7), ('Q', 9)])  # обновление словаря
# print(d)
# d.update([('A', 20), ('B', 40)])
# print(d)
# print("Даны два словаря: x = {'a': 1, 'b': 2} и y = {'b': 3, 'c': 4}. Объединить их в третий словарь.\n")
# x = {'a': 1, 'b': 2}
# y = {'b': 3, 'c': 4}
# z = x.copy()
# z.update(y)
# print(z)

# v = d.values()
# print(list(v))

# d = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
#
# d1 = dict()
# d1['name'] = d.pop('name')
# d1['salary'] = d.pop('salary')
# print(d)
# print(d1)

# d = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
#
# print(d)
# s = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
# s['location'] = s.pop('city')
# print(s)
#
# a = {
#     "First": {
#         1: 'one',
#         2: 'two',
#         3: 'three'
#     },
#     "Second": {
#         4: 'four',
#         5: 'five'
#     }
# }
# print(a)
# for x in a:
#     print(x)
#     for y in a[x]:
#         print('\t', y, ': ', a[x][y], sep="")


# sales = {
#     "John": {"N": 3056, "S": 8463, "E": 8441, "W": 2694},
#     "Tom": {"N": 4832, "S": 6786, "E": 4737, "W": 3612},
#     "Anne": {"N": 5239, "S": 2802, "E": 5820, "W": 1859},
#     "Fiona": {"N": 3904, "S": 3645, "E": 8821, "W": 2451}
# }
#
# for x in sales:
#     print(x)
#     for y in sales[x]:
#         print('\t', y, ': ', sales[x][y], sep="")
#
# name = input("name ")
# region = input("code region ")
# print(sales[name][region])
# num = int(input("numbers "))
#
# sales[name][region] = num
# print(sales[name])

# d = {'A': 1, 'B': 2, 'C': 7, 'D': 4, 'C': 3}
# d1 = {key: value for key, value in d.items()}
# print(d1)
# b = [10, 20, 30, 40]
# b = "Hello"
# a = {i: i*2 for i in b}
# print(a)

# value = int(input('-> '))
# lst = [1, 2, 3, 4]
# d = {k: value for k in lst}
# print(d)

# shapes = {1: 'Rectangle', 2: 'Triangle', 3: 'Circle'}
#
# values = list(shapes.values())
# print(values)
# keys = list(shapes.keys())
# print(keys)
# pairs = list(shapes.items())
# print(pairs)

# a = ['one', 1, 2, 3, 'two', 10, 20, 'three', 15, 36, 60, 'four', -20]
#
# d = dict()
# s = None
#
# for i in a:
#     if type(i) == str:
#         s = i
#         d[i] = []
#     else:
#         d[s].append(i)
# print(d)

# zip()
# d = dict(zip([1, 2, 3], ['a', 'b', 'c']))
# # print(d)
#
# a = ['a', 'b', 'c']
# b = [1, 2, 3, 4]
# c = [4.0, 5.0, 6.0]
# # print({k: v for (k, v) in zip(a, b)})
# print(list(zip(a, b, c)))

# print(list(zip(range(5), range(100))))
# one = {'name': 'Igor', 'last_name': 'Dou', 'job': 'Consultant'}
# two = {'name': 'Irina', 'last_name': 'Smith', 'job': 'Manager'}
#
# for (k1, v1), (k2, v2) in zip(one.items(), two.items()):
#     print(k1, '->', v1)
#     print(k2, '->', v2)

# pairs = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
# a, b = zip(*pairs)
# print(a)
# print(b)
# num = [2, 4, 1, 3]
# letters = ['b', 'a', 'd', 'c']
# data = list(zip(letters, num))
# print(data)
# data.sort()
# print(data)
# data1 = list(zip(num, letters))
# print(data1)
# data1.sort()
# print(data1)

# month = ["January", 'February', 'Match']
# total_sales = [52000.00, 51000.00, 48000.00]
# prod_cost = [46800.00, 45900.00, 43200.00]
# for sales, costs, m in zip(total_sales, prod_cost, month):
#     profit = sales - costs
#     print("Общая прибыль в", m, "=", profit)

# one = {'apple': 0.40, 'orange': 0.35, 'pepper': 0.25}
# two = {'pepper': 0.20, 'onion': 0.35}
# print({**one, **two})
# for k, v in {**one, **two}.items():
#     print(k, "->", v)

# data = [2, 5, 3, 4, 1, 5]
# num = 1
# for val in data:
#     print(num, "->", val)
#     num += 1

# data = [2, 5, 3, 4, 1, 5]
#
# for num, val in enumerate(data, 15):
#     print(num, "->", val)

# d = {1: {'a': 55, 'b': 74, 'c': 45, 'd': 77},
#      2: {'a': 155, 'b': 174, 'c': 145, 'd': 177}}
#
# for i, j in enumerate(d):
#     print(i, ": ", j, "=", d[j], sep='')

# num = [2, 5, 3, 4, 1, 5]
# itr = iter(num)
# print(itr)
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr, "STOP"))

# num = [2, 5, 3, 4, 1, 5]
# b = enumerate(num)
# c = next(b)
# print(c)
# print(type(c))
# print(next(b))

# a = [1, 2, 3]
# print(*a)
# b = [*a, 4, 5, 6]
# print(b)

# def func(*args):
#     # res = 0
#     # for n in args:
#     #     res += n
#     # return res
#     return sum(args)
#
#
# print(func(1, 2))
# # print(func("xyz", "abc"))
# print(func(1, 2, 3, 4))
# print(func())
# def to_dict(*args):
#     return {i: i for i in args}
# # def to_dict(*argm):
# #     d = {}
# #     for i in argm:
# #         d[i] = i
# #     return d
#
#
# print(to_dict(1, 2, 3, 4))
# print(to_dict('grey', (2, 17), 3.11, -4))

# def func(a, *args):
#     return a, args
#
#
# print(func(1))
# print(func(1, 2, 3, 4, "abc"))

# def func(student, *scores):
#     print("Student name:", student)
#     for i in scores:
#         print(i, end=" ")
#     print()
#
#
# func("Ирина", 36, 68, 100, 97, 66)
# func("Борис", 100, 97, 64, 57)
# def reverse_num(n):
#     s = str(n)
#     return int(s[::-1])
#
#
# def func(*args, only_odd=False):
#     res = []
#     for i in args:
#         if not only_odd or (only_odd and i % 2 != 0):
#             res.append(reverse_num(i))
#     return res
#
#
# print(func(12, 2345, 323, 4456, 5687, 62, 734, 81, 91))
# print(func(12, 2345, 323, 4456, 5687, 62, 734, 81, 91, only_odd=True))

# def func(**kwargs):
#     return kwargs
#
#
# print(func(a=1, b=2, c=3))
# print(func())
# print(func(a="Python"))

# def info(**data):
#     for key, values in data.items():
#         print(key, "is", values)
#     print()
#
#
# info(firstname="Irina", lastname="Sharma", age=22, phone="1234567845")
# info(firstname="Igor", lastname="Wood", email="igor@mail.ru", age=25, country="Russia", phone="7894567844")

# def print_pet_names(owner, *args, name=True, **pets):
#     return owner, args, name, pets
#
#
# print(print_pet_names("Jonatan"))

# def func1(*args):
#     print(args[0])
#
#
# def func2(**kwargs):
#     print(kwargs['one'])
#
#
# func1(1, 2, 3, 4, 5)
# func2(one=123, two=456)

# x = {'a': 1, 'b': 2}
# y = {'b': 3, "c": 4}
# z = {**x, 'one': 1, 'two': 2, **y}
# print(z)

# name = "Tom"
#
#
# def hi():
#     global name
#     name = "Sam"
#     print("Hello,", name)
#
#
# def bye():
#     print("Good bue,", name)
#
#
# hi()
# print(name)
# bye()
# i = 6
#
#
# def func(arg=i):
#     print(arg)
#
#
# i = 5
#
# func()
# z = 12
#
#
# def add(a):
#     x = 2
#
#     def add_some():
#         print("x =", x)
#         print("z =", z)
#         # w = 9
#
#         return a + x
#
#
#     return add_some()
#
#
# print(add(3))
# # print(add(4))


# import builtins
#
# names = dir(builtins)
#
# for t in names:
#     print(t)

# def outer_func(who):
#     def inner_func():
#         print("Hello,", who)
#
#     inner_func()
#
#
# outer_func("World!")

# def fun1():
#     a = 6
#
#     def fun2(b):
#         a = 4
#         print("Сумма внутренней функции:", a + b)  # 4 + 5
#
#     print("Значение переменной a:", a)
#     fun2(5)
#
#
# fun1()

# x = 25
#
#
# def fn():
#     global t
#     a = 30
#
#     print("global x:", x)
#
#     def inner():
#         nonlocal a
#         a = 35
#         print("nonlocal:", a)
#
#     inner()
#     print(a)
#     t = a
#
#
# fn()
# z = x + t
# print(z)

# def fn1():
#     x1 = 25
#
#     def fn2():
#         x1 = 33
#
#         def fn3():
#             nonlocal x1
#             x1 = 55
#             print('fn3.x1 =', x1)
#
#         fn3()
#         print('fn2.x1 =', x1)
#
#     fn2()
#     print('fn1.x1 =', x1)
#
#
# fn1()

# def outer(a1, b1, a2, b2):
#     a = 0
#     b = 0
#
#     def inner():
#         nonlocal a, b
#         a = a1 + a2
#         b = b1 + b2
#
#     inner()
#     return [a, b]
#
#
# print(outer(2, 3, -1, 4))


# def func1():
#     a = 1
#     b = 'line'
#     c = [1, 2, 3]
#
#     def func2():
#         nonlocal b
#         c.append(4)
#         a = 2
#         b = b + 'new'
#         print(a, b, c)
#
#     func2()
#
#
# func1()

# локальная переменная
# def rect_paral_square(a, b, c):
#     def rect_square(i, j):
#         return i * j
#
#     s = 2 * (rect_square(a, b) + rect_square(a, c) + rect_square(c, b))
#     return s
#
#
# print(rect_paral_square(2, 4, 6))
# print(rect_paral_square(5, 8, 2))
# print(rect_paral_square(1, 6, 8))

# глобальная переменная
# s = 0
#
#
# def rect_paral_square(a, b, c):
#     def rect_square(i, j):
#         return i * j
#
#     global s
#     s = 2 * (rect_square(a, b) + rect_square(a, c) + rect_square(c, b))
#     return s
#
#
# print(rect_paral_square(2, 4, 6))
# print(s)
# print(rect_paral_square(5, 8, 2))
# print(s)
# print(rect_paral_square(1, 6, 8))
# print(s)

# нелокальная переменная
# def rect_paral_square(a, b, c):
#     s = 0
#
#     def rect_square(i, j):
#         nonlocal s
#         s += i * j
#
#     rect_square(a, b)
#     rect_square(a, c)
#     rect_square(c, b)
#     return 2 * s
#
#
# print(rect_paral_square(2, 4, 6))
# print(rect_paral_square(5, 8, 2))
# print(rect_paral_square(1, 6, 8))


# def outer(n):
#     def inner(x):
#         return n + x
#
#     return inner
#
#
# add1 = outer(2)
# print(add1(4))
#
# add2 = outer(6)
# print(add2(2))
#
# one = outer(5)(10)
# print(one)

# def func(city):
#     s = 0
#
#     def inner():
#         nonlocal s
#         s += 1
#         print(city, s)
#
#     return inner
#
#
# res1 = func('Москва')
# res1()
# res1()
#
# res2 = func('Сочи')
# res2()
# res2()
#
# res1()

# ====================
# students = {
#     'Alice': 98,
#     'Bob': 67,
#     'Chris': 85,
#     'David': 75,
#     'Ella': 54,
#     'Fiona': 35,
#     'Grace': 69
# }
#
#
# def make_class(lower, upper):
#     def wrap(exam):
#         return {k: v for (k, v) in exam.items() if lower <= v <= upper}
#
#     return wrap
#
#
# a = make_class(80, 100)
# b = make_class(70, 80)
# c = make_class(50, 70)
# d = make_class(0, 50)
# print(a(students))
# print(b(students))
# print(c(students))
# print(d(students))


# def func_object(a, b):
#     def add():
#         return a + b
#
#     def sub():
#         return a - b
#
#     def mul():
#         return a * b
#
#     def replace():
#         pass
#
#     replace.add = add
#     replace.sub = sub
#     replace.mul = mul
#     return replace
#
#
# obj1 = func_object(5, 2)
# print(obj1.add())
# obj2 = func_object(5, 2)
# print(obj2.sub())
# obj3 = func_object(5, 2)
# print(obj3.mul())


# lambda

# print((lambda x, y: x + y)(1, 2))
# print((lambda x, y: x + y)("a", "b"))
#
# func = lambda x, y: x + y
# print(func(1, 2))
# print(func("a", "b"))

# sum1 = lambda a=1, b=2, c=3: a + b + c
#
# print(sum1())
# print(sum1(10))
# print(sum1(10, 20))
# print(sum1(10, 20, 30))

# func = lambda *args: args
# print(func(1, 2, 3, 4, 5, 6, 4, 5, 6, 7, 8, 98, 7))

# c = (lambda x: x * 2,
#      lambda x: x * 3,
#      lambda x: x * 4)
#
# for t in c:
#     print(t("abc "))

# def inc(n):
#     return lambda x: x + n

# inc = lambda n: lambda x: x + n
# f = inc(42)
# print(f(1))
# print(f(5))

# print((lambda n: lambda x: x + n)(42)(1))
#
# print((lambda n: lambda x: lambda y: x + n + y)(2)(4)(6))

# d = {'c': 24, 'a': 100, 'b': 15}
# lst = list(d.items())
# print(lst)
# lst.sort(key=lambda i: i[1])
# print(lst)
# players = [
#     {'name': 'Антон', 'last name': 'Бирюков', 'raiting': 9},
#     {'name': 'Алексей', 'last name': 'Бодня', 'raiting': 10},
#     {'name': 'Федор', 'last name': 'Сидоров', 'raiting': 4},
#     {'name': 'Михаил', 'last name': 'Семенов', 'raiting': 6}
# ]
# print(sorted(players, key=lambda item: item['last name']))
# print(sorted(players, key=lambda item: item['raiting'], reverse=True))
# print(sorted(players, key=lambda item: item['raiting']))
# # print(players.sort(key=lambda item: item['raiting']))
# print(players)

# a = [(lambda x, y: x + y), (lambda x, y: x - y), (lambda x, y: x * y), (lambda x, y: x / y)]
# print(a[0](12, 6))

# a = {"one": lambda x: x - 1, 'two': lambda x: abs(x) - 1, 'three': lambda x: x}
# b = [-3, 10, 0, 2]
# for i in b:
#     if i < 0:
#         print(a['two'](i))
#     elif i > 0:
#         print(a['one'](i))
#     else:
#         print(a['three'](i))

# d = {
#     1: lambda: print('Monday'),
#     2: lambda: print('Tuesday'),
#     3: lambda: print('Wednesday'),
#     4: lambda: print('Thursday'),
# }
# d[2]()
# import math
# area = {
#     'Circle': lambda r: print('Площадь окружности радиуса', r, math.pi * r ** 2),
#     'Rectangle': lambda a, b: print('Площадь прямоугольника размером ', a * b),
#     'Trapezoid': lambda a, b, h: print('Площадь трапеции', (a + b) / 2 * h)
# }
#
# area["Circle"](2)
# area["Rectangle"](10, 13)
# area["Trapezoid"](7, 5, 3)

# maximum = lambda a, b: a if a > b else b
# print(maximum(15, 23))
#
# print((lambda x, y, z: x if x < y and x < z else y if y < x and y < z else z)(10, 5, 15))

# def mul(t):
#     return t * 2
#
#
# lst = [2, 8, 12, -5, -10]
# print(list(map(mul, lst)))
# print(list(map(lambda t: t * 2, "hello")))

# t = (2.88, -1.75, 100.55)
# print(tuple(map(lambda x: int(x), t)))
#
# s = ['1', '2', '3', '4', '5']
# print(list(map(int, s)))
#
# areas = [3.56457, 5.457895, 9.456789, 7.6578945, 8.456789, 2.4789545]
# print(list(map(round, areas, range(1, 4))))
#
# # print(round(45.789456, 2))
# for i in range(1, 7, 2):
#     print(i, end=" ")

# st = "hello"
# num = [1, 2, 3, 4, 5]
# print(dict(map(lambda x, y: (y,  x), st, num)))

# t = ('abcd', 'abc', 'cdefg', 'def', 'ghi')
# print(tuple(filter(lambda s: len(s) == 3, t)))
#
# b = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
# res = list(filter(lambda s: s > 75, b))
# print(res)

# from random import randint

# lst = [randint(1, 40) for i in range(10)]
# print(lst)
# res = list(filter(lambda s: 10 <= s <= 20, lst))
# print(res)

# m = list(map(lambda x: x ** 2, filter(lambda x: x % 2 != 0, range(10))))
# print(m)
# m1 = [x ** 2 for x in range(10) if x % 2 != 0]
# print(m1)

# Декораторы
# def hello():
#     return "Hello, I am func 'hello'"
#
#
# def super_func(func):
#     print("Hello, I am func 'super_func'")
#     print(func())
#
#
# super_func(hello)

# def hello():
#     return "Hello, I am func 'hello'"
#
#
# test = hello
# print(test())

# def my_decorator(func):  # декорирующая функция
#     def wrap(*args):
#         print('Code before')
#         res = func(*args)
#         print('Code  after')
#         return res
#
#     return wrap
#
#
# @my_decorator   # декоратор
# def func_test(a, b):  # декорируемая функция
#     return a + b
#
#
# @my_decorator
# def func_test1(a, b, c):
#     return a + b + c
#
#
# print(func_test(2, 5))
# print(func_test1(2, 5, 3))
# test = my_decorator(func_test)
# test()
# def bold(fn):
#     def wrap():
#         return "<b>" + fn() + "</b>"
#
#     return wrap
#
#
# def italic(fn):
#     def wrap():
#         return "<i>" + fn() + "</i>"
#
#     return wrap
#
#
# @italic
# @bold
# def hello():
#     return "text"
#
#
# print(hello())
# count = 0

# def cnt(fn):
#     count = 0
#     def wrap():
#         # global count
#         nonlocal count
#         count += 1
#         fn()
#         print("Вызов функции: ", count)
#
#     return wrap
#
#
# @cnt
# def hello():
#     print("Hello")
#
#
# hello()
# hello()
# hello()
# def args_decorator(arg1, arg2):
#     print("Аргументы декоратора", arg1, arg2)
#
#     def my_decorator(fn):
#         print("Аргументы декоратора во вложенной функции", arg1, arg2)
#
#         def wrap(func_arg1, func_arg2):
#             fn(arg1, arg2)
#             return fn(func_arg1, func_arg2)
#
#         return wrap
#
#     return my_decorator
#
#
# @args_decorator("Игорь", "Нефедов")
# def print_full_data(first, second):
#     print(first, second)
#
#
# print_full_data("Ирина", "Владимировна")

# def typed(*args, **kwargs):
#     def wrapper(fn):
#         def wrap(*f_args, **f_kwargs):
#             print("args, kwargs", args, kwargs)
#             print("f_args, f_kwargs", f_args, f_kwargs)
#             for i in range(len(args)):
#                 if type(f_args[i]) != args[i]:
#                     raise TypeError("Тип данных не соответствует")
#
#             for i in kwargs:
#                 if type(f_kwargs[i]) != kwargs[i]:
#                     raise TypeError("Тип данных не соответствует")
#
#             return fn(*f_args, **f_kwargs)
#
#         return wrap
#
#     return wrapper
#
#
# @typed(int, int, int)
# def typed_fn(x, y, z):
#     return x * y * z
#
#
# @typed(str, str, str)
# def typed_fn2(x, y, z):
#     return x + y + z
#
#
# @typed(str, str, z=int)
# def typed_fn3(x, y, z=10):
#     return (x + y) * z
#
#
# print(typed_fn(3, 4, 5))
# # # print(typed_fn(3, 4, "Hello"))
# # print(typed_fn2("Hello, ", "World", "!"))
# print(typed_fn3("Hello, ", "World ==  ", z=5))
# print(typed_fn3("Hello, ", "World ==  ", z=2))
# def args_decorator(tx=None, decorator_text=""):
#     def my_decorator(func):
#         def wrap(*args):
#             print(decorator_text, end="")
#             func(*args)
#
#         return wrap
#     if tx is None:
#         return my_decorator
#     else:
#         return my_decorator(tx)
#
#
#
# @args_decorator
# def hello_world(text):
#     print(text)
#
#
# @args_decorator(decorator_text="Hello, ")
# def hello_world2(text):
#     print(text)
#
#
# hello_world('Hi!')
# hello_world2('world!')

# color: #00FF00  #0F0
# color: rgb(0,255,0)

# print(int('19'))
# # print(int('19.5'))
# print(int(19.5))

# print(int("100", 2))
# print(int("100", 8))
# print(int("100", 10))
# print(int("100", 16))

# print(bin(18))  # двоичное  0b
# print(oct(18))  # восьмиричное  0o
# print(hex(18))  # шеснадцатеричное  0x
#
# print(0b1010)
# print(0o12)
# print(0xFF)

# q = "Pyt"
# w = 'hon'
# e = q + w
# print(e)
# print(e * 3)
# # print("-3: ", e * -3)
#
# print(e in 'I am learn Python')
# print(e in 'I am learn Java')

# s = "Hello"
# print(s[slice(2, 5)])
# print(s[slice(5, None, -1)])
# print(s[slice(None, None, 2)])  # s[::2]

# s = "python"
# print(s[3])
# # s[3] = 't'
# print(id(s))
# s = s[:3] + 't' + s[4:]
# print(id(s))
# print(s)

# def changeCharToStr(s, c_old, c_new):
#     s2 = ""
#     i = 0
#
#     while i < len(s):
#         if s[i] == c_old:
#             s2 += c_new
#         else:
#             s2 += s[i]
#         i += 1
#
#     return s2
#
#
# str1 = "Я изучаю Nuthon. Мне нравится Nuthon. Nuthon очень интересный язык программирования."
# print(changeCharToStr(str1, "N", "P"))


# def change_text(s, c_old, c_new):
#     #   return s.replace(c_old, c_new)
#     s2 = ""
#     for i in s:
#         if i == c_old:
#             s2 += c_new
#         else:
#             s2 += i
#     return s2
#
#
# str1 = "я изучаю Nython, мне Nython нравится"
# print(change_text(str1, "N", "P"))


# print(u"Hello")
# print('I\'m learning Python')
# print('C:\\file.txt\\')
# print(r'C:\file.txt\\'[:-1])
# print(r'C:\file.txt' + "\\")
# name = "Дмитрий"
# age = 25
# print(f"Меня зовут {name}. Мне {age} лет.")
# print("Меня зовут " + name + ". Мне " + str(age) + " лет.")

# import math
#
# print(f"Значение числа pi: {math.pi:.2f}")
# print(f"13 / 3 = {round(13 / 3, 2)}")
# print(f"13 / 3 = {13 / 3:.2f}")
# x = 15
# y = 5
# print(f"{x} x {y} / 2 = {x * y / 2}")

# name = "друг"
# prof = "программист"
# lang = "Python"
#
# message = (
#     f"Привет, {name}. "
#     f"Ты {prof}. "
#     f"На языке {lang}."
# )
#
# print(message)

# print(f'Словарь: {{key = 22}}')
# a = 7 + 4
# print(f"{{a}}")

# dir_name = "my_doc"
# file_name = "data.txt"
# print(fr'home\{dir_name}\{file_name}')

# '''<div><a href='#'>content</a></div>'''
# s = """<div>
#     <a href='#'>content</a>
# </div>"""
# print(s)

# def square(n):
#     """Принимает число n, возвращает квадрат числа n"""
#     return n ** 2
#
#
# print(square(5))
# print(square.__doc__)
# import math
#
#
# def cylinder(r, h):
#     """
#     Вычисляет площадь цилиндра.
#
#     Вычисляет площадь цилиндра на основании заданной высоты и радиуса основания
#     :param r: положительное число, радиус основания цилиндра
#     :param h: положительное число, высота цилиндра
#     :return: положительное число, площадь цилиндра
#     """
#     return 2 * math.pi * r * (r + h)
#
#
# print(cylinder(2, 4))
# print(cylinder.__doc__)

# print(ord("a"))
# print(ord("#"))
# print(ord("г"))
#
# while 1:
#     n = input("-> ")
#     if n != "-1":
#         print(ord(n))
#     else:
#         break

# mystr = "Test string for me"
# arr = [ord(x) for x in mystr]
# print("ASCII коды:", arr)
# arr = [int(sum(arr) / len(arr))] + arr
# print("Среднее арифметическое:", arr)
# arr += [x for x in [ord(x) for x in (input("-> ") + " ")[:3]] if x not in arr]
# print(arr)
# if arr[-1] in arr[:-1]:
#     print("Количество последних элементов:", arr.count(arr[-1]) - 1)
# arr.sort(reverse=True)
# print(arr)

# print(chr(97))
# print(chr(35))
# a, b = 97, 122
# # print(*(chr(x) for x in range(b, a + 1)))
# print(*(chr(x) for x in range(a, b + 1)) if a < b else (chr(x) for x in range(b, a + 1)))
# if a > b:
#     for i in range(b, a + 1):
#         print(chr(i), end=" ")
# else:
#     for i in range(a, b + 1):
#         print(chr(i), end=" ")
# print("apple" == "Apple")
# print("apple" > "Apple")
# print(ord("A"))
# print(ord("a"))

# s = "hello, WORLD! I am learning Python."
# print(s.capitalize())  # Hello, world! i am learning python.
# print(s.lower())  # hello, world! i am learning python.
# print(s.upper())  # HELLO, WORLD! I AM LEARNING PYTHON.
# print(s.swapcase())  # HELLO, world! i AM LEARNING pYTHON.
# print(s.title())  # Hello, World! I Am Learning Python.
# print(len(s))
# print(s.count("h", 0, -4))
# print(s.find("Python", 0, 30))  # -1 - не найдено
# # print(s.index("Python", 0, 30))  # ValueError
# print(s.rfind("l", 3, 19))
# print(s.rindex("l"))
# print(s.endswith("on."))
# print(s.endswith("lo", 3, 5))
# print(s.startswith("hello", 14))

# print('abc123'.isalnum())
# print('abc&123'.isalnum())
# print('abc'.isalnum())
# print("ACBabc".isalpha())
# print("ACB123".isalpha())
# print("ACB123".isdigit())
# print("123".isdigit())
#
# print('for'.isidentifier())
#
# print('abc&D'.islower())
#
# print(' \t \n '.isspace())
#
# print('This'.istitle())
# print('thiS'.istitle())
# print('THIS123%'.isupper())
# ab&c = 20
# s1 = "один два"
# s1 = 'ab12c59p7dq0'
# digits = []
# for symbol in s1:
#     if '0123456789'.find(symbol) != -1:
#         digits.append(int(symbol))
# print(digits)

# s = "ab12c59p7dq"
# digits = []
# for i in s:
#     if i in "0123456789":
#         digits.append(int(i))
#
# print(digits)

# s1 = "ab12c59p7dq"
# digits = []
#
# for i in s1:
#     try:
#         digits.append(int(i))
#     except ValueError:
#         pass
# print(digits)

# s1 = "Дана ст(рока символов, среди которых есть одна открыв)ающаяся"
# # ind1 = s1.index('(')
# # ind2 = s1.index(')')
# print(s1[s1.index('(')+1:s1.index(')')])

# s1 = "Send unlimited free text and make WiFi calls from a free phone number."
# s1 = s1[:s1.find("f")] + s1[s1.rfind("f")+1:]
# print(s1)
# if s1.count("f") == 1:
#     print(s1.find('f'))
# elif s1.count("f") >= 2:
#     print(s1.find('f'), s1.rfind('f'))

# a = "Send unlimited free texts and make WiFi calls from a free phone number."
# print(a.rfind("f"))
# f = "f"
# if f in a:
#     if a.find(f) != a.rfind(f):
#         print(a.find(f), a.rfind(f))
#     else:
#         print(a.find(f))
# else:
#     pass

# print('py'.center(10, "-"))
# print('py'.center(1))

# print('     py'.lstrip())
# print('     py      '.rstrip())
# print('https://www.python.org/'.lstrip('/:pthsw').rstrip("/.org"))
# print('     py      '.strip())
# print('https://www.python.org/'.strip('/:pthsw.org'))

# s = "-"
# seq = ('a', 'b', 'c')
# print(s.join(seq))
#
# print("..".join(['1', '2']))
# print(":".join("Hello"))
#
# print("Строка разделенная пробелами".rsplit())
# print('www.python.org.www.python.org'.rsplit(".", 3))
# #
# # a = input("-> ").split("/")
# # print(a)
# a = input("введите строку")
# inic = a.split()
# inic2 = "*".join(inic)
# print(inic2)

import re

# s = "Я ищу [сов-паден-ия] в 20-26. И я их найду в 200000 7894 9684 9568_3654 счёта. Python"
# reg = r'20*'
# print(re.findall(reg, s))
#
# d = "Цифры: 7б +17, -42, 0013, 0.1"
# print(re.findall(r'[+-]?\d+', d))

# + {1, }
# * {0, }
# ? {0, 1}

# s = "05-03-1987 # Дата рождения"
# print("Дата рождения: ", re.sub(r'#.*', '', s))
# print(re.sub(r'-', '.', s))
# print("Дата рождения: ", re.sub(r'-', ".", re.sub(r"#.*", "", s)))
# 05.03.1987 # Дата рождения"
# [0-3]
# [0-9А-Яа-яa-z_]
# w = "Еда, беду, победа"
# pattern = "[Ее]д[ау]"
# print(re.findall(pattern, w))

# print(re.search(reg, s))
# print(re.search(reg, s).span())
# print(re.search(reg, s).start())
# print(re.search(reg, s).end())
# print(re.search(reg, s).group())
# print(re.match(reg, s))
# print(re.split(reg, s, 1))
# print(re.sub(reg, "!", s, 1))

# srting = "Час в 24-часовом формате от 00 до 23. 2021-06-15T21:55. Минуты, в диапазоне от 00 до 59. 2021-06-15Е01:09"
#
#
# # s = "Я ищу совпадения в 2021. И я их найду в 2 счета 16:24, 25:71"
# req = r"[0-2][0-9]:[0-5][0-9]"
# print(re.findall(req, srting))

# s = "author=Пушкин A.C.; title =     Евгений Онегин; price  =200; year= 1931"
# reg = r'\w+\s*=\s*[^;]+'
# print(re.findall(reg, s))

# s1 = "27 ноября 2021 года 456454646"
# reg1 = r'\d{2,5}'
# print(re.findall(reg1, s1))

# s = "МИ Д - Министерство иностранных дел, ГЭС - гидроэлектростанция, ФСБ - Федеральная служба безопасности"
# reg = r"""
#       [А-ЯЁ]  # поиск букв
#       {2,}
#       \s*
#       [А-ЯЁ]*
#       """
# print(re.findall(reg, s))  # []
# print(re.findall(reg, s, re.VERBOSE))  # ['МИ Д', 'ГЭС ', 'ФСБ ']

# s = "Я ищу совпадения в 2021. И я их найду в 2 счета."
# reg = r"^\w+\s\w+"
# reg = r"\w+\.$"
# print(re.findall(reg, s))

# print(re.findall(r'\w+', '12 + й'))
# print(re.findall(r'\w+', '12 + й + r', flags=re.ASCII))
#
# text = 'h+ello world'
# print(re.findall(r'\w+', text, flags=re.DEBUG))
# print()
# print(re.findall(r'\w\+', text, flags=re.DEBUG))

# s = "Я ищу совпадения в 2021. И я их найду в 2 счета."
# reg = r'[а-я]+'
# print(re.findall(reg, s))
# print(re.findall(reg, s, re.IGNORECASE))

# text = """
# one
# two
# """
# # print(re.findall(r'one.\w+', text))
# # print(re.findall(r'one.\w+', text, flags=re.DOTALL))
# print(re.findall(r'one$', text))
# print(re.findall(r'one$', text, flags=re.MULTILINE))

# text = """
# {
# "one": 1,
# "two": 2,
# "three": 3
# }
# """
# print(re.findall(r'^["\w]+', text))
# print(re.findall(r'^["\w]+', text, flags=re.MULTILINE))

# text = """Python,
# python,
# PYTHON"""
# reg = "(?im)^python"
# print(re.findall(reg, text))


# def validate_name(name):
#     return re.findall(r'^[a-z0-9_-]{3,16}$', name, re.IGNORECASE)
#
#
# print(validate_name('Python_master'))
# print(validate_name('Python'))

# s = "123456@i.ru, 123_456@ru.name.ru, login@i.ru, логин-1@i.ru, login.3@i.ru, login.3-67@i.ru, 1login@ru.name.ru, " \
#     "login.com@ru."
# reg = r"[\w.-]+@[\w.]+\w{2,3}"
# # reg = "[a-zа-я0-9@_.-]{3,25}"
# print(re.findall(reg, s))

# text = "<body>Пример жадного соответствия регулярных выражений</body>"
# print(re.findall('<.*?>', text))
# # *?, +?, ??
# # {m,n}?, {,n}?, {m,}?
# print(re.search('<.*?>', text).group())

# s = "<p>Изображение <img src='bg.jpg' alt='картинка'> - фон страницы</p>"
# reg = r'<img\s+[^>]*?src\s*=\s*[^>]+>'
# print(re.findall(reg, s))

# text = "Python[16][17] (в русском языке[] встречаются названия питон[18] или пайтон[19] - язык программирования)"
# # print(re.findall(r'\[[0-9]+]', text))
# print(re.findall(r'\[.*?]', text))

# s = "Петр, Ольга и Виталий отлично учатся!"
# reg = 'Петр|Ольга|Виталий|Валентина'
# print(re.findall(reg, s))

# s = "int = 4, float = 4.0, double = 8.0f"
# reg = r"(int|float)\s*=\s*(\d+[.\w+]*)"
# print(re.findall(reg, s))

# 192.168.255.255
# s = '127.0.0.1'
# # reg = r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}'
# reg = r'(?:\d{1,3}.){3}(?:\d{1,3})'
# print(re.findall(reg, s))

# s = "Word2016, PS6, AI5"
# reg = r'([a-z]+\d*)'
# print(re.findall(reg, s, re.I))

# s = "5 + 7*2 - 4"
# reg = r'\s*([+*-])\s*'
# print(re.split(reg, s))

# a = "31-01-2021"
# pattern = r'([0][1-9]|[1-2][0-9]|[3][01])-(0[1-9]|1[0-2])-(19[0-9][0-9]|20[0-9][0-9])'
# print(re.findall(pattern, a))

# s = "Базовый JS прост. Продвинутый Python сложен. Базовый Python прост."
# reg = r'[а-я]+(?= Python)'
# print(re.findall(reg, s, re.IGNORECASE))
# reg = r'Базовый(?! Python) \w+'
# print(re.findall(reg, s, re.IGNORECASE))
# reg = r'(?<=Базовый )\w{2,6}'
# print(re.findall(reg, s, re.IGNORECASE))
# reg = r'\w+ (?<!Продвинутый )Python'
# print(re.findall(reg, s, re.IGNORECASE))

# s = "Я ищу совпадения в 2021 году. И я их найду в 2 счета."
# reg = r'([0-9]+)\s(\D+)'
# print(re.search(reg, s).group())
# m = re.search(reg, s)
# print(m[0])
# print(m[1])
# print(m[2])

# <option value='1'>Самара</option>
# text = """
# Самара
# Москва
# Тверь
# Уфа
# Казань
# """
# count = 0
#
#
# def repl_find(m):
#     global count
#     count += 1
#     return f"<option value='{count}'>{m.group(1)}</option>\n"
#
#
# print(re.sub(r'\s*(\w+)\s*', repl_find, text))

# s = "<p>Изображение <img src=\"bg.jpg\"> - фон страницы</p>"
# # reg = r'<img\s+[^>]*src=([\'"])(.+?)\1'
# reg = r'<img\s+[^>]*src=(?P<q>[\'"])(.+?)(?P=q)'
# print(re.search(reg, s).group(2))

# (?P<name>...)  (?P=name)

# s = "Самолет прилетает 10/23/2021. Будем рады вас видеть после 10/24/2021"
# reg = r'(\d{2})/(\d{2})/(\d{4})'
# print(re.sub(reg, r'\2.\1.\3', s))  # 23.10.2021

# s = "google.com and google.ru"
# reg = r'(([a-z0-9-]{2,}\.)+[a-z]{2,4})'
# print(re.sub(reg, r'http://\1', s))

# def elevator(n):
#     if n == 0:
#         print("Вы в подвале")
#         return
#     print("=>", n)
#     elevator(n - 1)
#     print(n, end=" ")
#
#
# n1 = int(input("На каком вы этаже: "))
# elevator(n1)

# def sum_list(lst):
#     res = 0
#     for i in lst:
#         res = res + i
#     return res
# def sum_list(lst):
#     if len(lst) == 1:
#         print(lst, "=> lst[0]:", lst[0])
#         return lst[0]
#     else:
#         print(lst, "=> lst[0]:", lst[0])
#         return lst[0] + sum_list(lst[1:])
#
#
# print(sum_list([1, 3, 5, 7, 9]))
#
# lst1 = [1, 3, 4, 7, 9]
# s = 0
# def summ(x):
#     global s
#     if x == len(lst1):
#         return
#     s += lst1[x]
#     summ(x + 1)
#
#
# summ(0)
# print('\nSumma = ', s)

# def to_str(n, base):
#     convert = "0123456789ABCDEF"
#     if n < base:
#         return convert[n]
#     else:
#         a = to_str(n // base, base)
#         print(a)
#         return a + convert[n % base]  # 255 15
#
#
# print(to_str(255, 16))

# def count_leaf_items(lst):
#     count = 0
#     for item in lst:
#         if isinstance(item, list):
#             count += count_leaf_items(item)
#         else:
#             count += 1
#     return count

# def count_leaf_items(lst):
#     count = 0
#     stack = []
#     cur_lst = lst
#     i = 0
#     while True:
#         if i == len(cur_lst):
#             if cur_lst == lst:
#                 return count
#             else:
#                 cur_lst, i = stack.pop()
#                 i += 1
#         if isinstance(cur_lst[i], list):
#             stack.append([cur_lst, i])
#             cur_lst = cur_lst[i]
#             i = 0
#         count += 1
#         i += 1
#
#
# names = ["Adam", ["Bob", ["Chet", "Cat"], "Bart", "Bert"], "Alex", ["Bea", "Bill"], "Ann"]
# print(count_leaf_items(names))
# print(names[0])
# print(type(names[0]) == list)
# print(names[1])
# print(isinstance(names[1], list))
# print(names[1][1])
# print(isinstance(names[1][1], list))
# print(names[1][1][0])
# print(isinstance(names[1][1][0], list))

# print(len(names))


# def remove(text):
#     if not text:
#         return ""
#     if text[0] == "$" or text[0] == " ":
#         return remove(text[1:])
#     else:
#         return text[0] + remove(text[1:])
#
#
# print(remove("  Hello$World El$$ "))

# def union(s):
#     if not s:  # s == []: список пуст
#         return s
#     if isinstance(s[0], list):
#         return union(s[0]) + union(s[1:])
#     return s[:1] + union(s[1:])
#
# print("Программа принимает на вход список, состоящий из других списков, и возвращает обычный список,\nв котором "
#       "присутствуют все элементы из вложенных списков:")
# names = ['Adam', ['Bob', ['Chet', 'Cat'], 'Barb', 'Bert'],
#          'Alex', ['Bea', 'Bill'], 'Ann']
# print("Исходный список: ", names, "\n")
# print("Выпрямленный список: ", union(names))


# линейный или последовательный поиск
# def seq_search(s, item):
#     pos = 0
#     found = False
#     while pos < len(s) and not found:
#         if s[pos] == item:
#             found = True
#         else:
#             pos = pos + 1
#     return found
#
#
# lst = [1, 2, 32, 8, 17, 19, 42, 13, 0]
#
# print(seq_search(lst, 3))
# print(seq_search(lst, 13))

# def seq_search(s, item):
#     pos = 0
#     found = False
#     stop = False
#     while pos < len(s) and not found and not stop:
#         if s[pos] == item:
#             found = True
#         else:
#             if s[pos] > item:
#                 stop = True
#             else:
#                 pos = pos + 1
#     return found
#
#
# lst = [0, 1, 2, 8, 13, 17, 19, 32, 42]
#
# print(seq_search(lst, 3))
# print(seq_search(lst, 13))


# Бинарный поиск
# def binary_search(s, item):
#     first = 0
#     last = len(s) - 1
#     found = False
#
#     while first <= last and not found:
#         midpoint = (first + last) // 2
#         if s[midpoint] == item:
#             found = True
#         else:
#             if item < s[midpoint]:
#                 last = midpoint - 1
#             else:
#                 first = midpoint + 1
#
#     return found
#
#
# lst = [0, 1, 2, 8, 13, 17, 19, 32, 42]
#
# print(binary_search(lst, 12))
# print(binary_search(lst, 13))

# from random import randint
#
#
# def binary_search(s, item):
#     s.sort()
#     first = 0
#     last = len(s) - 1
#     found = False
#     while first <= last and not found:
#         midpoint = (first + last) // 2
#         if s[midpoint] == item:
#             found = True
#         else:
#             if item < s[midpoint]:
#                 last = midpoint - 1
#             else:
#                 first = midpoint + 1
#     return found
#
#
# lst = [randint(1, 100) for i in range(10)]
# print(lst)
# num = int(input("Введите число, которое хотите найти: "))
# # print(binary_search(lst, num))
# if binary_search(lst, num):
#     print(f"Число {num} в списке присутствует")
# else:
#     print(f"Число {num} в списке отсутствует")

from random import randint
import time as t

#
#
# def bubble(array):
#     for i in range(len(array) - 1):
#         for j in range(len(array) - i - 1):
#             if array[j] < array[j + 1]:
#                 array[j], array[j + 1] = array[j + 1], array[j]
#         # print(array)
#         # print("-" * 30)
#
#
# a = [randint(1, 99) for i in range(10)]
# print(a)
# # start = t.monotonic()
# bubble(a)
# print(a)
# # res = t.monotonic() - start
# # print(round(res, 4), "sec")


# def merge_sort(a):
#     n = len(a)
#     if n < 2:
#         return a
#     l = merge_sort(a[:n // 2])
#     r = merge_sort(a[n // 2:n])
#
#     i = j = 0
#     res = []
#
#     while i < len(l) or j < len(r):
#         if not i < len(l):
#             res.append(r[j])
#             j += 1
#         elif not j < len(r):
#             res.append(l[i])
#             i += 1
#         elif l[i] < r[j]:
#             res.append(l[i])
#             i += 1
#         else:
#             res.append(r[j])
#             j += 1
#     return res
#
#
# # array = [8, 2, 6, 4, 5]
# array = [randint(1, 99) for i in range(10000)]
# print(array)
# start = t.monotonic()
# array = merge_sort(array)
# print(array)
# res = t.monotonic() - start
# print(round(res, 4), "sec")
# def shell_sort(s):
#     gap = len(s)
#
#     while gap > 0:
#         for val in range(gap, len(s)):
#             cur_val = s[val]
#             pos = val
#
#             while pos >= gap and s[pos - gap] > cur_val:
#                 s[pos] = s[pos-gap]
#                 pos -= gap
#                 s[pos] = cur_val
#
#         gap //= 2
#         # print("После увеличения размера", gap, "Список:", s)
#     return s


# a = [randint(1, 99) for i in range(10)]
# print(a)
# a1 = [randint(1, 99) for i in range(10)]
# print(a1)
# # start = t.monotonic()
# shell_sort(a)
# print()
# print(a)
# shell_sort(a1)
# print(a1)
# res = t.monotonic() - start
# print(round(res, 4), "sec")

# all = [randint(1, 99) for j in range(10)]
# all1 = [randint(1, 99) for j in range(10)]
# print(all)
# print(all1)
# start = t.monotonic()
# all.sort()
# print(all)
# res = t.monotonic() - start
# print(round(res, 4), "sec")

# f = open(r'text.txt', 'r')   # , encoding="utf-8"
# print(f.read(3))
# print(f.read())
# # print(f.closed)
# # print(f.mode)
# # print(f.name)
# # print(f.encoding)
# # print(f)
# # print(*f)
# f.close()

# f = open(r'text.txt', 'r')
# try:
#     print(f.read())
# finally:
#     f.close()


# f = open(r'test.txt', 'r')
# print(f.readline())
# print(f.readline(8))
# print(f.readline())
# print(f.readline())
# f.close()

# f = open(r'test.txt', 'r')
# print(f.readlines(17))
# print(f.readlines())
# f.close()

# f = open(r'test.txt', 'r')
# for line in f:
#     print(line)
# f.close()

# f = open(r'test.txt', 'r')
# lst = f.readlines()
# print(lst)
# count = len(lst)
# print(count)
# f.close()

# f = open('xyz.txt', 'w')
# f.write('Hello \nWorld')
# f.close()

# f = open('xyz2.txt', 'a')
# lines = ['This is line 1', 'This is line 2', '50']
# f.writelines(lines)
# f.close()

# f = open('xyz.txt', 'w')
# lst = [str(i) + str(i-1) for i in range(1, 20)]
# print(lst)
# for index in lst:
#     f.write(index + '\t')
# f.close()

# my_file = open("text2.txt", "w")
# my_file.write("Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл;")
# my_file.close()
#
#
# my_file = open("text2.txt", "r")
# read_file = my_file.readlines()
# print(read_file)
# for i in range(len(read_file)):
#     if read_file[i] == "изменить строку в списке;\n":
#         read_file[i] = "Hello world!\n"
# print(read_file)
# my_file.close()
#
# my_file = open("text2.txt", "w")
# my_file.writelines(read_file)
# my_file.close()


# f = open("text2.txt", "w")
# f.write("Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл;")
# f.close()
#
# f = open("text2.txt")
#
# f = open("text2.txt", "w")
# f.writelines(s)
# f.close()

# f = open("text2.txt", 'r')
# text_data = f.readlines()
# print(text_data)
# f.close()

# index_del = int(input("какую строку удаляем "))
# if index_del > len(text_data):
#     print("нет такой строки")
# else:
#     f = open("text2.txt", 'w')
#     for i in range(len(text_data)):
#         if i == index_del - 1:
#             text_data[i] = ""
#     f.writelines(text_data)
# f.close()
#
# f = open("text2.txt", "r")
# print(f.readlines())
# f.close()

# f = open('text.txt', 'r')
# print(f.read(3))
# print(f.tell())  # 3
# print(f.seek(1))
# print(f.read())
# print(f.tell())
# f.close()

# f = open('text.txt', 'r+')
# print(f.write("I am learning Python"))
# print(f.seek(3))
# print(f.write("-new string-"))
# print(f.tell())
# f.close()

# with - контекстный мереджер
# with open('text.txt', "w+") as f:
#     print(f.write('0123456789'))
#
# with open('text.txt', 'r') as f:
#     for line in f:
#         print(line[:6])

# file_name = "res_1.txt"
# lst = [4.5, 2.8, 3.9, 1.0, 0.3, 4.33, 7.777]
#
#
# def get_line(lt):
#     lt = list(map(str, lt))
#     print(lt)
#     a = " ".join(lt)
#     print(a)
#     return a
#
#
# with open(file_name, "w") as f:
#     f.write(get_line(lst))
# print('Done!')


# file_name = "res_1.txt"
#
# with open(file_name, 'r') as f:
#     nums = f.read()
#
# print(nums)
#
# s = list(map(float, nums.split()))
# print(s)
# print(len(s))

# def longest_world(file):
#     with open(file, 'r') as text:
#         w = text.read().split()
#         max_length = len(max(w, key=len))
#         res = [word for word in w if len(word) == max_length]
#         return res
#
# print(longest_world('test.txt'))
#
#
# with open('test.txt', 'r') as f:
#     lst = f.read().split()
#     m = max(len(word) for word in lst)
#     print([i for i in lst if len(i) == m])

# text = "Строка №1\nСтрока №2\nСтрока №3\nСтрока №4\nСтрока №5\nСтрока №6\nСтрока №7\nСтрока №8\nСтрока №9\nСтрока №10\n"
# with open("one.txt", 'w') as f:
#     f.write(text)

# read_file = 'one.txt'
# write_file = 'two.txt'
#
# with open(read_file, 'r') as fr, open(write_file, 'w') as fw:
#     for line in fr:
#         line = line.replace("Строка", "Линия -")
#         fw.write(line)
#
# with open(write_file, 'r') as fr:
#     for line in fr:
#         print(line, end='')


import os
import os.path
import time

# print(os.getcwd())
# print(os.listdir())
# os.mkdir("folder")
# os.makedirs("nested1/nested2/nested3")
# os.remove("xyz.txt")
# os.rename("nested1", "test")
# os.rename("test.txt", "test/test.txt")
# os.rename("text.txt", "test/nested2/text1.txt")
# os.renames("two.txt", "text/three1.txt")
# os.rmdir("text")
# os.walk("путь к директории", topdown=True)

# for root, dirs, files in os.walk("test"):
#     print("Root:", root)
#     print("\tSubdirs:", dirs)
#     print("\tFiles:", files)

# for root, dirs, files in os.walk("test"):

# for path, names, files in os.walk("test", topdown=False):
#     if not os.listdir(path):
#         os.rmdir(path)
#         print(f"Директория {path} удалена")

# print(os.path.split(r"D:\pythonProject5\test\nested2\text1.txt")[1])
# print(os.path.dirname(r"D:\pythonProject5\test\nested2\text1.txt"))
# print(os.path.basename(r"D:\pythonProject5\test\nested2\text1.txt"))
#
# print(os.path.join("folder", "files", "/home", "dir", "three.txt"))


# dirs = ["Work/F1", "Work/F2/F21"]
# for dir1 in dirs:
#     os.makedirs(dir1)
#
# files = {
#     'Work': ['w.txt'],
#     'Work/F1': ['f11.txt', 'f12.txt', 'f13.txt'],
#     'Work/F2/F21': ['f211.txt', 'f212.txt']
# }
#
# for dir1, files in files.items():
#     for file in files:
#         file_path = os.path.join(dir1, file)
#         open(file_path, "w").close()
#
#
# file_with_text = ['Work/w.txt', 'Work/F1/f12.txt', 'Work/F2/F21/f211.txt', 'Work/F2/F21/f212.txt']
# for file in file_with_text:
#     with open(file, "w") as f:
#         f.write(f"some sample text for {file} file")
#
#
# def print_tree(root, topdown):
#     print(F"Обход {root} {'сверху вних' if topdown else 'снизу вверх'}")
#     for root, dirs, files in os.walk(root, topdown=topdown):
#         print(root)
#         print(dirs)
#         print(files)
#     print("-" * 40)
#
#
# print_tree("Work", topdown=False)
# print_tree("Work", topdown=True)

# print(os.path.exists(r"D:\pythonProject5\Work\F2\F21\f212.txt"))
# print(os.path.exists(r"D:\pythonProject5\Work\F2\F21\f2123.txt"))
# path = r"text2.txt"
# print(os.path.getctime(path))  # время создания файла
# print(os.path.getatime(path))  # время последнего доступа к файла
# print(os.path.getmtime(path))  # время последнего измения файла
# print(os.path.getsize(path))  # размер файла в байтах

# path = r"111.py"
# size = os.path.getsize(path)
# ksize = size // 1024
# atime = os.path.getatime(path)
# mtime = os.path.getmtime(path)
# print(time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(atime)))  # время последнего доступа к файла
# print(time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(mtime)))  # время последнего измения файла
#
# print("Размер:", ksize, "KB")

# file_path = "text/three.txt"
#
# if os.path.exists(file_path):
#     dir, name = os.path.split(file_path)
#     atime = os.path.getatime(file_path)
#     print(f"{name} ({dir}) - last access time {atime} sec")
# else:
#     print(f"File {file_path} does not exist!")

# print(os.path.normcase(r"D:/pythonProject5/text/three.txt"))
# print(os.path.relpath(r"D:\pythonProject5\text\three.txt"))
# print(os.path.isfile(r"D:\pythonProject5\text\three.txt"))
# print(os.path.isdir(r"D:\pythonProject5\text"))

# dir_name = "Work"
#
# objs = os.listdir(dir_name)
# print(objs)
# for obj in objs:
#     p = os.path.join(dir_name, obj)
#     # print(p)
#     if os.path.isfile(p):
#         print(f"{obj} - file - {os.path.getsize(p)} bytes")
#     elif os.path.isdir(p):
#         print(f"{obj} - dir")

# print("Вносим изменения")
# print("*" * 40)
# print("Вносим изменения на новом утройстве")
# print("*" * 40)


# def sum_date(a, b):
#     return a + b
#
#
# print(sum_date(3, 2))
# print(sum_date("Hello", "world"))


# print("Получилось")


# for root, dirs, files in os.walk("Work"):
#     for name in files:
#         j = os.path.join(root, name)
#         s = os.path.getsize(j)
#         if s != 0:
#             print(name, s, "bytes")
#         if s == 0:
#             print(name)
#             os.rename(j, os.path.join("D_Z", name))
#             print(f"файл {name} перемещен по адресу Work/D_Z ")

# for root, dirs, files in os.walk("Work"):
#     for name in files:
#         s = os.path.getsize(os.path.join(root, name))
#         if s != 0:
#             print(name, s, "bytes")

# EMPTY_DIR = 'Work/empty_files'
# for root, dirs, files in os.walk("Work"):
#     if "Work" == EMPTY_DIR:
#         continue
#     for name in files:
#         file_path = os.path.join("Work", name)
#         file_size = os.path.getsize(file_path)
#         if file_size == 0:
#             # print(name)
#             os.rename(file_path, os.path.join(EMPTY_DIR, name))
#             print(f"файл {name} перемещен из папки {root} в папку Work/D_Z")
import os, os.path


def info_files(root, folder):
    for root, dirs, files in os.walk(root):
        if root == folder:
            continue
        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)
            if file_size == 0:
                os.rename(file_path, os.path.join(folder, file))
                print(f"Файл {file} перемещен из папки {root} в папку {folder}")
            else:
                print(f"{file_path} - {file_size} bytes")


info_files('Work', 'Work/D_Z')




