# Домашнее задание по теме "Форматирование строк"

team1_num = 5      # Количество участников команды 1. Только целое число, иначе подстановка %d и вызов функции suffix
team2_num = 6      # приведет к неверному результату.
team1_name = 'Мастера кода'
team2_name = 'Волшебники данных'
score_1 = 40        # Количество задач, решённых командой 1
score_2 = 41
team1_time = 1552.512   # 1552.512 - время, за которое команда 1 решила задачи
team2_time = 2153.31451 # 2153.31451 - время, за которое команда 2 решила задачи

tasks_total = score_1 + score_2        # общее количество решённых задач
time_avg = (team1_time + team2_time) / tasks_total  # среднее время решения одной задачи
challenge_result = '' # Исход соревнования, например, 'Победа команды Волшебники данных!'

def suffix(word: str, num):
    # Функция возвращает слово с добавленным окончанием для порядковых числительных к словам "участник", "задача".
    # Еще для таких случаев можно использовать библиотеки pymorphy2 и morpher
    # PS: если функцию использовать как самодостаточную во внешнем модуле, то переменную words лучше заменить на
    # константу WORDS или _WORDS, но тут пусть будет так.
    words = {'участник': ['', 'а', 'ов'], 'задач': ['у', 'и', '']}  # Корни и окончания
    if word not in words or not isinstance(num, (float, int)):
        return word
    if isinstance(num, float):
        return word + words[word][1]
    num = int(str(num)[-1])
    if num == 1:
        return word + words[word][0]
    elif 2 <= num <= 4:
        return word + words[word][1]
    else:
        return word + words[word][2]

# Использование %:
print('В команде "%s" %d %s' % (team1_name, team1_num, suffix('участник', team1_num)))
print('Итого сегодня в командах: %d и %d участников' % (team1_num, team2_num))

# Использование format():
print('Команда "{}" решила {} {}'.format(team2_name, score_2, suffix('задач', score_2)))
print('"{}" решили задачи за {} сек.'.format(team2_name, round(team2_time, 2)))

# Использование f-строк:
if score_1 > score_2 or (score_1 == score_2 and team1_time < team2_time):
    challenge_result = f'победа команды "{team1_name}"!'
elif score_1 < score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = f'победа команды "{team2_name}"!'
else:
    challenge_result = 'ничья!'
print(f'Команды решили {score_1} и {score_2} {suffix('задач', score_2)}')
print(f'Результат битвы - {challenge_result}')
print(f'Сегодня команды решили {tasks_total} {suffix('задач', score_2)}, в среднем по '
      f'{round(time_avg, 2)} секунд на задачу')