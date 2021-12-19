# class Point3D:
#     pass


class Point:
    # x = 1
    # y = 1

    def set_coords(self, x, y):
        self.x = x
        self.y = y
        self.z = self.x + self.y
        print(self.z)

    def print_info(self):
        print(f"Координата x: {self.x}, координата y: {self.y}, cумма: {self.z}")


p1 = Point()

# p1.x = 5
# p1.y = 10
p1.set_coords(5, 10)
p1.print_info()
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
print("p1:", p1.__dict__)
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
