# По условию задачи в любой структуре переданных данных функция должна считать:
# 1. все числа (не важно, являются они ключами или значениями или ещё чем-то);
# 2. все строки (не важно, являются они ключами или значениями или ещё чем-то).
# Дополнительно я сделал так, что считается длина символьного представления чисел с плавающей запятой
# и учитываются булевы значения (True = 1, Bool = 0).

data_structure = [
3.014, 'True', True, False,             # сумма значений этих элементов = 10
[1, 2, 3],                              # сумма значений этих элементов = 6
{'a': 4, 'b': 5},                       # сумма значений этих элементов = 11
(6, {'cube': 7, 'drum': 8}),            # сумма значений этих элементов = 29
"Hello",                                # сумма значений этих элементов = 5
((), [{(2, 'Urban', ('Urban2', 35))}])  # сумма значений этих элементов = 48
]

def calculate_structure_sum(*data_):
    count_ = 0
    for i in data_:
        if isinstance(i, (int, bool)):
            count_ += i             # Для int и bool берется его значение (True = 1, Bool = 0).
        elif isinstance(i, str):
            count_ += len(i)        # Для str считается количество символов в этой строке.
        elif isinstance(i, float):
            count_ += len(str(i))   # Для float считается кол-во символов в его строковом представлении.
        elif isinstance(i, (list, tuple, set)):
            for j in i:
                count_ += calculate_structure_sum(j)    # Рекурсивный вызов по каждому элементу коллекции.
        elif isinstance(i, dict):
            for j in i.items():
                count_ += calculate_structure_sum(j)    # Рекурсивный вызов по каждой паре "ключ-значение" (как кортеж).
        else:
            return 0    # Неизвестный тип данных.
    return count_

result = calculate_structure_sum(data_structure)
print(result)