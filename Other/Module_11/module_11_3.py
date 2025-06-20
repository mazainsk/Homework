# Домашнее задание по теме "Интроспекция"
# Примечание: сейчас решил НЕ использовать модуль inspect, а обойтись встроенными инструментами.

import requests
import matplotlib.pyplot as plt


class IntrospectionInfo:
    """
    Класс интроспекции объекта.
      Возвращает тип объекта, перечень его атрибутов и методов, а также значения атрибутов экземпляра класса.
    Параметры:
      obj - проверяемый объект;
      short_list_option (по-умолчанию = True) - флаг сокращенного вывода: указывает не выводить скрытые и "магические"
        атрибуты, текст выводимых значений атрибутов обрезается до двух первых строк.
    """
    def __init__(self, obj, short_list_option: bool = True):
        self._obj = obj
        self._short_list = short_list_option

    def __str__(self):
        info = (f'\nТип объекта: {type(self._obj)}\nПринадлежность модулю: ' +
                (f'{self._obj.__module__}\n' if hasattr(self._obj, '__module__') else 'n/a\n') +
                'Вызываемый объект: ' + ('Да\n' if callable(self._obj) else 'Нет\n') +
                f'\nОписание объекта:\n' + '=' * 60 + '\n' +
                (f'{self._obj.__doc__}\n' if hasattr(self._obj, '__doc__') else 'Отсутствует\n') +
                f'\nАтрибуты и методы:\n' + '=' * 60)
        attr_methods = dir(self._obj)
        for item in attr_methods:
            if not self._short_list or (self._short_list and item[0] != '_'):
                info += f'\n{item}'
        info += '\n\nЗначения атрибутов экземпляра класса:\n' + '=' * 60
        if hasattr(self._obj, '__dict__'):
            attributes = vars(self._obj)    # Аналогично self._obj.__dict__
            if attributes == {}:
                info += '\nПусто\n'
            else:
                for key, value in attributes.items():
                    if not self._short_list or (self._short_list and str(value).count('\n') < 2 and key[0] != '_'):
                        info += f'\n{key}: {value}'
                    elif self._short_list and str(value).count('\n') > 1 and key[0] != '_':
                        # Вывести только первые две строки:
                        text = '\n'.join(str(value).split('\n')[:2])
                        info += f"\n{key}: {text}\n.../it's too long string to print/..."
                info += '\n'
        else:
            info += '\nУ данного объекта отсутствует "магический" метод __dict__().\n'
        return info


class TestClass:
    """Класс для проверки интроспекции"""
    class_attribute = '???'

    def __init__(self):
        self.txt_value = 'Просто текст'

    def fake_method(self):
        pass

    def __str__(self):
        return self.txt_value


def test_mul(x, y):
    """Функция возведения в степень"""
    return x ** y


# Проверка на тестовых данных:
tst_1 = IntrospectionInfo(plt.figure, False)
print('Объект: Функция <matplotlib.pyplot.figure>', tst_1)
tst_2 = IntrospectionInfo(requests)
print('Объект: Модуль <requests>', tst_2)
tst_3 = IntrospectionInfo(51, False)
print('Объект: Число <51>', tst_3)
tst_4 = IntrospectionInfo(list)
print('Объект: Встроенная функция <list>', tst_4)
tst_5 = IntrospectionInfo(TestClass())  # Экз
print('Объект: Экземпляр класса <TestClass>', tst_5)
tst_6 = IntrospectionInfo(test_mul)
print('Объект: Функция <test_mul> в текущем модуле', tst_6)
