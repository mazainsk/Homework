# Домашнее задание по теме "Многопроцессное программирование"
# Необходимо считать информацию из нескольких файлов одновременно, используя многопроцессный подход,
# и сравнить с однопоточной работой, закомментировав/раскомментировав соответствующие фрагменты кода.

from concurrent.futures import ProcessPoolExecutor    # Альтернатива Pool из multiprocessing
# from multiprocessing import Pool
from timeit import timeit


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        for line in file:
            all_data.append(line)
    print(f'{name[2:]} - ok')

def main():
    with ProcessPoolExecutor(4) as pool:   # Можно заменить на Pool из multiprocessing
        pool.map(read_info, filenames)


filenames = [f'./file {i}.txt' for i in range(1, 5)]

# Последовательное чтение (3,8-3,9 сек)

# read_time = timeit("[read_info(filename) for filename in filenames]", globals=globals(), number=1)
# print(f'Время выполнения {read_time:.2f} секунд')

# Параллельное, в 4х процессах (~1,6 сек)

if __name__ == '__main__':
    read_time = timeit("main()", globals=globals(), number=1)
    print(f'Время выполнения {read_time:.2f} секунд')