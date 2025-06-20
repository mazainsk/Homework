class House:

    def __init__(self, name: str, number_of_floors: int):
        self.name = name
        self.number_of_floors = number_of_floors
        print(f'Создано здание "{self.name}" с количеством этажей {self.number_of_floors}')

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return 'Название: "' + self.name + '", кол-во этажей: ' + str(self.number_of_floors)

    def go_to(self, new_floor):
        if 1 <= new_floor <= self.number_of_floors:
            print(f'В здании "{self.name}" едем с 1-го на {new_floor}-й этаж:')
            for i in range(1, new_floor + 1):
                print(i)
        else:
            print(f'{new_floor} - такого этажа в здании "{self.name}" не существует')

    # Реализация операций сравнения атрибута "количество этажей" у разных объектов:
    def __eq__(self, other):
        # Здесь и далее перед выполнением операций нужно проверить, является ли other числом или объектом класса House и
        # в противном случае вызвать программное прерывание (например, исключение TypeError).
        # Однако мы еще не изучали тему исключений, поэтому просто буду возвращать сообщение об ошибке.
        if not isinstance(other, (int, float, House)):
            return f'Неподдерживаемый тип данных для операции сравнения: "{type(other).__name__}"'
        return self.number_of_floors == change_type_of_value(other)
    def __lt__(self, other):
        if not isinstance(other, (int, float, House)):
            return f'Неподдерживаемый тип данных для операции сравнения: "{type(other).__name__}"'
        return self.number_of_floors < change_type_of_value(other)
    def __le__(self, other):
        if not isinstance(other, (int, float, House)):
            return f'Неподдерживаемый тип данных для операции сравнения: "{type(other).__name__}"'
        return self.number_of_floors <= change_type_of_value(other)
    def __gt__(self, other):
        if not isinstance(other, (int, float, House)):
            return f'Неподдерживаемый тип данных для операции сравнения: "{type(other).__name__}"'
        return self.number_of_floors > change_type_of_value(other)
    def __ge__(self, other):
        if not isinstance(other, (int, float, House)):
            return f'Неподдерживаемый тип данных для операции сравнения: "{type(other).__name__}"'
        return self.number_of_floors >= change_type_of_value(other)
    def __ne__(self, other):
        if not isinstance(other, (int, float, House)):
            return f'Неподдерживаемый тип данных для операции сравнения: "{type(other).__name__}"'
        return self.number_of_floors != change_type_of_value(other)

    # Реализация некоторых арифметических операций, которые можно выполнять над этажами (сложение, вычитание,
    # умножение и деление).
    def __add__(self, other):
        if not isinstance(other, (int, float, House)):
            print(f'Неподдерживаемый тип данных для операции сложения: "{type(other).__name__}"')
        else:
            self.number_of_floors += change_type_of_value(other)
                # Если я правильно понимаю, то такое поведение скорее характерно для метода __iadd__,
                # здесь желательно возвращать другой объект:
                # return House(self.name, self.number_of_floors + value)
                # Но у нас, согласно п.3 имеет место упрощение - должен возвращаться сам объект self, поэтому:
        return self
    def __sub__(self, other):
        if not isinstance(other, (int, float, House)):
            print(f'Неподдерживаемый тип данных для операции вычитания: "{type(other).__name__}"')
        else:
            self.number_of_floors -= change_type_of_value(other)
        return self
    def __mul__(self, other):
        if not isinstance(other, (int, float, House)):
            print(f'Неподдерживаемый тип данных для операции умножения: "{type(other).__name__}"')
        else:
            self.number_of_floors *= change_type_of_value(other)
        return self
    def __floordiv__(self, other):
        if not isinstance(other, (int, float, House)):
            print(f'Неподдерживаемый тип данных для операции деления: "{type(other).__name__}"')
        else:
            self.number_of_floors //= change_type_of_value(other)
        return self
    def __truediv__(self, other):
        return self.__floordiv__(other)   # Обычное деление будет аналогично целочисленному

    # Согласно пункту 1 примечаний к заданию "Методы __iadd__ и __radd__ не обязательно описывать заново, достаточно
    # вернуть значение вызова __add__". Поэтому и остальные методы для упрощения - по аналогии:
    def __radd__(self, other):
        return self.__add__(other)
    def __iadd__(self, other):
        return self.__add__(other)
    def __rsub__(self, other):
        return self.__sub__(other)
    def __isub__(self, other):
        return self.__sub__(other)
    def __rmul__(self, other):
        return self.__mul__(other)
    def __imul__(self, other):
        return self.__mul__(other)
    def __rfloordiv__(self, other):
        return self.__floordiv__(other)
    def __ifloordiv__(self, other):
        return self.__floordiv__(other)
    def __rtruediv__(self, other):
        return self.__truediv__(other)
    def __itruediv__(self, other):
        return self.__truediv__(other)

# Повторяющийся фрагмент кода - в отдельной функции:
def change_type_of_value(value) -> int:
    if isinstance(value, House):
        return value.number_of_floors
    elif isinstance(value, float):
        return int(value)
    else:
        return value


# Проверка на тестовых данных:

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2)     # __eq__ высоты не равны, должно быть False

h1 = h1 + 10        # __add__ изменение высоты 1го здания (будет 20)
print(h1)
print(h1 == h2)     # теперь высоты равны, должно быть True

h1 += 10            # __iadd__ высота 1го здания теперь 30
print(h1)

h2 = 10 + h2        # __radd__ высота 2го здания теперь тоже 30
print(h2)

print(h1 > h2)      # __gt__ первое здание равно по высоте второму, поэтому тут будет False
print(h1 >= h2)     # __ge__ True
print(h1 < h2)      # __lt__ False
print(h1 <= h2)     # __le__ True
print(h1 != h2)     # __ne__ False

h1 *= (1,5)             # __imul__ на кортеж должен выдать сообщение "неподдерживаемый тип данных"
print(h1 != 'Эльбрус')  # сравнение со строкой должно выдать сообщение "неподдерживаемый тип данных"
h1 *= 4                 # __imul__ должен умножить и вернуть 120 (4 * 30)
print(h1)

h1 = (h1 / 2 - 3 ) // 2.7   # 120 / 2 = 60, затем минус 3 получится 57, и потом целочисленно разделить на int(2.7)
print(h1)                   # (т.е. на 2) и в результате получится 28 (отбрасывается дробная часть 0.5)
print(h2 - 1)               # 30 минус 1 будет 29