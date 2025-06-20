# Домашнее задание по теме "Сложные моменты и исключения в стеке вызовов функции"

def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for i in numbers:
        try:
            result += i
        except TypeError:
            incorrect_data += 1
            print(f'Некорректный тип данных для подсчёта суммы -', *{i})
    return tuple((result, incorrect_data))  # tuple указан исключительно для PyCharm, чтобы не ругался на скобки

def calculate_average(numbers):
    try:
        summ = personal_sum(numbers)
        result = summ[0] / (len(numbers) - summ[1])     # В знаменателе - разница между общим кол-вом принятых
        return result                               # аргументов и количеством тех из них, что оказались некорректными
    except ZeroDivisionError:
        return 0
    except TypeError:
        print('В numbers записан некорректный тип данных')
        return None


# Проверка на тестовых данных:
print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать

