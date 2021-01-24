# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
import math

class Triangle:
    def __init__(self, A, B, C):
        self.A = A
        self.B = B
        self.C = C

        def side(coordinateX, coordinateY):
            """
            Вычисляет длину стороны треугольника по координатам точек
            :param coordinateX: координата Х
            :param coordinateY: координата У
            :return: длина стороны треугольника
            """
            return math.sqrt(pow((coordinateX[0] - coordinateY[0]), 2)
                             + pow((coordinateX[1] - coordinateY[1]), 2))

        self.AB = side(self.A, self.B)
        self.BC = side(self.B, self.C)
        self.CA = side(self.C, self.A)

    def perimeter(self):
        """
        Вычисляет периметр треугольника
        :return: периметр треугольника
        """
        return self.AB + self.BC + self.CA

    def area(self):
        """
        Вычисляет площадь треугольника по формуле Герона
        :return: площадь треугольника
        """
        semi_perimeter = self.perimeter() / 2
        return math.sqrt(semi_perimeter
                         * (semi_perimeter - self.AB)
                         * (semi_perimeter - self.BC)
                         * (semi_perimeter - self.CA))

    def height(self):
        """
        Вычисляет высоту треугольника
        :return: высота треугольника
        """
        return self.area() / (self.AB / 2)


abc = Triangle((2, 4), (1, 5), (3, 2))

print(abc.perimeter())
print(abc.area())
print(abc.height())

# Мой первый вариант решения этой задачи. Но тут слишком DRY
# from math import sqrt, pow
#
# class Triangle:
#     def __init__(self, X1, Y1, X2, Y2, X3, Y3):
#         self.X1 = X1
#         self.Y1 = Y1
#         self.X2 = X2
#         self.Y2 = Y2
#         self.X3 = X3
#         self.Y3 = Y3
#
#     def area(self):
#         return 0.5 * ((self.X2 - self.X1) * (self.Y3 - self.Y1) -
#                       (self.X3 - self.X1) * (self.Y2 - self.Y1))
#
#     def perimeter(self):
#         return sqrt(pow((self.X2 - self.X1), 2) + pow((self.Y2 - self.Y1), 2)) + \
#                sqrt(pow((self.X3 - self.X2), 2) + pow((self.Y3 - self.Y2), 2)) + \
#                sqrt(pow((self.X3 - self.X1), 2) + pow((self.Y3 - self.Y1), 2))
#
#     def height(self):
#         p = sqrt(pow((self.X2 - self.X1), 2) + pow((self.Y2 - self.Y1), 2)) + \
#                    sqrt(pow((self.X3 - self.X2), 2) + pow((self.Y3 - self.Y2), 2)) + \
#                    sqrt(pow((self.X3 - self.X1), 2) + pow((self.Y3 - self.Y1), 2)) / 2
#
#         hA = (2 * sqrt(p * (p - sqrt(pow((self.X2 - self.X1), 2) + pow((self.Y2 - self.Y1), 2)))
#           * (p - sqrt(pow((self.X3 - self.X2), 2) + pow((self.Y3 - self.Y2), 2))) *
#             (p - sqrt(pow((self.X3 - self.X1), 2) + pow((self.Y3 - self.Y1), 2))))) / \
#             sqrt(pow((self.X2 - self.X1), 2) + pow((self.Y2 - self.Y1), 2))
#
#         hB = (2 * sqrt(p * (p - sqrt(pow((self.X2 - self.X1), 2) + pow((self.Y2 - self.Y1), 2)))
#           * (p - sqrt(pow((self.X3 - self.X2), 2) + pow((self.Y3 - self.Y2), 2))) *
#             (p - sqrt(pow((self.X3 - self.X1), 2) + pow((self.Y3 - self.Y1), 2))))) \
#             / sqrt(pow((self.X3 - self.X2), 2) + pow((self.Y3 - self.Y2), 2))
#
#         hC = (2 * sqrt(p * (p - sqrt(pow((self.X2 - self.X1), 2) + pow((self.Y2 - self.Y1), 2)))
#           * (p - sqrt(pow((self.X3 - self.X2), 2) + pow((self.Y3 - self.Y2), 2))) *
#             (p - sqrt(pow((self.X3 - self.X1), 2) + pow((self.Y3 - self.Y1), 2))))) \
#             / sqrt(pow((self.X3 - self.X1), 2) + pow((self.Y3 - self.Y1), 2))
#         return hA, hB, hC
#
#
# abc = Triangle(2, 4, 1, 5, 3, 2)
#
# print(abc.area())
# print(abc.perimeter())
# print(abc.height())


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class Trapezoid:
    def __init__(self, A, B, C, D):
        self.A = A
        self.B = B
        self.C = C
        self.D = D

        def side(coordinateX, coordinateY):
            """
            Вычисляет длину стороны треугольника по координатам точек
            :param coordinateX: координата Х
            :param coordinateY: координата У
            :return: длина стороны треугольника
            """
            return math.sqrt(pow((coordinateX[0] - coordinateY[0]), 2)
                             + pow((coordinateX[1] - coordinateY[1]), 2))

        self.AB = side(self.A, self.B)
        self.BC = side(self.B, self.C)
        self.CD = side(self.C, self.D)
        self.DA = side(self.D, self.A)
        self.diagonal_AC = side(self.C, self.A)
        self.diagonal_BD = side(self.B, self.D)
        self.perimeter = self.AB + self.BC + self.CD + self.DA

        def areaTriangle(side1, diagonal, side2):
            """
            Вычисляет площадь треугольника
            :return: площадь треугольника
            """
            semi_perimeter = (side1 + diagonal + side2) / 2

            return math.sqrt(semi_perimeter
                             * (semi_perimeter - side1)
                             * (semi_perimeter - diagonal)
                             * (semi_perimeter - side2))


        self.area = areaTriangle(self.AB, self.diagonal_BD, self.DA) \
                    + areaTriangle(self.diagonal_BD, self.BC, self.CD)

    def isTrapezeEqu(self):
        """
        Проверяет, является ли фигура равнобочной трапецией
        :return: bool
        """
        if self.diagonal_AC == self.diagonal_BD:
            return True
        return False

abcd = Trapezoid((2,3), (1,5), (2,7), (3,9))

print(abcd.isTrapezeEqu())