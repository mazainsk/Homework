class House:
    """
    Класс для развития навыков работы с объектами, их атрибутами и методами
    """
    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return object.__new__(cls)

    def __init__(self, name: str, number_of_floors: int):
        self.name = name
        self.number_of_floors = number_of_floors
        print(f'Создано здание "{self.name}" с количеством этажей {self.number_of_floors}')
        print('Список истории строительства:', House.houses_history)

    def __del__(self):
        print(f'"{self.name}" снесён, но он останется в истории: {House.houses_history}')

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
#print(House.houses_history)
h2 = House('ЖК Акация', 20)
#print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
#print(House.houses_history)
del h2
del h3
#print(House.houses_history)
