# Домашнее задание по теме "Создание функций на лету"

# Задача "Lambda-функция":
first = 'Мама мыла раму'
second = 'Рамена мало было'
# Должен получиться список совпадения букв по результатам сравнения списков:
# [False, True, True, False, False, False, False, False, True, False, False, False, False, False]

print(list(map(lambda a, b: a == b, first, second)))


# Задача "Замыкание":
# Функция должна принимать название файла для записи, внутри - функция, принимающая неограниченное количество данных
# любого типа и добавляющая их в файл в том же виде.

def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a', encoding='utf-8') as f:
           [f.write(str(value) + '\n') for value in data_set]
    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'], list[(25,38)], None, True)


# Задача с объектом класса (случайный выбор из заданной коллекции).

# import нужно писать в начале модуля, но в данном случае тут будет показательнее
import random
import pymorphy3    # pip install pymorphy3

class MysticBall:

    def __init__(self, *words):
        self.words = words

    def __call__(self, iters=1):
        iters = min(iters, len(self.words))  # обрезка для случая, когда iters > len(self.words)
        # Случайные неповторяющиеся номера элементов в words в том порядке, в котором они заданы при инициализации
        choices = sorted(random.sample(range(len(self.words)), iters))
        return ', '.join(f'{self.words[i]}' for i in choices)

morph = pymorphy3.MorphAnalyzer()
day_word = morph.parse('день')[0]
win_days = MysticBall('понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'СЕГОДНЯ!')

num_of_win_days = 2     # можно задавать от 1 и больше (обрежется по размеру коллекции)
print(f'Вот {num_of_win_days} {day_word.make_agree_with_number(num_of_win_days).word}, '
      f'когда вам придется сверхурочно поработать на следующей неделе:')
print(win_days(num_of_win_days))

# print(win_days())     # можно вот так, тогда будет выводиться по одному элементу коллекции, но при нескольких
                        # повторениях будут повторы