# Домашнее задание по теме "Создание исключений"

class Car:

    def __init__(self, model, vin, num):
        self.model = model
        if self.__is_valid_vin(vin):
            self.__vin = vin
        if self.__is_valid_numbers(num):
            self.__numbers = num

    def __is_valid_vin(self, vin_number):
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber(vin_number, 1)
        if not (1000000 <= vin_number <= 9999999):
            raise IncorrectVinNumber(vin_number, 2)
        else:
            return True

    def __is_valid_numbers(self, numbers):
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers(numbers, 1)
        elif len(numbers) != 6:
            raise IncorrectCarNumbers(numbers, 2)
        else:
            return True


class IncorrectVinNumber(Exception):

    def __init__(self, vin_num, exc_type):
        super().__init__()  # В пользовательских классах исключений рекомендуется вызывать родительский init через
                            # super, чтобы подгрузились дефолтные атрибуты
        if exc_type == 1:
            self.message = f'Некорректный тип данных для vin номера "{vin_num}"'
        elif exc_type == 2:
            self.message = f'Неверный диапазон для vin номера "{vin_num}"'


class IncorrectCarNumbers(Exception):

    def __init__(self, num, exc_type):
        super().__init__()
        if exc_type == 1:
            self.message = f'Некорректный тип данных для номеров "{num}"'
        elif exc_type == 2:
            self.message = f'Неверная длина номера "{num}"'


try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')
