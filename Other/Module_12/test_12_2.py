# Доработанный вариант исходного кода, взятого с GitHub:
# https://github.com/yanchuki/HumanMoveTest/blob/master/runner_and_tournament.py
# Доработка понадобилась для выявления юнит-тестами неполадок при различных вариантах поведения программы.

class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()

                # Исходный вариант расчета занятых мест:
                if participant.distance >= self.full_distance:
                    finishers[place] = participant.name  # В исходном виде здесь ошибочно был сам объект, а не имя!
                    place += 1
                    self.participants.remove(participant)
        return finishers

                # Исходный вариант расчета занятых мест имеет логическую ошибку, т.к. перебор участников забега идет
                # в той же последовательности, в которой эти участники задавались при создании объекта Tournament,
                # что приводит к ситуации, когда на короткой дистанции бегун с меньшей скоростью (но переданный в
                # Tournament первым) может ошибочно занять первое место из-за того, что бегун с большей скоростью
                # (который был передан вторым) в прошлой итерации еще не достиг финиша, а в текущей - достигнет
                # его вторым по причине более позднего расчета своей пройденной дистанции в цикле.

            # # Модифицированный вариант расчета занятых мест. Ждет, пока все участники забега достигнут финиша.
            # # Но как и исходный вариант не имеет проверки на равность скоростей бегунов и, соответственно, не
            # # учитывает возможность их одновременного финиша и разделения общей позиции между несколькими участниками.
            # if all([participant.distance >= self.full_distance for participant in self.participants]):
            #     results_ = [(i.distance, i.name) for i in self.participants]
            #     results_sorted = sorted(results_, reverse=True)
            #     # results_names = [results_dict[i] for i in results_distances]
            #     for i in results_sorted:
            #         finishers[place] = i[1]
            #         place += 1
            #     return finishers


# Локальный тест корректности расчета победителей для случая забега на короткую дистанцию:
# if __name__ == '__main__':
#
#     runners_data = {'Ник': 3, 'Андрей': 9, 'Усэйн': 10}
#     runners = []
#     for name_, speed_ in runners_data.items():
#         runners.append(Runner(name_, speed_))
#     print('Стартуют: ', runners_data, sep='\n')
#     finish_order = sorted(runners_data.items(), key=lambda item: item[1], reverse=True)  # list of tuples
#     finish_order = {i + 1: v[0] for i, v in enumerate(finish_order)}                     # dict
#     print('Ожидаемый порядок финиширования: ', finish_order, sep='\n')
#     results = Tournament(5, *runners).start()
#     print('Фактический финиш на дистанции 5: ', results, sep='\n')
#     results = Tournament(18, *runners).start()
#     print('Фактический финиш на дистанции 18: ', results, sep='\n')
