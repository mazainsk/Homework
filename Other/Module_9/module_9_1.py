# Домашнее задание по теме "Введение в функциональное программирование"

def apply_all_func(int_list, *functions):
    # Вариант 1: если хотя бы один элемент в списке не является типом int или float, то вернуть сообщение об ошибке
    # if any(not isinstance(i, (int, float)) for i in int_list):
    #     return 'Все аргументы в списке должны быть числами!'

    # Вариант 2: если среди элементов списка встречается строка, то пытаться преобразовать ее в число
    error_message = 'Недопустимый элемент в списке'
    for i, value in enumerate(int_list):
        if isinstance(value, (int, float)):
            continue
        if not isinstance(value, str):
            return error_message
        else:
            try:
                int_list[i] = float(value)
            except ValueError:
                return error_message
    results = {}
    for func in functions:
        results[func.__name__] = func(int_list)
    return results


# Проверка на тестовых данных:
print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
print(apply_all_func([6, 20, 15, '9.0'], len, sum, sorted))
print(apply_all_func([6, 20, 15, '9,0'], len, sum, sorted))