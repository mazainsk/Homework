# Домашнее задание по теме "Простые Юнит-тесты"

import unittest as ut
import test_12_1 as test


class RunnerTest(ut.TestCase):
    is_frozen = False

    @ut.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        person = test.Runner('Вовка')
        for i in range(10):
            person.walk()
        self.assertEqual(person.distance, 50)

    @ut.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        person = test.Runner('Маша')
        for i in range(10):
            person.run()
        self.assertEqual(person.distance, 100)

    @ut.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        person_1 = test.Runner('Гагарин')
        person_2 = test.Runner('Леонов')
        for i in range(10):
            person_1.walk()
            person_2.run()
        self.assertNotEqual(person_1.distance, person_2.distance)


if __name__ == '__main__':
    ut.main()