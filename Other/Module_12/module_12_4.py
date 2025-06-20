# Домашнее задание по теме "Логирование".
# Задача "Логирование бегунов".
# Цель: получить опыт использования простейшего логирования совместно с тестами.


import unittest as ut
import test_12_4 as test
import logging

logging.basicConfig(filename='runner_tests.log', filemode='w', encoding='utf-8',
                    level=logging.INFO, datefmt='%Y_%m_%d %H:%M:%S',
                    format='%(asctime)s %(name)s %(levelname)s: %(message)s [%(module)s | %(threadName)s]')

class RunnerTest(ut.TestCase):
    is_frozen = False

    @ut.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            # Отрицательное значение - для проверки логгирования ошибки.
            person = test.Runner('Вовка', speed=-5)
            for i in range(10):
                person.walk()
            self.assertEqual(person.distance, 50)
        except ValueError:
            logging.warning('Неверная скорость для Runner', exc_info=True)
        except TypeError:
            logging.warning('Неверный тип данных для имени объекта Runner')
        else:
            logging.info('"test_walk" выполнен успешно')

    @ut.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            # Неверное имя - для проверки логгирования ошибки.
            person = test.Runner(24.16)
            for i in range(10):
                person.run()
            self.assertEqual(person.distance, 100)
        except ValueError:
            logging.warning('Неверная скорость для Runner', exc_info=True)
        except TypeError:
            logging.warning('Неверный тип данных для имени объекта Runner', exc_info=True)
        else:
            logging.info('"test_run" выполнен успешно')

    @ut.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run_2(self):
        try:
            # Корректная работа, в лог запишется то, что указано в блоке <else>.
            person = test.Runner('Маша')
            for i in range(10):
                person.run()
            self.assertEqual(person.distance, 100)
        except ValueError:
            logging.warning('Неверная скорость для Runner', exc_info=True)
        except TypeError:
            logging.warning('Неверный тип данных для имени объекта Runner', exc_info=True)
        else:
            logging.info('"test_run" выполнен успешно')

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
