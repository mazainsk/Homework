# Домашнее задание по теме "Потоки на классах"

import time
import pymorphy3
import random
from threading import Thread


class Knight(Thread):
    _Enemies = 100

    def __init__(self, name: str, power: int):
        super().__init__()
        self.name = name
        self.power = power
        self.power_mod = 1

    def run(self):
        morph = pymorphy3.MorphAnalyzer()
        day_word = morph.parse('день')[0]
        warrior_word = morph.parse('воин')[0]
        print(f'{self.name}, на нас напали!')
        days_of_battle = 0
        while self._Enemies > 0:
            if random.randint(1, 10) == 3 and self.power_mod == 1:
                self.power_mod =0.8
                print(f'{self.name} ранен! Его сила снижена на 20% до конца битвы...')
            self._Enemies -= int(self.power * self.power_mod)
            if self._Enemies < 0:
                self._Enemies = 0
            warriors_word = warrior_word.make_agree_with_number(self._Enemies).word
            days_of_battle += 1
            days_word = day_word.make_agree_with_number(days_of_battle).word
            print(f'{self.name} сражается {days_of_battle} {days_word}..., осталось {self._Enemies} {warriors_word}.')
            time.sleep(1)
            if self._Enemies == 0:
                print(f'{self.name} одержал победу спустя {days_of_battle} {days_word}!')


warriors = {'Sir Lancelot': 10, 'Sir Galahad': 20, "Sir C'Urban (Dallas)": 13}
w_threads = []
for name, power in warriors.items():
    w = Knight(name, power)
    w.start()
    w_threads.append(w)
for w in w_threads:
    w.join()
print('Все битвы закончились!')