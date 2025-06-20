# Домашнее задание по теме "Try и Except"

def add_everything_up(*args):
    """
    Функция складывает числа, строки и булевы типы, учитывает вложенные списки и кортежи,
    аргументы не подходящего типа пропускаются.
    """
    values = []

    # Вложенная функция рекурсивного перестроения входных аргументов в новый ("плоский") список
    # с исключением из него элементов не подходящих типов
    def args_remap(*args):
        nonlocal values     # можно не указывать, т.к. переменные не переопределяются, но так читабельнее
        for arg in args:
            if isinstance(arg, (int, float, bool, str)):
                values.append(arg)
            elif isinstance(arg, (list, tuple, set)):
                args_remap(*arg)
            elif isinstance(arg, dict):     # словари - в отдельной проверке, т.к. складываю и ключи и значения
                args_remap(*arg.items())

    args_remap(*args)
    try:
        result = sum(values)
    except TypeError:
        result = ''.join(str(i) for i in values)
    return result


# Проверка на тестовых данных:

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215, '_против_груши', 48.2))
print(add_everything_up(123.456, 7))
print(add_everything_up(5, False, True))
print(add_everything_up(64.8, [1, 2, 3, ('?', {'a': 17, 'b': ('0', '_1_', 0)}), 90], False))
print(add_everything_up('1', {'abc', None}, '?'))
