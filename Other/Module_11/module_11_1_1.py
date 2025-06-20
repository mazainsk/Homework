# Домашнее задание по теме "Обзор сторонних библиотек Python".
# Часть 1. Пример использования сторонних библиотек для расчета и вывода изображения известного фрактала - множества
# Мандельброта на комплексной плоскости.

from copy import deepcopy
import numpy as np
import matplotlib.pyplot as plt
from tqdm import trange
from PIL import Image
import tkinter as tk

# Исходные данные для расчета:
xmin, xmax, xn = -1.9, +0.5, 800  # Диапазон на оси действительных чисел комплексной плоскости и количество точек по
                                    # горизонтали.
ymin, ymax, yn = -1.2, +1.2, 800  # Диапазон на оси мнимых чисел комплексной плоскости и количество точек по вертикали.
maxiter = 200   # Максимальное число итераций.
horizon = 10.0  # "Горизонт множества" - предельное значение модуля комплексного числа, при выходе за которое
    # считается, что точка НЕ принадлежит множеству Мандельброта и ее цвет характеризуется номером итерации, на которой
    # этот выход произошёл.

# Простейший вариант расчета множества Мандельброта - средствами pillow.
mandel = Image.effect_mandelbrot(size=(xn, yn), extent=(xmin, ymin, xmax, ymax), quality=maxiter)

# Более изощренный вариант - работа с массивами numpy.
# Создание линейных пространств:
X = np.linspace(xmin, xmax, xn).astype(np.float32)  # массив из xn значений, равномерно распределенных от xmin до xmax.
Y = np.linspace(ymin, ymax, yn).astype(np.float32)  # массив из yn значений, равномерно распределенных от ymin до ymax.
# Создание двумерных массивов:
# Начальные значения для точек множества Мандельброта:
C = X + Y[:, None] * 1j  # Y[:, None] * 1j добавляет измерение, преобразуя Y в столбец мнимых частей комплексных чисел.
# Количество итераций:
N = np.zeros_like(C, dtype=int)  # Массив целочисленного типа размерностью как С, заполненный нулями.
# Точки множества Мандельброта для текущей итерации:
Z = np.zeros_like(C)             # Массив комплексных чисел размерностью как С, заполненный нулями.
# Цикл вычислений:
for n in trange(maxiter):
    I = abs(Z) < horizon  # Массив-маска (тип boolean) - находится ли модуль значения точки Z в пределах horizon.
    N[I] = n  # Номер текущей итерации записывается во все элементы N, соответствующие элементам I = True.
    Z[I] = Z[I]**2 + C[I]  # Пересчет значений для элементов множества, которые находятся в пределах horizon.
N[N == maxiter-1] = 0  # Сброс номера итерации для элементов множества, значения которых остались в пределах horizon
                        # даже после maxiter итераций.

dpi = 96    # Плотность пикселей на дюйм для экрана моего ноутбука.
fig_1 = plt.figure(figsize=(xn/dpi, yn/dpi)).add_axes((0, 0, 1, 1))  # (left, bottom, width, height) - в долях от w/h
fig_1.imshow(mandel, extent=(xmin, xmax, ymin, ymax), interpolation="kaiser")
plt.axis('off')  # Выключить отображение подписей на осях.

# Позиционирование изображений:
# Создание скрытого окна
root = tk.Tk()
root.withdraw()  # Скрыть главное окно
# Получение разрешения экрана
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
# print("Разрешение экрана:", screen_width, "x", screen_height)
# Вычисление смещений:
width_corr = 50  # Не знаю почему, но реальная ширина окна меньше, чем xn.
height_corr = 120  # Высота окна больше, чем yn из-за нижней панели и заголовка.
offset_left = (screen_width - (xn + width_corr) * 2) // 3
offset_top = (screen_height - yn - height_corr) // 2
# Позиционирование текущего окна:
plt.get_current_fig_manager().window.wm_geometry(f'+{offset_left}+{offset_top}')
plt.get_current_fig_manager().set_window_title('Using pillow')
# Подготовка и вывод изображения во второе окно:
offset_left = offset_left * 2 + xn + width_corr
fig_2 = deepcopy(fig_1)
fig_2.imshow(N, extent=(xmin, xmax, ymin, ymax), interpolation="kaiser")
plt.get_current_fig_manager().window.wm_geometry(f'+{offset_left}+{offset_top}')
plt.get_current_fig_manager().set_window_title('Using numpy')

plt.show()

# ПРИМЕЧАНИЯ:
# Часть по работе с массивами numpy взял отсюда (но не стал использовать затенение и нормализацию для цветовой карты
  # преобразования):
  # https://matplotlib.org/stable/gallery/showcase/mandelbrot.html#sphx-glr-gallery-showcase-mandelbrot-py
# По интерполяциям смотрел здесь:
  # https://matplotlib.org/stable/gallery/images_contours_and_fields/interpolation_methods.html