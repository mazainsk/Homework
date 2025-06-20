# Дополнительное практическое задание по модулю 6 "Наследование классов"

from math import pi


class Figure:
    sides_count: int = 0

    def __init__(self, color, *sides):
        self.filled = False   # применения данному атрибуту не нашёл, здесь он только для выполнения условия задачи
        self.__color = []
        self.__sides = [1] * self.sides_count
        self.set_color(*color)
        self.set_sides(*sides)

    def __len__(self):
        return sum(self.__sides)

    def __str__(self):
        return (f'Фигура: {self.__class__.__name__}, Цвет: {self.__color}, Длины сторон ({self.sides_count} шт):'
                f' {self.__sides}')

    def __eq__(self, other):
        return (self.__class__.__name__ == other.__class__.__name__) and (self.__len__() == other.__len__())

    def print_info(self):
        print(f'Длина окружности: ' if self.__class__.__name__ == 'Circle' else '', end='')
        print(f'Периметр: ' if self.__class__.__name__ == 'Triangle' else '', end='')
        print(f'Сумма длин рёбер: ' if self.__class__.__name__ == 'Cube' else '', end='')
        print(self.__len__())
        print(f'Площадь: {self.get_square()}') if hasattr(self, 'get_square') else ''
        print(f'Объём: {self.get_volume()}') if hasattr(self, 'get_volume') else ''
        print(f'Радиус: {self.__radius}') if hasattr(self, '__radius') else ''
        print()

    def get_color(self):
        return self.__color

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def get_sides(self):
        return self.__sides

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides.clear()
            if self.__class__.__name__ == 'Cube':
                self.__sides = [new_sides[0]] * self.sides_count
            else:
                [self.__sides.append(side) for side in new_sides]

    def __is_valid_color(self, r, g, b):
        return all(map(lambda x: isinstance(x, int) and (0 <= x <= 255), [r, g, b]))

    def __is_valid_sides(self, *sides):
        if self.__class__.__name__ == 'Cube':
            return (len(sides) == 1) and (isinstance(sides[0], int) and (sides[0] > 0))
        else:
            return ((len(sides) == self.sides_count) and
                    (all(map(lambda x: isinstance(x, int) and (x > 0), sides))))


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, side):
        super().__init__(color, side)
        self.__radius = super().get_sides()[0] / (2 * pi)

    def get_square(self):
        return pi * self.__radius ** 2

class Triangle(Figure):
    sides_count = 3

    def get_square(self):
        pp = super().__len__() / 2
        sides = super().get_sides()
        return (pp * (pp - sides[0]) * (pp - sides[1]) * (pp - sides[2])) ** 0.5

class Cube(Figure):
    sides_count = 12

    def get_volume(self):
        return super().get_sides()[0] ** 3


if __name__ == '__main__':

    # Проверка на тестовых данных

    # Проверка на корректность задания длин сторон при создании объектов
    circle1 = Circle((200, 200, 100), 10)
    print(circle1)
    circle1.print_info()
    triangle1 = Triangle((255, 0, 255), 2, 3, 4)
    print(triangle1)
    triangle1.print_info()
    triangle1 = Triangle((255, 0, 255), 2, 3, 4, 7) # лишняя сторона -> создастся с 1-1-1
    print(triangle1)
    triangle1.print_info()
    triangle1 = Triangle((255, 0, 255), 2, 3, -1) # отрицательная длина стороны -> создастся с 1-1-1
    print(triangle1)
    triangle1.print_info()
    cube1 = Cube((222, 35, 130), 6)
    print(cube1)
    cube1.print_info()

    # Проверка на изменение цветов:
    circle1.set_color(55, 66, 77)       # изменится
    print(circle1.get_color())
    triangle1.set_color(2.5, 10, 0)     # не изменится
    print(triangle1.get_color())
    cube1.set_color(300, 70, 15)        # не изменится
    print(cube1.get_color())

    # Проверка на изменение сторон:
    cube1.set_sides(5, 3, 12, 4, 5)    # не изменится
    print(cube1.get_sides())
    circle1.set_sides(15)                       # изменится
    print(circle1.get_sides())
    triangle1.set_sides(4, 3, 2)      # изменится
    print(triangle1.get_sides())

    # Проверка периметра и площади:
    print(len(circle1))
    print(len(triangle1))
    print(circle1.get_square())
    print(triangle1.get_square())


    # Проверка объёма (куба):
    print(cube1.get_volume())
