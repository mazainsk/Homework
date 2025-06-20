# Домашнее задание по теме "Множественное наследование"
from random import randint

class Animal:
    _DEGREE_OF_DANGER = 0
    live = True
    sound = None

    def __init__(self, speed=1):
        self._cords = {'x': 0, 'y': 0, 'z': 0}
        self.speed = speed

    def move(self, dx, dy, dz):
        # погружение под воду (отрицательная Z) невозможно, если у объекта нет атрибута dive_in
        if self._cords['z'] + dz * self.speed < 0 and not hasattr(self, 'dive_in'):
            print('Слишком глубоко, я не могу нырять :(')
        else:
            self._cords['x'] += dx * self.speed
            self._cords['y'] += dy * self.speed
            self._cords['z'] += dz * self.speed

    def get_cords(self):
        print(f'X: {self._cords['x']}, Y: {self._cords['y']}, Z: {self._cords['z']}')

    def attack(self):
        print('Простите, я миролюбивый :)') if self._DEGREE_OF_DANGER < 5 else print('Осторожно, я атакую! 0_0')

    def speak(self):
        print(self.__class__.__name__, ' издаёт звук "', self.sound, '"', sep='')

class Bird(Animal):
    beak = True

    def lay_eggs(self):
        eggs = randint(1, 4)
        print(f'И вот я снесла {eggs} яйц', end='')
        print('о ', end='') if eggs == 1 else print('а ', end='')
        print('для вас')

class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        self._cords['z'] = self._cords['z'] - abs(dz) // 2 * self.speed

class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8

class Duckbill(Bird, PoisonousAnimal, AquaticAnimal):
    sound = "клик-клик-клик"


if __name__ == '__main__':

    db = Duckbill(10)
    print(db.live)
    print(db.beak)
    db.speak()
    db.attack()
    db.move(1, 2, -3)   # погрузиться под воду сможет
    db.get_cords()
    db.dive_in(4)
    db.get_cords()
    db.lay_eggs()

    # объект без атрибута dive_in не сможет нырять
    b1 = Bird(5)
    b1.move(1,2,-3)     # погрузиться под воду не сможет
    b1.get_cords()              # координаты останутся 0-0-0

    print(dir(db))      # проверка наличия всех наследованных атрибутов и методов

    # Вывод на консоль:
    # True
    # True
    # Duckbill издаёт звук "клик-клик-клик"
    # Осторожно, я атакую! 0_0
    # X: 10, Y: 20, Z: -30
    # X: 10, Y: 20, Z: -50
    # И вот я снесла <?> яйца для вас   (число яиц - от 1 до 4)
    # Слишком глубоко, я не могу нырять :(
    # X: 0, Y: 0, Z: 0
    # <список методов и атрибутов>