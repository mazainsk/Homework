# Домашнее задание по теме "Систематизация и пропуск тестов".
# Задача "Заморозка кейсов".

import unittest as ut
from module_12_1 import RunnerTest
from module_12_2_1 import TournamentTest

simple_ts = ut.TestSuite()
simple_ts.addTests(ut.TestLoader().loadTestsFromTestCase(RunnerTest))
simple_ts.addTests(ut.TestLoader().loadTestsFromTestCase(TournamentTest))

runner_ts = ut.TextTestRunner(verbosity=2)
runner_ts.run(simple_ts)