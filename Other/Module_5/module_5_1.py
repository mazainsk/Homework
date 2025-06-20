# п.1 - создание класса:
class House:

    # п.2 - создание метода инициализации с передачей в него названия объекта и кол-ва этажей
    def __init__(self, name: str, number_of_floors: int):
        # п.3 - создание нужных атрибутов объекта
        self.name = name
        self.number_of_floors = number_of_floors
        print(f'Создано здание "{self.name}" с количеством этажей {self.number_of_floors}')

    # п.4 - создание метода перемещения на заданный этаж
    def go_to(self, new_floor):
        if 1 <= new_floor <= self.number_of_floors:
            print(f'В здании "{self.name}" едем с 1-го на {new_floor}-й этаж:')
            for i in range(1, new_floor + 1):
                print(i)
        else:
            print(f'{new_floor} - такого этажа в здании "{self.name}" не существует')

# Проверка на тестовых данных:
h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)

h1.go_to(5)
h2.go_to(10)
h2.go_to(0)
h2.go_to(2)