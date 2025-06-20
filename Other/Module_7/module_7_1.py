# Домашнее задание по теме "Режимы открытия файлов"

import os


class Product:

    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:

    __file_name = 'products.txt'
    __is_file_exist = False

    def __init__(self):
        if os.path.isfile(self.__file_name):
            self.__is_file_exist = True

    def get_products(self):
        if self.__is_file_exist:
            with open(self.__file_name, 'r') as  file:  # в конструкции with файл закроется автоматом, без file.close()
                data_prod = file.read().splitlines()    # решил сразу разбивать на элементы
        else:
            data_prod = []
        return data_prod    # возвращаю не единую строку, как в условии задачи, а список (надеюсь, не страшно)

    def add(self, *products: Product):
        existing_products = self.get_products()
        # создается множество из уникальных названий
        existing_names = {line.split(', ')[0] for line in existing_products}    # 0 - name, 1 - weight, 2 - category
        with open(self.__file_name, 'a') as file:
            for product in products:
                if product.name in existing_names:
                    print(f"Продукт {product.name} уже есть в магазине")
                else:
                    file.writelines(f'{product.name}, {product.weight}, {product.category}\n')
            self.__is_file_exist = True


if __name__ == '__main__':

    # Проверка на тестовых данных, файл 'products.txt' нужно предварительно удалить!!
    s1 = Shop()
    print('Продукты, добавляемые в файл:')
    p1 = Product('Potato', 50.5, 'Vegetables')
    p2 = Product('Spaghetti', 3.4, 'Groceries')
    p3 = Product('Potato', 5.5, 'Vegetables')   # дубликат имени, но запишется отдельным элементом
    print(p1, p2, p3, sep='\n')
    print('Список из файла ДО добавления в него новых продуктов:', s1.get_products(), sep='\n')
    s1.add(p1, p2, p3)
    print('Список из файла ПОСЛЕ добавления в него новых продуктов:', s1.get_products(), sep='\n')

    print()
    print('Еще продукты, добавляемые в файл:')
    p3 = Product('Potato', 1, 'Veg')            # повтор имени, данные не добавятся
    p4 = Product('Apples', 18.1, 'Fruits')      # новый продукт, добавится
    print(p3, p4, sep='\n')
    print('Список из файла ДО добавления в него новых продуктов:', s1.get_products(), sep='\n')
    s1.add(p3, p4)
    print('Список из файла ПОСЛЕ добавления в него новых продуктов:', s1.get_products(), sep='\n')
