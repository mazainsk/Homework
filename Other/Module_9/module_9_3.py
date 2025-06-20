# Домашнее задание по теме "Генераторные сборки"

# Условия:
# В переменную first_result запишите генераторную сборку, которая высчитывает разницу длин строк из списков first и
# second, если их длины не равны. Для перебора строк попарно из двух списков используйте функцию zip.
# В переменную second_result запишите генераторную сборку, которая содержит результаты сравнения длин строк в
# одинаковых позициях из списков first и second. Составьте эту сборку НЕ используя функцию zip. Используйте range и len.

# Исходные данные:
first_list = ['Strings', 'Student', 'Computers', 'Test']  # 4й элемент ввёл для разницы длин списков
second_list = ['Строка', 'Урбан', 'Компьютер']

# Решение:
first_result = (abs(len(a) - len(b)) for a, b in zip(first_list, second_list) if len(a) != len(b))
second_result = (len(first_list[i]) == len(second_list[i]) for i in range(min(len(first_list), len(second_list))))

print(list(first_result))
print(list(second_result))

# 2й вариант решения первой задачи - через моржовый оператор
first_result = (a for x, y in zip(first_list, second_list) if (a := abs(len(x) - len(y))))
print(list(first_result))