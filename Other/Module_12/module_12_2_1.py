# Домашнее задание по теме "Методы Юнит-тестирования"
# Вариант 1, максимально близкий к формулировке задачи.

import unittest as ut
from test_12_2 import Runner, Tournament


class TournamentTest(ut.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.distance = 90

    @ut.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def setUp(self):
        self.all_results = {}
        self.runner_1 = Runner('Усэйн', 10)
        self.runner_2 = Runner('Андрей', 9)
        self.runner_3 = Runner('Ник', 3)

    @ut.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def tearDown(self):
        print(self.all_results)

    @classmethod
    def tearDownClass(cls):
        # По условию задачи печать результатов должна быть здесь, но оказалось гораздо удобнее делать это после
        # отработки каждой фикстуры.
        pass

    @ut.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament_1(self):
        self.all_results.update(Tournament(self.distance, self.runner_1, self.runner_3).start())
        self.assertTrue(self.all_results[2] == 'Ник')

    @ut.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament_2(self):
        self.all_results.update(Tournament(self.distance, self.runner_2, self.runner_3).start())
        self.assertTrue(self.all_results[2] == 'Ник')

    @ut.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament_3(self):
        self.all_results.update(Tournament(self.distance,
                                           self.runner_1, self.runner_2, self.runner_3).start())
        self.assertTrue(self.all_results[3] == 'Ник')

    @ut.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament_4(self):
        # Эта фикстура выявляет некорректный расчет финиша при измененной последовательности передачи участников
        # забега и уменьшенной дистанции. При этом на исправленной версии алгоритма расчета финиша ошибок нет нигде.
        self.distance = 5
        self.all_results.update(Tournament(self.distance,
                                           self.runner_3, self.runner_2, self.runner_1).start())
        self.assertTrue(self.all_results[3] == 'Ник' and  self.all_results[1] == 'Усэйн')


if __name__ == '__main__':
    ut.main()