class House:

    def __init__(self, name: str, number_of_floors: int):
        self.name = name
        self.number_of_floors = number_of_floors
        print(f'Создано здание "{self.name}" с количеством этажей {self.number_of_floors}')

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return 'Название: "' + self.name + '", кол-во этажей: ' + str(self.number_of_floors)

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

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))