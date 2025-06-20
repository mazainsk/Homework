# Домашнее задание по теме "Асинхронность на практике"
# Цель: приобрести навык использования асинхронного запуска функций на практике
# Задача "Асинхронные силачи"

import asyncio


strongman_data = {'Василий': 30, 'Балагур': 50, 'Чарли': 80}
power_const = 90
balls_max = 5

async def start_strongman(name, power):
    balls_count = 0
    print(f'Силач {name} начал соревнования')
    while balls_count < balls_max:
        await asyncio.sleep(power_const/power)
        balls_count += 1
        print(f'Силач {name} поднял {balls_count} шар')
    print(f'Силач {name} закончил соревнования')

async def start_tournament():
    task_list = []
    for i, v in enumerate(strongman_data.items()):
        task_list.append(asyncio.create_task(start_strongman(*v)))
    for task in task_list:
        await task


if __name__ == '__main__':
    asyncio.run(start_tournament())