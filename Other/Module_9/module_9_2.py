# Домашнее задание по теме "Списковые, словарные сборки"

first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

# Список из длин строк списка first_strings, при условии, что длина строки не менее 5 символов.
first_result = [len(i) for i in first_strings if len(i) >= 5]

# Список из кортежей - пар слов одинаковой длины.
# Каждое слово из списка first_strings должно сравниваться с каждым из second_strings.
second_result = [(i, j) for i in first_strings for j in second_strings if len(i) == len(j)]

# Словарь, где пара ключ-значение это строка-длина строки. Значения строк - из объединённых вместе списков
# first_strings и second_strings. Условие записи пары в словарь - чётная длина строки.
third_result = {i: len(i) for i in first_strings + second_strings if not len(i) % 2}

print(first_result)
print(second_result)
print(third_result)