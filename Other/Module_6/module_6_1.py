# Домашнее задание по теме "Зачем нужно наследование"

class Animal:
    def __init__(self, name: str):
        self.name = name
        self.alive = True   # живой
        self.fed = False    # не накормлен, т.е. голодный

    def __str__(self):      # как информация о себе
        text = f'{self.name} '
        text += '(живой, ' if self.alive else '(мертвый, '
        text += 'сытый)' if self.fed else 'голодный)'
        return text

    def eat(self, food):
        # Универсальный метод для наследников класса Animal
        if not isinstance(food, Animal | Plant) or (isinstance(food, Plant) and not food.edible):
            # Любое животное НЕ может есть еду, которая не относится к классам Animal, Plant или их наследникам,
            # так же эта часть кода сработает для несъедобных растений:
            print(f'{self.name} не стал есть {food}')
            self.alive = False
        elif isinstance(food, Plant) and food.edible:
            # любое животное может есть съедобное растение
            print(f'{self.name} съел {food}')
            self.fed = True
        # тут еда - это точно животное и надо сделать разное поведение для хищника и травоядного (надо дополнить метод
        # в классах-потомках Animal)

class Plant:
    def __init__(self, name: str):
        self.name = name
        self.edible = False  # съедобность

    def __str__(self):      # как информация о себе
        text = f'{self.name} ('
        text += 'не ' if not self.edible else ''
        text += 'съедобный)'
        return text

class Mammal(Animal):
    def eat(self, food):
        super().eat(food)
        if self.alive and not self.fed: # если остался живым и голодным, значит еда - это другое животное
            print(f'{self.name} не стал есть {food}')
            self.alive = False

class Predator(Animal):
    def eat(self, food):
        super().eat(food)
        if self.alive and not self.fed: # если остался живым и голодным, значит еда - это другое животное
            # в качестве еды он съест любое другое животное, даже падаль
            print(f'{self.name} съел {food}')
            self.fed = True
            food.alive = False      # жизнь животного, которого съели, прекратилась

class Flower(Plant):
    pass        # просто заглушка, потому что все атрибуты и методы определены в родительском классе

class Fruit(Plant):
    def __init__(self, name: str):
        super().__init__(name)
        self.edible = True          # переопределить атрибут, унаследованный от родительского класса




if __name__ == '__main__':

    # Проверка на тестовых данных
    a1 = Predator('Волк с Уолл-Стрит')
    a2 = Mammal('Хатико')
    p1 = Flower('Цветик семицветик')
    p2 = Fruit('Заводной апельсин')
    a3 = Predator('Другой хищник')
    a4 = Mammal('Другой травоядный')
    print('Перечень всех объектов:')
    print(a1, a2, p1, p2, sep='\n', end='\n'*2)
    print('Прямое обращение к атрибутам:')
    print(f'Значение атрибута alive для {a1.name}:', a1.alive)
    print(f'Значение атрибута fed для {a2.name}:',a2.fed)
    print()
    a1.eat(p1)
    print(a1)
    a2.eat(p2)
    print(a2)

    # Что произошло: Хищник попытался съесть цветок и погиб, млекопитающее съело фрукт и насытилось.