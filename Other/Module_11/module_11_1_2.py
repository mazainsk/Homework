# Домашнее задание по теме "Обзор сторонних библиотек Python".
# Часть 2. Пример использования сторонних библиотек для работы с изображениями.

from matplotlib import animation
from matplotlib import pyplot as plt
from PIL import Image, ImageEnhance  # pillow
from PIL.Image import Resampling


# Пункт 1. Простейшие манипуляции с изображением (использование pillow).
# ----------------------------------------------------------------------
filename = "DSC04533.JPG"
with Image.open(filename) as img:
    img.load()
print(f'Свойства исходного изображения (файл "{filename}"):', f' - формат {img.format}',
      f' - размер (разрешение) {img.width} x {img.height} пикселей', f' - режим {img.mode}', sep='\n')

# Модификация изображения
img_rotated = img.rotate(-7, resample=Resampling.BICUBIC)  # Поворот на 7 градусов по часовой стрелке.
img_cropped = img_rotated.crop((800, 30, 2050, 1820))  # Обрезка. В скобках - отступ от левого верхнего угла исходного
    # изображения для нового левого-верхнего угла (800 вправо, 30 вниз) и правого-нижнего угла (2050 вправо, 1820 вниз).
img = ImageEnhance.Contrast(img_cropped).enhance(1.2)  # Повышение контраста на 20%.
img_gray = img.convert("L")  # Преобразование в оттенки серого.
low_res_img = img_gray.reduce(2)  # Уменьшение разрешения в 2 раза. Также можно использовать метод resize.

# Запись модифицированного изображения в новый файл в текущем каталоге проекта.
new_filename = "puppy.png"
low_res_img.save(new_filename)

# Считывание записанного изображения, чтобы проверить его формат (он должен выбираться автоматически по расширению,
# которое назначалось при записи).
with Image.open(new_filename) as new_img:
    new_img.load()
print(f'Свойства модифицированного изображения (файл "{new_filename}"):', f' - формат {new_img.format}',
      f' - размер (разрешение) {new_img.width} x {img.height} пикселей', f' - режим {new_img.mode}', sep='\n')
# print(low_res_img.size)  # Размер изображения можно выводить как кортеж.

# Показать итоговое изображение программой-просмотрщиком в ОС.
low_res_img.show()


# Пункт 2. Создание GIF-файла анимации из набора кадров в одном исходном изображении (использование pillow).
# ----------------------------------------------------------------------------------------------------------
img_animation = []  # Список, где будут все кадры GIF-анимации.
filename = "DSC04548.JPG"  # В этом файле 16 кадров: 4 строки по 4 столбца.
with Image.open(filename) as img:
    img.load()
width_step = img.width // 4
height_step = img.height // 4
# Цикл нарезки кадров.
for y in range(0, img.height, height_step):
    for x in range(0, img.width, width_step):
        img_animation.append(img.crop((x, y, x + width_step - 1, y + height_step - 1)))
img_animation[0].save("animation.gif", save_all=True, append_images=img_animation[1:], loop=1)


# Пункт 3. Воспроизведение GIF-файла анимации (использование pillow + matplotlib).
# --------------------------------------------------------------------------------
filename = "animation.gif"
with Image.open(filename) as gif:
    gif.load()
    # Получение списка frames из кадров gif
    frames = []
    try:
        while True:
            frames.append(gif.copy())  # Копирование кадра в список.
            gif.seek(gif.tell() + 1)   # Переход к следующему кадру в открытом файле.
    except EOFError:
        pass  # Возбуждение исключения - это конец GIF, так что можно ничего не делать.

fig, ax = plt.subplots()  # Создание фигуры fig и осей ax для отображения анимации.
patch = plt.imshow(frames[0])  # Отображение первого кадра из списка frames на графике с помощью функции imshow.

# Функция обновления изображения для текущего кадра; она получает кадр и устанавливает его в patch.
def update(frame):
    patch.set_data(frame)
    return patch,

# Создание анимации (метод matplotlib.animation.FuncAnimation) путём вызова функции update в фигуре fig для каждого
# кадра в списке frames с интервалом 100 мс и опцией бесконечного повтора.
my_animation = animation.FuncAnimation(fig, update, frames=frames, interval=100, repeat=True)
# Важное примечание из документации matplotlib:
# надо сохранить созданную анимацию в переменной, которая будет существовать столько времени, сколько должна
# выполняться анимация; в противном случае объект Animation будет удален сборщиком мусора, а анимация прекратится.

plt.axis('off')  # Скрыть оси, потому что у нас 2D-анимация, а не график.
plt.show()      # Показать анимацию.