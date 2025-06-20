calls = 0   # начальное значение глобальной переменной - счетчика вызова функций

# Функция подсчитывает вызовы остальных функций
def count_calls():
    global calls    # ссылка на то, что переменная - в глобальном пространстве имен, а не локальная внутри функции
    calls += 1
    return

# Функция принимает аргумент-строку и возвращает кортеж из длины этой строки, строки в верхнем и нижнем регистре
def string_info(string):
    count_calls()       # увеличение счетчика вызова функций
    if not isinstance(string, str): # если в функцию передан аргумент не строкового типа, ..
        string = str(string)        # ..то преобразовать в строковый тип
    return len(string), string.upper(), string.lower()    # возврат необходимых значений (см.описание ф-ции)

# Функция принимает строку и список, возвращает True, если строка находится в этом списке, False - если отсутствует.
# Регистр не учитывается.
def is_contains(string, list_to_search):
    count_calls()       # увеличение счетчика вызова функций
    if not isinstance(string, str):
        string = str(string)
    string = string.upper()
    for i in range(len(list_to_search)): # каждый элемент списка преобразовывается в строковый тип, в верхний регистр
        if not isinstance(list_to_search[i], str):
            list_to_search[i] = str(list_to_search[i])
        list_to_search[i] = list_to_search[i].upper()
    return string in list_to_search     # возврат необходимых значений (см.описание ф-ции)

# Вызов функций string_info и is_contains несколько раз с произвольными данными, вывод значения переменной calls
print(string_info('Hello world!'))
print(string_info(True))
print(string_info('Terminator-2024'))
print(is_contains('neWtoN', ['Bart', 'Newton', 'Stevenson']))
print(is_contains('16', ['Yellow', 'Twelve', True, 16]))
print(is_contains('tru', ['Yellow', 'Twelve', True, 16]))
print(calls)
