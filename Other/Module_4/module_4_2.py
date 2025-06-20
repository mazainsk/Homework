def test_function():

    def inner_function():
        print('Я в области видимости функции test_function')

    inner_function()  # п.3 - вызов функции inner_function внутри функции test_function


inner_function()  # п.3 - вызов функции inner_function вне функции test_function; попытка неудачная,
                    # т.к. функция inner_function находится в локальной области видимости функции test_function,
                    # и, соответственно, не видна из глобального пространства имен модуля.