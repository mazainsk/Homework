# Домашнее задание по теме "Очереди для обмена данными между потоками"
# Необходимо имитировать ситуацию с посещением гостями кафе.

import time
from queue import Queue
from threading import Thread
from random import randint


class Table:
    """Стол, хранит информацию о находящемся за ним гостем (Guest)"""

    def __init__(self, number: int):
        self.number = number
        self.guest = None  # У каждого объекта "стол" свой гость, поэтому сделал атрибутом объекта, а не класса


class Guest(Thread):
    """Гость, поток, при запуске которого происходит задержка от 3 до 10 секунд"""

    def __init__(self, name: str):
        super().__init__()
        self.name = name

    def run(self):
        time.sleep(randint(3, 10))


class Cafe:
    """Кафе, в котором есть определённое кол-во столов и происходит имитация прибытия гостей (guest_arrival) и их
       обслуживания (discuss_guests)"""

    def __init__(self, *args: Table):
        self.tables = args
        self.queue = Queue()
        self.guests = None

    def guest_arrival(self, *args: Guest):
        self.guests = args
        for guest in self.guests:
            for table in self.tables:
                if table.guest is None:
                    table.guest = guest
                    table.guest.start()
                    print(f'{guest.name} сел(-а) за стол номер {table.number}')
                    break
            else:
                self.queue.put(guest)
                print(f'{guest.name} в очереди')

    def discuss_guests(self):
        while not self.queue.empty() or any([bool(table.guest) for table in self.tables]):
            for table in self.tables:
                if table.guest and not table.guest.is_alive():
                    print(f'{table.guest.name} покушал(-а) и ушёл(ушла)')
                    table.guest = None
                    print(f'Стол номер {table.number} свободен')
                if table.guest is None and not self.queue.empty():
                    table.guest = self.queue.get()
                    print(f'{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                    table.guest.start()
        print('Все гости ушли, кафе можно закрывать')


# Создание столов
tables = [Table(number) for number in range(1, 6)]

# Имена гостей
guests_names = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman', 'Vitoria', 'Nikita', 'Galina', 'Pavel',
                'Ilya', 'Alexandra']

# Создание гостей
guests = [Guest(name) for name in guests_names]

# Заполнение кафе столами
cafe = Cafe(*tables)

# Приём гостей
cafe.guest_arrival(*guests)

# Обслуживание гостей
cafe.discuss_guests()