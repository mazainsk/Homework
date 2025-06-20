# Домашнее задание по теме "Доступ к свойствам родителя. Переопределение свойств"

from random import choice

class Vehicle:
    # Список цветов не планируется изменять, поэтому не список (как в описании задачи), а кортеж:
    __COLOR_VARIANTS = ('blue', 'red', 'green', 'black', 'white', 'yellow', 'purple', 'gray', 'pink', 'brown', 'silver')

    def __init__(self, owner: str, model: str, power: int, color: str=''):
        self.owner = owner
        self.__model = model
        self.__engine_power = power
        if color in self.__COLOR_VARIANTS:
            self.__color = color
        else:
            self.__color = choice(self.__COLOR_VARIANTS)    # Цвет будет выбран случайным образом из доступных

    def get_model(self):
        return f'Модель: {self.__model}'

    def get_horse_power(self):
        return f'Мощность двигателя: {self.__engine_power}'

    def get_color(self):
        return f'Цвет: {self.__color}'

    def print_info(self):
        print(self.get_model(), self.get_horse_power(), self.get_color(), f'Владелец: {self.owner}', sep='\n')

    def set_color(self, new_color: str):
        new_color = new_color.lower()       # учета регистра не будет
        if new_color != self.__color:       # продолжать, только если новый цвет не совпадает с текущим
            if new_color not in self.__COLOR_VARIANTS:
                # если новый цвет не из перечня доступных, то либо оставить как есть, либо перекрасить на новый
                print(f'Нельзя изменить текущий цвет {self.__color} на {new_color}')
                if not input(f'Перекрасить на случайный цвет из доступных? ('
                             f'да/нет) >> ').lower().startswith('д'):
                    print()
                    return      # оставить цвет без изменений, выйти из метода
                else:
                    # перекраска на новый цвет, который не равен текущему
                    new_color_list = list(self.__COLOR_VARIANTS)
                    new_color_list.remove(self.__color)
                    new_color = choice(new_color_list)
            print(f'Текущий цвет {self.__color} изменён на {new_color}\n')
            self.__color = new_color


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

    # переопределение родительского метода для вывода дополнительной информации по кол-ву пассажиров
    def print_info(self):
        super().print_info()
        print(f'Вместимость: {self.__PASSENGERS_LIMIT}\n')
    pass


if __name__ == '__main__':

    # Проверка на тестовых данных

    vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500)        # Цвет будет выбран произвольно
    vehicle2 = Sedan('Patterson', 'Volvo S50', 340, 'white')

    # Изначальные свойства
    vehicle1.print_info()
    vehicle2.print_info()

    # Меняем свойства (в т.ч. вызывая методы)
    vehicle1.set_color('Pink')      # поменяет
    vehicle1.set_color('BLACK')     # поменяет
    vehicle2.set_color('orange')    # должен выдать "Нельзя сменить"
    vehicle1.owner = 'Vasyok'

    # Проверяем что поменялось
    vehicle1.print_info()
    vehicle2.print_info()   # если при попытке смены цвета на недопустимый orange (см.выше) ответили положительно на запрос
                            # на перекраску, то должен выдать новый цвет из списка допустимых