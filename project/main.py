# from shapes import rectangle
# from shapes import circle
# from shapes import cylinder
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