# Домашнее задание по теме "Создание потоков"

import time
from threading import Thread
from tqdm import trange


def write_words(word_count: int, file_name: str, pbar):
    with open(file_name, 'w', encoding='utf-8') as f:
        for i in range(1, word_count + 1):
            f.write(f'Какое-то слово № {str(i)}\n')
            pbar.update(1)
            time.sleep(0.1)

# Данные (количество слов) для всех примеров:
data_ = (10, 30, 200, 100)

# Последовательный вызов функции для всех входных данных:
time_ = time.time()
print('Последовательная запись, 4 файла в 1 поток:')
for i, v in enumerate(data_):
    file_name = f'example{i+1}.txt'
    with trange(v, bar_format='{l_bar}{bar}| {n_fmt}/{total_fmt}{postfix}') as pbar:
        pbar.set_postfix_str('Обработка...')
        write_words(v, file_name, pbar)
        pbar.set_postfix_str('Готово')
time_ = time.time() - time_
print(f'Время работы {time_:.2f} сек.')

# Вызов каждой функции в отдельном потоке с общим прогресс-баром:
time_ = time.time()
print('Параллельная запись, 4 файла в 4 потока:')
threads = []
# Пауза для того, чтобы предыдущая строка (print) успела отобразиться в консоли до следующего прогресс-бара
time.sleep(0.1)
with trange(sum(data_), postfix=f'Обработка...', bar_format='{l_bar}{bar}| {n_fmt}/{total_fmt}{postfix}') as pbar:
    for i, v in enumerate(data_):
        t = Thread(target=write_words, args=(v, f'example{i+5}.txt', pbar))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    pbar.set_postfix_str('Готово')
time_ = time.time() - time_
print(f'Время работы {time_:.2f} сек.')
