# Домашнее задание по теме "Файлы в операционной системе"

import os
import time
from tkinter import filedialog as fd
from tkinter import messagebox as mb

def get_file_paths_scandir(start_dir):
    # Использую наиболее быстрый метод, доступный с Python 3.5:
    # os.scandir() возвращает итератор, поддерживающий протокол менеджера контекста, поэтому с ним лучше использовать
    # with или закрывать итератор и освобождать ресурсы явным вызовом os.scandir.close()
    with os.scandir(start_dir) as entries:
        for entry in entries:
            if entry.is_file():
                filetime = os.path.getmtime(entry.path)
                formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
                print(f'Обнаружен файл: {entry.name}, Путь: {entry.path}, Размер: {os.path.getsize(entry.path)} байт, '
                      f'Время изменения: {formatted_time}, Родительская директория: {directory}')
            else:
                # if entry.is_dir(): - можно так, но это избыточно, потому что, если entry не файл, то - директория
                get_file_paths_scandir(entry.path)  # рекурсивный вызов по подкаталогу

while True:
    directory = fd.askdirectory(title="Выбор папки для сканирования содержимого", initialdir="/")
    if directory:
        # Если действительно что-то выбрано (даже недопустимый путь):
        try:
            get_file_paths_scandir(directory)
        except PermissionError:
            # На Win10 исключение возникнет, например, при попытке сканирования корня диска 'С'
            if mb.askretrycancel("Отказано в доступе", "Повторить выбор папки?"): continue
        break
    else:
        if mb.askyesno("Не выбрано", "Хотите выйти?"): break