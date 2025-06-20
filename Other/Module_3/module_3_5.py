# Функция, которая считает произведение цифр числа рекурсивным методом
def get_multiplied_digits(number):
    str_number = str(number)
    if len(str_number) < 2:
        return int(str_number)
    first = int(str_number[0])
    from_second = int(str_number[1:])   # Если со следующего знака относительно текущей позиции идут нули, то
                                        # при преобразовании строки в число эти нули автоматически игнорируются.
    if from_second == 0:    # Если число, переданное в функцию, заканчивается на ноль/нули,то необходимо
        return first        # прекратить рекурсию на текущей цифре (это последняя цифра, не равная нулю).
    return first * get_multiplied_digits(from_second)

result = get_multiplied_digits(41300200)
print(result)
        