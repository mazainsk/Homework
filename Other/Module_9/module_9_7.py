# Домашнее задание по теме "Декораторы"

import functools

def is_prime(func):
    @functools.wraps(func)    # Встроенный декоратор для переноса метаданных из декорируемой функции
    def wrapper(*args):
        check_func = lambda n: n > 1 and all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))
        text = f'{'Простое' if check_func(func(*args)) else 'Составное'}'
        return func(*args), text
    return wrapper

def is_even(func):
    @functools.wraps(func)
    def wrapper(*args):
        print(f'->> Вызов функции {func.__name__}() с аргументами {args}')
        orig_f = func(*args)
        print(f'->> Описание: {func.__doc__}')
        print(f'->> {func.__name__}() вернула {orig_f}')
        text = (f'{'Четное' if not (orig_f[0] % 2) else 'Нечетное'}, знаков {len(str(orig_f[0]))}, '
                f'сумма чисел = {sum(int(i) for i in str(orig_f[0]))}')
        return *orig_f, text
    return wrapper

# Применение декоратора is_prime (и опционально - is_even) для обертывания функции sum_three
@is_even
@is_prime
def sum_three(num_1, num_2, num_3):
    """Возвращает сумму трёх чисел"""
    return sum((num_1, num_2, num_3))


# Проверка на тестовых данных:
res = sum_three(2, 3, 6)    # 11 - число нечетное, знаков 2, простое
print(*res, sep='\n')
print()
res = sum_three(108, 4, 14)   # 126 - число четное, знаков 3, составное
print(*res, sep='\n')
print()
print(sum_three.__doc__)    # Для проверки. Без использования декоратора functools.wraps метаданные функции sum_three
                            # будут скрыты замыканием wrapper (тут будет None)