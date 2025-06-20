# Домашнее задание по теме "Методы Юнит-тестирования"
# Вариант 2. Реализовал цикл перебора всех возможных комбинаций из участников забега и вариантов дистанции.
# Пока не разобрался с библиотекой pytest, которая поддерживает декораторы для параметризации,
# поэтому сделал тест-кейс с циклами-подтестами в одной фикстуре.

import unittest as ut
from itertools import permutations
from test_12_2 import Runner, Tournament


class TournamentTest (ut.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.runners_data = {'Усэйн': 10, 'Андрей': 9, 'Ник': 3}
        cls.distances = (90, 15)
        cls.runners = []

    def setUp(self):
        for name_, speed_ in self.runners_data.items():
            self.runners.append(Runner(name_, speed_))
        self.all_results = {}

    def tearDown(self):
        self.runners.clear()
        for tour, result in self.all_results.items():
            print(f'Забег {tour:>2}:')
            print(result[0], ': ', result[1])
            print(result[2], ': ', result[3])

    @classmethod
    def tearDownClass(cls):
        pass

    def test_tournament_with_multiple_inputs(self):
        # Формирование списка кортежей из возможных комбинаций индексов исходного кортежа бегунов;
        # например, для трёх бегунов получается следующий список, соответствующий 12-ти забегам:
        # [(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1),
        #  (0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 0, 1), (2, 1, 0)]
        all_combinations = []
        for r in range(2, len(self.runners_data) + 1):
            all_combinations.extend(permutations((x for x in range(len(self.runners_data))), r))

        # Формирование полного списка исходных данных (аргументов фикстуры) - расширение кортежей до вида
        # (<кол-во участников забега>, <индекс участника (их два или три)>, <дистанция забега>, <индекс быстрейшего
        # бегуна>, <индекс самого медленного бегуна>):
        test_cases = []
        for i in self.distances:
            for j in all_combinations:
                # Список кортежей из скорости бегуна и индекса бегуна:
                speed_list = [(self.runners[x].speed, x) for x in j]
                # Индекс быстрейшего бегуна (выбор из всех возможных индексов в их текущей комбинации):
                fastest = sorted(speed_list, reverse=True)[0][1]
                # Индекс самого медленного бегуна:
                slowest = sorted(speed_list)[0][1]
                # Итоговый (расширенный) список кортежей:
                test_cases.append((len(j), *j, i, fastest, slowest))

        # Цикл забегов в соответствии с подготовленными тестовыми данными:
        tour = 1
        for case in test_cases:
            with self.subTest(case=case):
                # Кол-во бегунов в текущем забеге:
                number_of_runners = case[0]
                # Дистанция текущего забега:
                distance = case[-3]
                # Участники текущего забега:
                participants = [self.runners[case[i + 1]] for i in range(number_of_runners)]
                participants_dict = {participant.name: participant.speed for participant in  participants}
                # Ожидаемые самый быстрый и самый медленный участники забега:
                expected_fastest = self.runners[case[-2]].name
                expected_slowest = self.runners[case[-1]].name
                # Старт тестового забега:
                result = Tournament(distance, *participants).start()
                # Сравнение результатов с эталонными (ожидаемыми) значениями:
                self.assertEqual(result[1], expected_fastest)
                self.assertEqual(result[number_of_runners], expected_slowest)

            # Добавление результата текущего забега в словарь общих результатов:
            self.all_results[tour] = ('Старт', participants_dict, 'Финиш', result)
            tour += 1


if __name__ == '__main__':
    ut.main()